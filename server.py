"""MCP server that teaches an LLM to build the dock pick-and-drop interaction stably.

Give the model your repo link. It can load the spec and reference from the repo
(or the copy bundled here), follow the build plan, and run a conformance check
on what it wrote before it hands the code back.

Run:  python server.py            (stdio)
Env:  DOCK_REPO_URL  default repo to load from, e.g. https://github.com/you/dock-pick-and-drop
"""
import json
import os
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from mcp.server.fastmcp import FastMCP

HERE = Path(__file__).parent
SPEC = json.loads((HERE / "spec.json").read_text(encoding="utf-8"))
mcp = FastMCP("dock-pick-and-drop")


def _raw_urls(repo_url: str, filename: str) -> list[str]:
    """Turn a github.com repo link into raw URLs. Only github.com is accepted."""
    u = urlparse(repo_url.strip())
    if u.scheme != "https" or u.netloc not in ("github.com", "www.github.com"):
        raise ValueError("Only https://github.com/<user>/<repo> links are supported.")
    parts = [p for p in u.path.split("/") if p]
    if len(parts) < 2:
        raise ValueError("Link must look like https://github.com/<user>/<repo>.")
    user, repo = parts[0], parts[1].removesuffix(".git")
    return [f"https://raw.githubusercontent.com/{user}/{repo}/{b}/{filename}" for b in ("main", "master")]


def _fetch(urls: list[str]) -> str:
    last = None
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                return r.read(2_000_000).decode("utf-8")
        except Exception as e:  # try the next branch name
            last = e
    raise RuntimeError(f"Could not fetch from the repo: {last}")


# ---------------------------------------------------------------- resources
@mcp.resource("dock://spec")
def spec_resource() -> str:
    """Machine-readable spec: states, transitions, tokens, invariants, gotchas, tests."""
    return json.dumps(SPEC, indent=2)


@mcp.resource("dock://reference")
def reference_resource() -> str:
    """Bundled reference implementation (single HTML file, vanilla JS)."""
    return (HERE / "reference" / "index.html").read_text(encoding="utf-8")


# -------------------------------------------------------------------- tools
@mcp.tool()
def get_spec(section: str = "all") -> str:
    """Return the spec. section: all | states | transitions | tokens | invariants | gotchas | test_scenarios."""
    if section == "all":
        return json.dumps(SPEC, indent=2)
    if section not in SPEC:
        return f"Unknown section. Choose from: all, {', '.join(k for k in SPEC if k not in ('name', 'version', 'summary'))}"
    return json.dumps(SPEC[section], indent=2)


@mcp.tool()
def load_from_repo(repo_url: str, filename: str = "index.html") -> str:
    """Fetch a file (default index.html, the reference implementation) from the user's GitHub repo.
    Falls back to the bundled copy if the repo cannot be reached."""
    urls = _raw_urls(repo_url, filename)  # raises on a non-GitHub or malformed link
    try:
        return _fetch(urls)
    except Exception as e:
        if filename == "index.html":
            return f"<!-- repo fetch failed ({e}); bundled reference follows -->\n" + reference_resource()
        raise


PLANS = {
    "vanilla": "Single HTML file. Items are absolutely positioned; JS writes transform every frame from one rAF loop.",
    "react": "Keep per-icon physics (x, y, scale, rotate, velocities) in a useRef array and write style.transform in rAF. Do not put per-frame values in useState. Use state only for the discrete machine state, the order array and the toast.",
    "vue": "Same as React: physics in plain objects outside reactivity (markRaw or a non-reactive array), a single rAF loop, reactive refs only for state name, order and toast.",
    "svelte": "Physics in plain variables updated by one rAF loop that writes to element styles directly. Use stores only for state name, order and toast.",
    "swiftui": "Use DragGesture(minimumDistance: 0) with a 130 ms long-press arm. Held icon offset = drag translation (no animation). Others use .spring(response: 0.3, dampingFraction: 0.75). Commit order on .onEnded, never during .onChanged. Provide accessibilityAction for move and delete.",
}


@mcp.tool()
def get_build_plan(framework: str = "vanilla") -> str:
    """Ordered build plan with the checks to run after each step. framework: vanilla | react | vue | svelte | swiftui."""
    note = PLANS.get(framework.lower())
    if note is None:
        return f"Unknown framework. Choose from: {', '.join(PLANS)}"
    steps = [
        f"0. Framework note: {note}",
        "1. Read get_spec('invariants') and get_spec('gotchas') first. Treat invariants as acceptance criteria.",
        "2. Build the layout as a pure function: slot index per icon from (order, held, insertIdx, intent). No other layout state (I4).",
        "3. Add the spring helper with 8 ms substeps and a 33 ms dt clamp (I8). Drive every non-held value through it.",
        "4. Add the state machine with exactly the states in get_spec('states'). Make setState the only place state changes.",
        "5. Pointer path: pointerdown arms, 130 ms or 6 px lifts, window pointermove drives, pointerup commits, pointercancel and blur cancel. Ignore a second pointer (I1).",
        "6. Held icon: assign position from the pointer each frame (I2), tilt from smoothed velocity, shadow and scale by spring. Resolve slot from the icon centre with 0.62 hysteresis (I7, I9).",
        "7. Commit only on release (I3). On release copy pointer velocity into the icon's spring velocity (I6).",
        "8. Remove intent with separate enter and exit thresholds, shrink and fade, close the gap, show Undo (I10).",
        "9. Keyboard path and aria-live announcements (I12). Reduced motion (I11).",
        "10. Add the idle rest test and a 1500 ms watchdog (I5).",
        "11. Run check_implementation on the finished code and fix every FAIL. Then walk get_spec('test_scenarios') and confirm each expectation.",
    ]
    return "\n".join(steps)


