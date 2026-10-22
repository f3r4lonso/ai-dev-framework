# Free AI clients for creative media

Research checked 2026-10-21. Free plans change frequently; confirm the linked official plan and terms before using a quota or shipping an asset. “Free” means a free account allowance, not unlimited use. This inventory covers established, publicly accessible services with official evidence for free access to at least one of image, video, music, sound effects or voice. It is a practical shortlist, not a claim that every service worldwide is included.

## Best starting points

| Service | Free allowance verified | Best fit | Advantages | Limits and risks | Workshop setup |
|---|---|---|---|---|---|
| [Leonardo.Ai](https://intercom.help/leonardo-ai/en/articles/8942360-how-to-generate-images-with-leonardo-ai) | 150 daily tokens (web app help page) | Game concept art, image editing, image-to-video experiments | Daily refresh; image creation and editing in one interface | Tokens vary by operation; video usage can consume them quickly; API quota is separate; check visibility and content rights per plan | Web workflow only; see [setup guide](../clients/creative-media/README.md) |
| [Krea](https://www.krea.ai/pricing) | 100 units/day (pricing page) | Rapid image iteration, model comparison, video and 3D experiments | Broad collection of image/video tools; daily refresh | Unit cost depends on model and operation. Confirm current output rights and visibility in account terms; web units and API billing are separate | Web workflow only; its API is separately billed |
| [Recraft](https://www.recraft.ai/ai-image-generator) | Free entry point is advertised; no fixed quota confirmed on the public page | Game art, illustrations, vectors, mockups | Image, vector and editing tools | Confirm the allowance, output visibility, ownership and commercial rights in current plan terms before use | Web workflow only |
| [Adobe Firefly](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html) | Limited daily generations for free users, quota not stated as a fixed number | Images, vectors, video/audio experiments | Integrates with Adobe creative apps; daily free allowance; broad media feature set | Number/models/features can change; premium media has tighter limits; verify terms for game/commercial release | Web workflow only |
| [ElevenLabs](https://elevenlabs.io/pricing) | 10,000 shared credits/month; sound effects about 200 credits/generation, music about 900 credits/minute | Game SFX, ambience, voice lines, music sketches | One credit pool covers multiple products; official APIs and SDKs are available | Free plan does not include the paid commercial license. Check terms applicable to your location; credits are shared and the API key stays outside the repo | Web console or API; optional SDK setup in guide |
| [Stability AI Platform](https://platform.stability.ai/pricing) | 25 one-time API credits; 1 credit = $0.01; Stable Image Core 3 credits and Stable Audio 3.0 26 credits | Quick image/audio API prototypes | Official API and transparent per-generation credit pricing | One-time trial is small; a full Stable Audio generation costs more than initial grant; API use is not unlimited | API console and optional Python client; no Workshop integration yet |
| [Suno](https://help.suno.com/en/articles/9601601) | 50 daily credits | Full song and music mockups | Fast prompt-to-song workflow | Free tracks are for personal, non-commercial use. Download availability is separately limited and may depend on account history; do not assume a free track can be downloaded or used commercially | Human-operated web workflow; no Workshop connector |
| [Udio](https://help.udio.com/en/articles/10739134-credits-and-credit-limits) | 10 daily credits plus a 100-credit monthly allowance | Song drafts and extensions | Daily plus monthly credit pools; several editing actions | Current download/export and licensing behavior has changed following legal agreements; check the live product before relying on downloadable assets | Human-operated web workflow; no Workshop connector |
| [Runway](https://help.runwayml.com/hc/en-us/articles/50404627334547-Free-plan-details) | 125 one-time credits; not renewed | Video generation and editing | Purpose-built video tool; images/video available across tiers | Free plan has a limited model set and generated videos have a watermark; model access can change | Web workflow only |
| [Luma Dream Machine](https://lumalabs.ai/learning-hub/payments-subscriptions) | Free plan offers limited image and draft-video exploration; exact quota is account/plan dependent | Cinematic image-to-video and video drafts | Free path includes image and draft video; clear separation between web subscription and API credits | Free output has watermark and personal-use-only restriction; subscription credits do not transfer to API | Web workflow only |
| [PixVerse](https://app.pixverse.ai/subscribe) | Daily credits renew at 00:00 UTC; amount is shown in account and may vary by route/eligibility | Short video, image-to-video, generated audio | Daily refreshing allowance; supports multiple video creation modes | Credits expire daily; watermark, model access and commercial rights depend on tier; public pricing page does not state a universal free amount | Web workflow only |
| [Ideogram](https://ideogram.ai/pricing/) | Eligible free accounts get weekly credits; amount varies | Images with readable typography and design | Strong text-in-image workflow; slow generation queue after priority credits | Free generations are public by default; private generation is paid; credits vary | Web workflow only |
| [Meta AI / Vibes](https://ai.meta.com/vibes/) | Free image and video creation is advertised; no fixed token allowance published | Casual image creation and short video experiments | No public token accounting; integrated with Meta services | Allowance, export controls, commercial rights and regional availability are not stated as a fixed quota on the linked page | Web/app workflow only |
| [Pika](https://pika.art/pricing) | 0 credits/month on Free; pricing says packs only | Short video, image and audio experiments | Browser studio offers multiple media tools | No included monthly credits; pricing says Free has no commercial license. Confirm any credit pack and model terms before use | Web workflow only |

## Other categories and exclusions

- Google AI Studio / Gemini API offers free access for selected models, but the official pricing page must be checked by model. It is useful for multimodal analysis and prototyping; do not assume image/video generation models are free merely because general Gemini tokens are free. The free-tier data-use terms differ from paid-tier terms. [Pricing](https://ai.google.dev/gemini-api/docs/pricing) · [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits).
- Free access without a published token balance is included where useful (Meta AI/Vibes). Such services are not quota-equivalent to providers that publish a daily or monthly balance.
- Pika’s API Club is **not free**: the official announcement describes a $10 monthly membership and $10 introductory credit. Omitted from the free-quota shortlist, though potentially relevant if later evaluating paid consolidated APIs. [Official announcement](https://pika.art/blog/pika-api-club).
- Local open-weight workflows (for example, image/audio models run on the user's own hardware) do not grant hosted tokens and have hardware, setup, license and model-download requirements. They are a separate evaluation, not counted as free client quotas.
- Video product plans such as Kling, Hailuo and others may provide promotional or account-specific credits. This research does not state a quota where a current official page could not be confirmed reliably; check these live before choosing them.

## Recommendations by creative task

| Task | Start with | Why |
|---|---|---|
| Game concept art / sprites | Leonardo, Firefly, then Stability API trial | Daily web allowance versus controlled API prototype; validate style consistency and rights |
| Short video / trailers | Runway, Firefly; check Pika account quota first | Runway and Adobe disclose a limited free path; Pika's published numbers conflict |
| Game sound effects / ambience | ElevenLabs | Free monthly credits explicitly cover sound effects and music; non-commercial restriction applies |
| Music sketches | Suno or Udio | Daily/weekly creative credits; keep outputs as private prototypes until rights/export terms are checked |
| Workshop automation/API experiments | ElevenLabs or Stability AI | Official developer interfaces and explicit trial credits; credentials stay in user-level secret storage |

## Rights and privacy checklist

1. Check whether the free tier permits commercial use. For a game release, “personal use” is not enough.
2. Check if outputs are public by default (notably Ideogram free accounts) and avoid uploading private or unreleased game material unless the provider's terms allow it.
3. Save the generation date, model, plan, prompt, output provenance and applicable terms with assets intended for release.
4. Do not use a free account to evade limits with multiple accounts. Follow each service's terms.
5. Treat API trial credits as finite promotional balance, not recurring free inference. Set a spend cap where supported.
6. Never place API keys in this repository, prompts, command history, screenshots or game builds. See [infra security policy](../SECURITY.md).

## Sources and confidence

Quota and plan claims were checked against official product/help/pricing pages on 2026-10-21. Runway, Pika, Krea, ElevenLabs, Suno and Stability figures were rechecked against their current official pages for this revision. Exact generation counts may depend on account region, model, resolution, queue, feature and eligibility. Where a public page does not confirm a fixed allowance, this inventory says so rather than estimating. Re-check linked sources before spending money or committing an asset to production.
