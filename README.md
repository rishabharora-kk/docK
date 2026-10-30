# docK

**Like the dock? Give this repo link to your AI assistant.**

The interaction, motion spec, reference code, and optional MCP server are here so your assistant can build it into your project.

### [Try the interactive dock →](https://rishabharora-kk.github.io/docK/)

No install. No sign-in. Open and drag.

[![Animated preview of the docK interaction. Click to try the live dock.](preview.svg)](https://rishabharora-kk.github.io/docK/)

GitHub READMEs cannot run JavaScript. Click the preview to use the real interactive dock.

## Get it in your project

Copy this into your AI coding assistant:

```text
Add this dock interaction to my project: https://github.com/rishabharora-kk/docK
Read IMPLEMENTATION.md, spec.json, and index.html from the repo. Adapt it to
my stack and existing design, preserve pointer and keyboard behaviour,
and verify the interaction scenarios. Use my app's icons and actions.
```

Your assistant needs repository/file access. **No MCP setup is required:** the files carry the implementation instructions. If you prefer MCP, the [implementation guide](IMPLEMENTATION.md#optional-mcp-connection) explains how to connect the local server and use its build plans and checks. Sharing the link does not automatically connect MCP.

## Try these gestures

- **Reorder:** drag an icon sideways. The outline shows where it will land.
- **Remove:** drag above the dock and release. Use **Undo** or **Ctrl/Cmd+Z** to restore it.
- **Cancel:** press **Esc** to return the icon to its original position.
- **Keyboard:** Tab to an icon, Space or Enter to pick up, arrow keys to move, Space or Enter to drop. Delete removes a picked-up icon.
- **Inspect:** enable Slow motion, or expand the interaction design notes below the demo.

## Use it locally

Open [`index.html`](index.html) in a modern browser. No dependencies or build step. The demo runs entirely in your browser; it does not upload your interactions.

The animation uses direct pointer positioning for the held icon, spring physics for its neighbours, deferred order commits, separate removal thresholds, and reversible removal. Native buttons, live announcements, keyboard controls, and reduced-motion support provide alternative ways to use it.

## Source map

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | Self-contained interactive demo and implementation |
| [`IMPLEMENTATION.md`](IMPLEMENTATION.md) | Start here: integration guide for AI assistants |
| [`spec.json`](spec.json) | Original interaction specification from the design bundle |
| [`UX-REVIEW.md`](UX-REVIEW.md) | Design evaluation, improvements, and remaining validation |
| [`server.py`](server.py) | Optional MCP server for exploring the supplied specification |
| [`reference/index.html`](reference/index.html) | Bundled reference for the MCP server |

To run the optional MCP server: `python -m pip install -r requirements.txt`, then `python server.py`. It is separate from the browser demo.

## Hosting

Enable GitHub Pages once in [Settings → Pages](https://github.com/rishabharora-kk/docK/settings/pages): choose **Deploy from a branch**, **main**, **/ (root)**, then **Save**. Until Pages is enabled, the demo link above will not resolve. Once enabled, changes to `index.html` publish through GitHub's Pages build.
