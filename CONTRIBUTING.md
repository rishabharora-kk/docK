# Contributing to docK

Useful contributions preserve the dock's feel and make it easier to integrate. Reproducible interaction bugs, touch improvements, clearer assistant instructions, and verified framework examples are welcome.

## Run locally

Open `index.html` in a modern browser, or serve the repository with `python -m http.server 8000`. The demo has no build step. Python dependencies in `requirements.txt` are only for the optional MCP server.

## Report a bug

Include browser/version, operating system, input method (mouse, touch, keyboard, or assistive technology), steps, expected result, and actual result. A short recording helps. Check whether the issue occurs with reduced motion or at a narrow viewport.

## Propose a change

Read `IMPLEMENTATION.md`, `spec.json`, and `UX-REVIEW.md`. Explain the user problem and the tradeoff. Keep the core motion simple and avoid adding a dependency for a minor effect. If changing the runnable demo, keep `reference/index.html` in sync while preserving its absolute links.

For behaviour changes, walk the relevant scenarios in `spec.json` and report what you actually tested. Check keyboard focus after reordering/removal, cancellation, undo, a second pointer, and reduced motion. A static conformance check is not a browser test.

For SEO or content changes, keep claims factual. Describe framework plans as guidance until working components exist. Preserve canonical links and absolute social-image URLs. Avoid fabricated popularity claims or duplicate keyword pages.

## Share an integration

Open an issue with your stack, a public demo or recording, the source if available, and the scenarios you verified. This helps establish which adaptations work in practice.

Contributions are provided under the repository's MIT license.
