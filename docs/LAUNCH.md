# docK launch kit

Prepared drafts, not posted. Use these only where relevant and allowed. Before posting, check the live demo and be available to discuss the work. Do not claim rankings, popularity, or compatibility that has not been demonstrated.

## Core message

**Try the dock. Give your AI the link.**

A draggable dock interaction with spring animation, reorder, remove and undo. The repo contains the motion specification and runnable reference so an AI coding assistant can adapt it to your project. Optional local MCP server. MIT licensed.

Demo: https://rishabharora-kk.github.io/docK/
Repo: https://github.com/rishabharora-kk/docK
Guide: https://rishabharora-kk.github.io/docK/guide/
Recording: `assets/demo.gif`
Sharing image: `assets/social-preview.png`

## Short post

> Try the dock. Give your AI the link.
>
> docK includes a draggable dock demo, spring/motion spec, runnable reference, and optional MCP server. Your coding assistant can adapt it to your stack.
>
> Reorder, remove, undo. MIT licensed.
>
> https://rishabharora-kk.github.io/docK/

Attach the real GIF. Add the repo link in the same post or a natural follow-up if the channel supports it.

## Technical community post

Title: **A draggable dock with a motion spec your AI assistant can use**

> docK is an interaction reference rather than a framework package. The held icon tracks the pointer directly; neighbours move on springs. It includes a landing slot, reorder hysteresis, deferred commits, upward removal, and undo.
>
> The repo puts the state transitions, motion values, invariants, and interaction scenarios alongside a self-contained HTML demo. Give the link to your coding assistant to adapt it to a project; no MCP setup is needed for that path. A local stdio MCP server also exposes build plans and heuristic checks.
>
> The current reference includes keyboard controls, focus handling, live announcements, and reduced motion. Very narrow touch targets remain a tradeoff to test in a production integration.
>
> Demo: https://rishabharora-kk.github.io/docK/
> Repo: https://github.com/rishabharora-kk/docK
>
> Feedback I'd find useful: where does the gesture feel ambiguous, and what context would your assistant need to reproduce it reliably?

## Show HN candidate

Only use this if the project meets the current Show HN guidelines and you can explain the work personally. A small demo or readme alone is not enough to assume eligibility.

Title: **Show HN: docK – a draggable dock with an AI-readable interaction spec**

URL: https://rishabharora-kk.github.io/docK/

Possible first comment:

> The interaction is a dock you can reorder, remove from, and undo. The implementation separates pointer tracking from spring animation: the held icon follows the hand, while neighbours make room.
>
> The part I want to explore is sharing UI behaviour with coding assistants. The repo includes motion tokens, a state machine, invariants, a working reference, and test scenarios instead of only a screenshot or vague animation prompt. It also has an optional MCP server; giving an assistant the files works without it.
>
> It is a vanilla JavaScript reference, not a set of prebuilt framework components. I'd be interested in reports from real adaptations, especially around touch precision and keyboard focus.
>
> Source and MIT license: https://github.com/rishabharora-kk/docK

## Release notes

Title: **docK v1.0.0 — Try the dock. Give your AI the link.**

- Self-contained draggable dock with spring animation, reorder, removal, and undo.
- Keyboard controls, focus continuity, live announcements, and reduced-motion behaviour.
- Motion specification, AI integration instructions, and optional Python MCP server.
- No-build live demo and statically readable integration guide.
- MIT licensed code and documentation.

Validation: Chromium checks for pointer and keyboard reorder, removal/undo, narrow-screen containment, reduced motion, and no runtime errors. Physical touch and screen-reader testing remain to be done. Framework build plans are guidance, not packaged integrations.