def _has(code: str, pattern: str) -> bool:
    return re.search(pattern, code, re.I) is not None


@mcp.tool()
def check_implementation(code: str) -> str:
    """Static conformance check of an implementation (HTML/JS/TS source as text) against the spec.
    Returns PASS/WARN/FAIL lines with the fix for each. It catches omissions, not logic bugs, so still run the test scenarios."""
    checks = [
        ("FAIL", r"pointerdown", "Uses Pointer Events (mouse and touch in one path).", "Use pointerdown, pointermove, pointerup, pointercancel."),
        ("FAIL", r"pointercancel", "Handles pointercancel (I5).", "Cancel the drag on pointercancel so nothing stays lifted."),
        ("FAIL", r"['\"]blur['\"]", "Cancels on window blur (I5).", "addEventListener('blur', cancel)."),
        ("FAIL", r"Escape", "Esc cancels (I12).", "Handle Escape and return the icon to its original slot."),
        ("FAIL", r"ArrowLeft[\s\S]*ArrowRight|ArrowRight[\s\S]*ArrowLeft", "Keyboard move with arrows (I12).", "Space picks up, arrows move, Space drops."),
        ("FAIL", r"aria-live|aria-live|ariaLive|accessibilityAnnounce", "Announces steps to screen readers (I12).", "Add an aria-live=polite region and announce pick, move, drop, cancel, remove."),
        ("FAIL", r"prefers-reduced-motion", "Respects reduced motion (I11).", "Query it and swap in near-instant springs, no tilt."),
        ("FAIL", r"touch-action\s*:\s*none|touchAction", "touch-action none on icons.", "Without it, touch scrolling fires pointercancel mid-drag."),
        ("FAIL", r"requestAnimationFrame|CADisplayLink|withAnimation|\.spring\(", "Single physics loop or native spring.", "Drive motion from one rAF loop (web) or spring animations (native)."),
        ("WARN", r"setPointerCapture", "Captures the pointer.", "Call setPointerCapture inside try/catch so the drag survives leaving the icon."),
        ("WARN", r"0?\.62|hysteresis", "Slot-swap hysteresis (I7).", "Swap only after the centre passes about 0.62 of a slot."),
        ("WARN", r"0\.?008|\.008|substep|Math\.min\([^)]*0?\.033", "Spring substeps or dt clamp (I8).", "Clamp dt to 33 ms and integrate in 8 ms substeps."),
        ("WARN", r"undo", "Undo for removal (I10).", "Offer Undo for 4 s and Ctrl/Cmd+Z."),
        ("WARN", r"settl", "Tracks settling to decide when idle (I5).", "Return to idle only when springs are at rest."),
    ]
    out = []
    for level, pat, ok_msg, fix in checks:
        out.append(("PASS " + ok_msg) if _has(code, pat) else f"{level} Missing: {ok_msg} Fix: {fix}")
    if _has(code, r"-\s*\([^()]*\)\s*\*\*|-\s*[A-Za-z_]\w*\s*\*\*"):
        out.append("FAIL Unary minus before ** is a SyntaxError and blanks the page. Write -((x)*(x)).")
    else:
        out.append("PASS No unary minus before **.")
    if _has(code, r"transition\s*:[^;}]*transform"):
        out.append("WARN A CSS transition on transform exists. It is fine on static UI (toast), but must not be on any icon that JS also drives, or they fight.")
    else:
        out.append("PASS No CSS transform transition fighting JS.")
    fails = sum(1 for l in out if l.startswith("FAIL"))
    warns = sum(1 for l in out if l.startswith("WARN"))
    return "\n".join(out) + f"\n\nResult: {fails} FAIL, {warns} WARN. " + ("Ready for the scenario walk-through." if fails == 0 else "Fix the FAIL lines first.")


# ------------------------------------------------------------------ prompts
@mcp.prompt()
def build_dock_pick_drop(repo_url: str = "", framework: str = "vanilla") -> str:
    """Start here. Pass the repo link and target framework."""
    repo = repo_url or os.environ.get("DOCK_REPO_URL", "")
    src = f"Call load_from_repo with {repo} to read the reference implementation." if repo else "Read the dock://reference resource for the reference implementation."
    return (
        f"Build the dock pick-and-drop interaction in {framework} so it behaves exactly like the reference.\n\n"
        f"1. {src}\n"
        "2. Call get_spec('invariants') and get_spec('gotchas'). These are acceptance criteria, not suggestions.\n"
        f"3. Call get_build_plan('{framework}') and follow it in order.\n"
        "4. Keep the design minimal: the held icon is glued to the pointer, everything else is a spring, removal is shown by losing weight, never by red.\n"
        "5. Before replying, call check_implementation on your code and fix every FAIL.\n"
        "6. Walk get_spec('test_scenarios') and state, for each, whether your code satisfies it and how you know.\n"
        "Do not invent new tokens. If you must deviate, say which token and why."
    )


if __name__ == "__main__":
    mcp.run()
