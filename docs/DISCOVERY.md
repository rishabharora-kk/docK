# docK discovery audit and launch plan

Researched 30 October 2026. Scope: live home page and its head markup, GitHub repository metadata, project files, a focused web search, and selected primary guidance. This is not a measurement of search volume, backlinks, rankings, Core Web Vitals, or Google's indexing state.

## What we found and changed

| Priority | Evidence before changes | Change | Verification |
| --- | --- | --- | --- |
| High | GitHub API returned null description, null homepage, no topics, and no detected license. | Added owner-approved MIT license. Prepared About copy and targeted topics below; API writes to settings returned 403. | Confirm license detection and paste About settings in GitHub. |
| High | Home returned HTTP 200, but the title described a gesture without identifying the product category or AI handoff. | Descriptive title, visible category text, and a clear AI-handoff headline; README describes capabilities and limits. | Inspect live title, heading, and source after Pages deploys. |
| High | No canonical, Open Graph, Twitter card, or JSON-LD in the inspected home head. | Added canonical URL, absolute PNG social image, sharing metadata, and SoftwareSourceCode JSON-LD matching the visible product. | Inspect rendered and raw HTML; confirm image returns 200. Structured data does not guarantee enhanced search appearance. |
| Medium | The reference copy is also published at `/reference/index.html`. | Its canonical points to the main demo. | Inspect canonical on both URLs. Canonical selection remains up to search engines. |
| Medium | Detailed instructions were primarily Markdown files on GitHub. | Added a statically readable `/guide/` page with file links, framework limits, MCP setup, and verification steps. Linked it from the home page. | Navigate without JavaScript and check internal links. |
| Medium | No site URL inventory or explicit assistant reading index in the repo. | Added sitemap.xml with the two useful HTML pages, plus llms.txt as a voluntary file index. | Validate XML and fetch file links. llms.txt is not an SEO ranking factor or guaranteed assistant ingestion mechanism. |
| Medium | Existing preview was an illustrative SVG animation. | Added a GIF recorded from the actual demo and a 1280×640 PNG card. | Open the GIF and verify the social image is under GitHub's 1 MB limit. |
| Medium | No contribution guide or structured integration reports. | Added focused contribution instructions and bug/integration issue templates. | Check links and templates on GitHub. These lower contribution friction; they are not ranking guarantees. |

## Positioning and search intent

A focused web search for `macOS dock component AI MCP draggable dock animation` surfaced React/macOS-style dock pages from Cult UI, shadcn.io and 21st.dev, and a Web Components dock repository. This is qualitative language research, not a competitive ranking or market-share report.

Cult UI explicitly describes a React dock with magnification and Motion springs. docK's useful emphasis is the reproducible interaction: drag-to-reorder, remove/undo, motion values, state transitions, verification scenarios, and an optional MCP server. Describe those accurately rather than claiming superiority or implying that framework packages exist.

| Intent | Phrase to answer naturally | Destination |
| --- | --- | --- |
| Try a UI interaction | draggable dock animation; spring animated dock | Home and actual GIF |
| Reproduce with an assistant | dock for AI coding assistants; AI-ready interaction spec | README and guide |
| Understand behaviour | drag-to-reorder dock; removal with undo; keyboard dock controls | Demo, spec, UX review |
| Configure tooling | dock MCP server; Model Context Protocol UI reference | Guide's optional MCP section |
| Adapt a framework | implement dock in React / Vue / Svelte / SwiftUI | Guide and build-plan notes, explicitly described as guidance |

## GitHub settings to paste

The integration could commit code, but GitHub returned HTTP 403 for both repository metadata and topic updates. These are ready for the owner to apply in the repo's **About → gear**:

**Description**

```text
A draggable dock your AI assistant can build. Spring animation, reorder, remove + undo. Live demo, motion spec, reference code & optional MCP server. MIT.
```

**Website**

```text
https://rishabharora-kk.github.io/docK/
```

**Topics**

```text
dock, drag-and-drop, spring-animation, javascript, vanilla-javascript,
microinteractions, ui-animation, interaction-design, accessibility,
ai-coding, model-context-protocol, mcp-server
```

**Social preview**: in repository Settings, upload `assets/social-preview.png`. The demo site's Open Graph image is set by HTML; GitHub's repository preview is a separate setting. Download the file from the repo if needed.

## Distribution that can earn real usage

Use the real demo GIF and a single proposition: **Try the dock. Give your AI the link.** Lead with something people can use immediately. Link directly to the no-sign-in demo and include the repo for the handoff.

1. Share one useful demonstration on a channel where you already participate. Explain a specific detail such as deferred commits or pointer tracking; invite testing and reports, not coordinated stars.
2. Ask developers to adapt it to a real app and share what broke. A verified integration is stronger evidence than unsupported framework claims. Use the integration issue template.
3. Consider Show HN only if you can personally discuss the implementation, tradeoffs, and iteration. Its guidelines require something substantive people can try, and prohibit asking friends to upvote. A generic AI-generated demo alone is unlikely to meet that bar. A launch draft is in LAUNCH.md; nothing has been submitted.
4. Share tailored posts in relevant frontend, interaction-design, and AI-coding communities only where their rules allow self-promotion. Do not copy-paste across communities or open promotional issues in unrelated repos.
5. Submit to a curated list or MCP directory only after checking its current inclusion criteria, licensing expectations, and whether a local stdio tool fits. This audit did not verify directory eligibility or submit listings.
6. Publish a practical follow-up: a real framework integration or a comparison of pointer-driven versus spring-driven dragging, backed by a recording and source.

## Measurement and next steps

At audit time the GitHub API reported 0 stars and 0 forks. These are a baseline, not a traction forecast. No analytics tracker has been added.

- After deployment, verify the live page, guide, GIF, PNG, sitemap, license, and raw implementation links.
- Set up a Google Search Console URL-prefix property for `https://rishabharora-kk.github.io/docK/` using the owner's Google account. Verification requires an account-specific token/file; none is fabricated or embedded here. Then submit `/docK/sitemap.xml` and inspect the home and guide URLs. This remains an owner action.
- A `robots.txt` file under `/docK/` would not control this GitHub Pages host: crawlers look for `/robots.txt` at the origin root. This project does not control that root, so no misleading project-level robots file was added.
- Once per week, record repo traffic/referrers from GitHub Insights if available, demo click-through evidence if available, stars/forks, and useful integration reports. GitHub traffic has a limited lookback, so save dated observations. Search Console can provide actual query and impression evidence after verification.
- Evaluate search trends over weeks, and product improvements through observed use. Do not infer failure from an empty `site:` query alone or claim rankings from one search response.

GitHub Trending is separate from Google Search. Neither the official sources consulted nor this audit establish a formula that can be reliably controlled. The aim is a discoverable, usable project worth recommending.

## Sources

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): descriptive titles, useful original content, links, discovery, and the absence of first-place guarantees.
- [Google introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data): markup provides context; eligible display is not guaranteed.
- [GitHub repository topics](https://docs.github.com/articles/classifying-your-repository-with-topics): relevant topics help people discover projects.
- [GitHub social previews](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview): image settings, under 1 MB, 1280×640 recommended.
- [GitHub licensing guidance](https://docs.github.com/articles/licensing-a-repository): a public repo without a license does not grant general reuse rights.
- [Cult UI dock](https://www.cult-ui.com/docs/components/dock): observed example of React/macOS dock positioning.
- [Show HN guidelines](https://news.ycombinator.com/showhn.html): tryability, substance, author participation, and no vote solicitation.
