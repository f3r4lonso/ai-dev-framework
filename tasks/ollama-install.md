# TASK PROMPT — Install Ollama and the Local Translation Model

Status: active

**Launch:** Start an AI coding client in the Workshop root and run this task. Follow workspace and `infra/` rules.
This task installs Ollama for the current Windows user and downloads one local model for the Spanish reading assistant.

## 1. Outcome

Install the official Windows Ollama runtime and `qwen3.5:4b-q4_K_M`, then verify the CLI, local API, model response,
GPU use and loopback-only network binding. Do not change application or infrastructure documentation; provider
registration is covered by [`ollama-local-model-runtime`](ollama-local-model-runtime.md).

## 2. Hard limits

- User-level installation only. Never install system-wide, elevate privileges, or modify unrelated applications.
- Use only the official Ollama Windows installer and the official Ollama model library. Verify the current version,
  download sizes, model tag and licenses from official sources immediately before presenting the install plan.
- Never use cloud-tagged models, `ollama signin`, Ollama web search, private prompts, or real user documents.
- Keep Ollama bound to loopback. Do not expose port 11434 to the network or set `OLLAMA_HOST` to a non-loopback
  address. Do not set persistent environment variables without separate approval.
- Never read `%USERPROFILE%\.ollama\` contents or credential files. Do not put model files, logs, or runtime
  configuration in a repository.
- Preserve all existing workspace changes. Do not commit or push.

## 3. Workflow

### Phase 0 — Check readiness (read-only)

1. Read `WORKSHOP-CONTEXT.md`, `infra/AGENTS.md`, `infra/SECURITY.md`, and this task.
2. Confirm Ollama is not already installed; if it is, report its version and stop before changing it.
3. Record Windows version, GPU and driver, available disk space, and names (not values) of any `OLLAMA_*` environment
   variables. `OLLAMA_HOST` may be checked only to confirm it is unset or loopback.
4. Confirm the current session can write to the current user's application install and model-storage locations. If
   permissions block that, stop and explain that this task must be run in a suitably authorized Windows session;
   do not work around the restriction by installing inside the repository or changing the sandbox.

### Phase 1 — Present the install plan (read-only)

Verify the official installer and model details, including licenses and any use restrictions. Present:

- Ollama version and official installer source;
- exact model tag, license, source and download size;
- required disk space with a reasonable buffer, compared with the observed free space;
- install scope, model storage location, context length (4,096 tokens), and expected startup behavior;
- verification steps and any limitations found for this GPU.

**Gate A — Install approval. Stop and wait for the user's explicit approval of this plan.**

### Phase 2 — Install and verify (only after Gate A)

1. Install the approved version for the current user and record `ollama --version`.
2. Pull only the approved model. Record its exact tag, size and digest from `ollama list`.
3. Use only generic test text. Check the model responds through both `ollama run` and the native `/api/chat` endpoint.
4. Check `ollama ps` for context and GPU/CPU split. Report the observed split; do not claim full GPU use unless the
   output confirms it.
5. Confirm the API listens on loopback only and `OLLAMA_HOST` is unset or loopback. If it listens on a public or
   wildcard interface, stop the service and report the failure; do not continue.
6. Report how to start, stop and uninstall Ollama, the installed version and model digest, test outcomes, and any
   limitations. Do not edit infrastructure docs in this task.

## 4. Acceptance

- The exact Gate A installer version and model tag are installed for the current user.
- CLI and local API respond to generic test text.
- Model tag, size, digest, context and GPU/CPU split are reported from observed output.
- The API is confirmed loopback-only, or the task stops with the service disabled and the issue reported.
- No private text, secrets, cloud model, account sign-in, persistent environment variable, repository configuration,
  commit or push was used.
