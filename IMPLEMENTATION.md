# Add docK to an existing project

This guide describes the dock interaction. Apply it within the user's requested scope and the target project's conventions.

## Read these files

1. `spec.json`: states, transitions, motion tokens, invariants, known pitfalls, and test scenarios.
2. `index.html`: the runnable reference and current browser behaviour. Read the script and dock styles; the surrounding demo page is optional.
3. `UX-REVIEW.md`: known limitations and design tradeoffs.

If browsing a repository URL does not expose file contents, fetch the raw files from `https://raw.githubusercontent.com/rishabharora-kk/docK/main/` or clone the repository. A repo link does not automatically install an MCP server.

## Build in the target project

Inspect its stack and existing navigation first. Implement the interaction using its conventions. Reuse the user's own icons, labels, destinations, and styling. Preserve the dock behaviour without copying the demo's article, project navigation, or sample app actions unless requested.

- Keep motion values outside per-frame component render state. Use one animation loop and clean it up when unmounting.
- Keep the held icon under direct pointer control. Animate neighbours, scale, tilt, and shadow with springs.
- Preserve deferred order commits, landing-slot feedback, reorder hysteresis, and separate removal enter/exit thresholds.
- Track the active pointer ID. Cancel on Escape, pointercancel, and blur. Clear hold timers on reset and teardown.
- Convert screen coordinates into dock coordinates when the dock is scaled. Account for animated dock width.
- Provide native focusable controls and labels. Synchronise focus/reading order after a committed reorder, preserve focus, and move it after removal.
- Provide keyboard pick-up, move, drop, cancel, remove, and undo with live announcements.
- Respect reduced motion. Keep undo available and avoid introducing accidental destructive app actions.
- Fit the available viewport. On narrow screens, choose an overflow strategy or fewer pinned items if scaling makes touch targets too small.

The specification is design intent; the reference is executable evidence. Where they differ, identify the difference and make the implementation choice explicit. For example, the reference snaps reduced-motion springs and offers keyboard undo beyond the four-second toast. The spec requests a 1500 ms watchdog, but the current reference relies on its spring rest test. Implement and verify the watchdog rather than assuming it exists.

## Verify before handing over

Run the target project's relevant checks and the scenarios in `spec.json`: tap, reorder, boundary jitter, remove/undo, cancel, pointercancel, second-pointer isolation, regrab during settling, keyboard operation, reduced motion, and one-icon behaviour. Also test narrow-screen coordinates, focus continuity, and component teardown.

Report which checks actually ran and which remain unverified. A static pattern check does not prove interactive behaviour or accessibility.

## Optional MCP connection

The default path is reading the files above. An assistant with repository access needs no MCP setup.

For an MCP-capable client, clone this repo, install `requirements.txt` in a Python environment, and configure a local stdio server using that environment's Python executable and an absolute path to `server.py`. Adapt this common configuration shape to your client's settings:

```json
{
  "mcpServers": {
    "dock": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/docK/server.py"],
      "env": {"DOCK_REPO_URL": "https://github.com/rishabharora-kk/docK"}
    }
  }
}
```

Available resources: `dock://spec`, `dock://reference`.

Available tools: `get_spec`, `load_from_repo`, `get_build_plan`, `check_implementation`.

Start with the `build_dock_pick_drop` prompt and your framework, or read the resources and call `get_build_plan` directly. Framework notes cover vanilla JS, React, Vue, Svelte, and SwiftUI; these are implementation guidance, not packaged components. `check_implementation` uses source-text patterns geared toward web code, so native implementations can produce false failures. Always validate actual behaviour.
