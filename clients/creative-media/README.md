# Creative media clients: Workshop setup

This guide covers the free image, video, music and sound-generation services in the [research inventory](../../docs/free-creative-ai-clients.md). Most are browser products, not command-line clients. Workshop infrastructure can document and launch a human-operated workflow, but it cannot install a provider's private web console or safely automate it without an official API and a separately reviewed integration.

## Quick start

1. Open the provider's official page from the research inventory and create/sign into your own account.
2. Check the current free-plan quota, region/model availability, export/download options, privacy, and commercial-use terms before generating release assets. Free allowances and rights change; use current provider terms rather than relying on a quota copied from this guide.
3. Keep the account in the provider's own credential manager. Do not add passwords, cookies, API keys or generated private media to `infra/`.
4. Record provider, model, date, plan, prompt and license/terms snapshot for any game asset that may ship.

## Optional API consoles

Only use an API when it is officially offered and the free quota is visible in the provider account. An API is not equivalent to a browser subscription and may have separate quotas and terms.

### Stability AI

1. Open the [Stability AI Platform](https://platform.stability.ai/) and create an account.
2. Review the current [API pricing](https://platform.stability.ai/pricing); the research check found 25 initial credits, with 1 credit equal to $0.01. This balance is not recurring.
3. Create an API key in the account dashboard. Store it in a user-level environment variable such as `STABILITY_API_KEY` or an approved secret manager. Never save it in this repo.
4. For Python experimentation, create an isolated virtual environment in the target project and install the current official SDK according to its official documentation. Do not install packages globally into Workshop infrastructure.
5. Check usage in the provider dashboard after each small test; Stable Audio 3.0 was listed at 26 credits per generation, so the initial grant does not cover that operation.

### ElevenLabs

1. Sign up at [ElevenLabs](https://elevenlabs.io/) and check the current shared free-credit balance and permitted use.
2. Create an API key only if an official API workflow is needed; store it in `ELEVENLABS_API_KEY` in your user environment or secret manager.
3. Follow the [official API documentation](https://elevenlabs.io/docs/overview/intro) for supported SDKs and authentication. Install an SDK in an isolated application environment, not as a global Workshop dependency.
4. The free allowance is shared among products. The pricing page does not include the paid commercial license on Free; check the terms applicable to your location and the output's usage rights before commercial use.

## What Workshop does and does not install

- Web services (Leonardo, Krea, Recraft, Firefly, Suno, Udio, Runway, Luma, PixVerse, Ideogram, Meta AI/Vibes, Pika) are opened in a browser and require no Workshop files or package installation.
- API services may be used by a future project integration, but this guide does not add an engine, API key, dependency or automated workflow to Workshop AI.
- Do not scrape browser sessions, automate account creation, bypass queues/quotas, or reuse subscription cookies as an API. Use only documented provider interfaces.
- For Workshop AI engine registration, first review the provider's API terms, data handling, authentication, quota behavior, costs, cancellation and error semantics. Then add a dedicated engine with explicit user approval and tests in the Workshop AI repository.

See [onboarding](../../docs/onboarding.md) for shared account and credential rules, [security](../../SECURITY.md) for prohibited files, and [creative client research](../../docs/free-creative-ai-clients.md) for current quotas and tradeoffs.
