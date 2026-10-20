# Game interface review

Workshop additions, 2026-10-19. Use as proposed acceptance cases during planning; record actual observations only
when an authorized implementation and device test exist.

| Area | Review case and expected outcome |
|---|---|
| Touch | Map selection, zoom, drag and end-turn gestures cannot trigger conflicting actions; critical actions have recovery or confirmation appropriate to their consequence. |
| Insets | Recalculate after orientation/window changes; convert OS display coordinates into the actual viewport/canvas space, including scale and origin. Important controls stay reachable. |
| Overlays | Block both UI and world input underneath modals, including pointer events and shortcuts; restore previous valid focus and input state on dismissal. |
| Interruption | App backgrounding, dialogs and screen changes preserve the intended turn and selection; resuming cannot repeat a purchase or end-turn action. |
| Readability | Unit/state information remains distinguishable without color alone; offer suitable text scaling and motion options. |
| Localization | Exercise long strings, number formats and right-to-left layouts where supported; labels remain readable and controls reachable. |
| Assistive input | Record which native/engine accessibility features actually work, their limitations, and available alternatives. Do not infer screen-reader support from visual contrast. |
| Device coverage | Choose representative small/large screens, densities, aspect ratios and supported inputs; avoid declaring keyboard/gamepad support without a product need. |

Use official Android and chosen-engine guidance to set touch dimensions and safe-area APIs. Never treat web CSS,
ARIA or a sample engine snippet as proof of native-game accessibility. Keep testing status separate from the spec.
