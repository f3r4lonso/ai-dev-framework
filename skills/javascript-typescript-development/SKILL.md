---
name: javascript-typescript-development
description: Write, change or review general JavaScript or TypeScript code (browser, Node.js or tooling), including modules, async code, type safety, tsconfig settings and project build/test discovery. Use for language-level JS/TS work; React-specific guidance lives in the React skills and VS Code extensions in vscode-extension-development.
---

# JavaScript and TypeScript Development

Use this skill for language-level JavaScript or TypeScript work in any project. It covers the language, the module
system, the runtime boundary and the type system. It does not repeat React guidance (`vercel-react-best-practices`,
`react-state-management`) or VS Code API guidance (`vscode-extension-development`); load those as well when relevant.

## 1. Inspect the project before writing code

Read these before choosing syntax, APIs or commands; never assume the newest toolchain is in use:

- `package.json`: `type` (`module` or CommonJS), `engines`, `scripts`, dependencies and devDependencies.
- The lockfile present (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`) decides the package manager.
  Do not switch package managers or regenerate a lockfile with a different tool.
- `tsconfig.json` (and any `extends`): `target`, `module`, `moduleResolution`, `strict`, `lib`, `jsx`, `noEmit`,
  `paths`. If there is no `tsconfig.json`, the project is JavaScript: do not convert it to TypeScript unasked.
- Bundler or runtime config (`vite.config.*`, `webpack.config.*`, `esbuild`, Node version files) and the project's
  rules file. Use the project's `scripts` for build, lint and test rather than calling tools directly.

## 2. Language and runtime

- Keep language features separate from host APIs. `fetch`, `window`, `document` and `localStorage` are browser (or
  partly Node 18+) APIs; `fs`, `process` and `Buffer` are Node APIs. Check which runtime the file runs in.
- Use one module system per package, matching `type` and the existing files. Do not mix `require` and `import` in
  the same module. Respect file extensions the resolver needs (`.js` in Node ESM import paths).
- Use `const` by default, `let` when reassigned, never `var`. Use `===`. Prefer optional chaining (`?.`) and nullish
  coalescing (`??`) over `||` when `0`, `''` or `false` are valid values.
- Numbers are IEEE-754 doubles: never compute money or quantities that need exact decimals with plain floats without an
  explicit rounding rule; integers beyond `Number.MAX_SAFE_INTEGER` need `BigInt` or strings.
- Dates: `Date` is UTC internally but formats in local time. Store and compare timestamps as UTC epoch values or ISO
  strings with an explicit offset; convert to local time only for display.

## 3. Async code and errors

- Every promise is awaited, returned or explicitly handled; no floating promises. Use `Promise.all` for independent
  work and `Promise.allSettled` when partial failure is acceptable and must be reported.
- Network calls need a timeout and cancellation (`AbortController`); check `response.ok` before parsing.
- Throw `Error` objects (or subclasses), never strings. Catch only where you can handle or add context; do not swallow
  errors. Show the user a clear message and keep technical detail in the console or log.
- Avoid races in UI code: ignore stale responses when inputs change, and clean up timers, listeners and subscriptions.

## 4. TypeScript

- Keep or raise strictness; never lower `strict`, add `skipLibCheck` or widen types to silence an error without saying so.
- Prefer `unknown` over `any` for external data, and narrow it with type guards or runtime validation. Data from the
  network, storage or user input is untrusted until validated, whatever its declared type.
- Model states with discriminated unions instead of optional-field bags; use exhaustive `switch` with a `never` check.
- Prefer type inference for locals and explicit types for exported functions and public APIs. Use `satisfies` to check
  a value against a type without widening it. Avoid non-null assertions (`!`) and `as` casts unless justified in a comment.
- Generics, conditional and mapped types: use them when they remove real duplication; keep public types readable.

## 5. Security

- Never build HTML with string concatenation from data (`innerHTML`, `document.write`); use DOM APIs or the framework's
  escaping. Never use `eval`, `new Function` or string `setTimeout` with data.
- Never put secrets, API keys or tokens in front-end code or bundles: anything shipped to the browser is public.
- Do not build shell commands from strings in Node; use argument arrays (`execFile`, `spawn`) and validate paths.

## 6. Verification and reporting

- Run what the project already defines: type check (`tsc --noEmit` or the `typecheck` script), lint, tests, build.
  If the project has no tests or linter, say so; adding a test runner or linter is a new dependency and needs the
  project's dependency review and the user's approval first.
- Report each check you ran with its result, and each check you could not run and why.

## Official references

- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) and [TSConfig Reference](https://www.typescriptlang.org/tsconfig/)
- [Node.js documentation](https://nodejs.org/docs/latest/api/)
