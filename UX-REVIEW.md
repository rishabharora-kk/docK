# docK interaction review

This is an expert heuristic review of the supplied prototype, not a usability study. Claims about user preference, speed, or comprehension require observed sessions with users.

## Assessment

The strongest choice is keeping the held object under direct pointer control while allowing neighbours to spring into position. This preserves agency and object continuity. A visible landing slot externalises the pending result; deferred commits make cancellation predictable. Distinct enter/exit thresholds reduce removal flicker. Undo makes an exploratory gesture recoverable.

The main adoption issue was presentation: a visitor had to read detailed mechanics before discovering the demo's value. The README contained placeholder URLs, and the technical exposition competed with the interactive stage. Six fixed-size icons also exceeded narrow phone widths. Keyboard operability existed, but DOM order did not track visual order after a move. A second pointer could move or release the first pointer's selection.

## Changes

- Put a live-demo link and linked preview at the top of the README. GitHub sanitises scripts and embedded interactive frames; one click to Pages is the practical path.
- Keep the original colour palette, typography, iconography, and core motion. Move technical notes into a disclosure below the demo.
- Fit the dock to the stage on narrow viewports and convert pointer coordinates into the scaled coordinate space.
- Use native buttons, preserve visible focus, synchronise DOM order after committed changes, and move focus away from removed items.
- Filter active gestures by pointer ID; clear pending holds on reset; block undo during a gesture.
- Snap spring values when reduced motion is requested, remove the tap hop in that mode, and disable CSS transitions.
- Add a light/dark switch and retain system-theme defaults.

## Tradeoffs and next validation

Mobile scaling keeps the whole dock visible but reduces targets below the preferred 44 CSS pixels at the narrowest widths. A production dock could use fewer pinned items or an overflow menu. Test this with touch users before claiming mobile optimisation.

Dragging upward to remove is initially hidden. The page explains it and shows a release label; test whether people discover it without coaching. A labelled Remove action could improve access for users who struggle with precision gestures.

Tapping produces motion feedback only: this is an interaction demo, not an application launcher. The sample app names are illustrative.

The original specification remains as design input. Its numerical tokens and guarantees are not all automated conformance claims. In particular, test magnification near adjacent targets, high-speed dragging, screen readers, background-tab recovery, and sustained use on physical touch devices. The reduced-motion preference is read at page load; reload after changing it.

## Suggested usability session

Ask participants to reorder Notes, remove Search, restore it, and cancel a move. Observe first-action latency, accidental removals, successful recovery, and whether the landing marker predicts the result. Repeat using keyboard only and a touch phone. Compare against the original without claiming statistical significance from a small sample.
