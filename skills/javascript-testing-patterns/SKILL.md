---
name: javascript-testing-patterns
description: Plan, write or review automated tests for JavaScript/TypeScript code and React components (unit, component and integration tests, mocking network calls, fake timers). Use when adding front-end tests or when a JS/TS change needs test coverage.
---

# JavaScript Testing Patterns

Use this skill when JavaScript or TypeScript code needs tests, or when reviewing existing tests. Pair it with
`javascript-typescript-development` for language rules and the React skills for component design.

## 1. Find out what the project already has

- Look for a test script in `package.json`, a runner config (`vitest.config.*`, `jest.config.*`, `test` block in
  `vite.config.*`) and existing test files (`*.test.*`, `*.spec.*`, `__tests__/`). Follow their conventions.
- **No runner installed?** Do not install one silently. Propose the smallest fit and wait for approval through the
  project's dependency review: for a Vite project, Vitest (it reuses the Vite config); add `jsdom` and
  React Testing Library only if component tests are needed. Pure logic can often be tested first with Node's built-in
  `node:test` runner and no new dependency, if the code is importable outside the bundler.

## 2. What to test first

1. **Pure logic** (formatting, calculations, indicators, parsers, validators): fastest and most valuable. Extract it
   from components when needed so it can be tested without rendering.
2. **API client code**: request building, error and timeout handling, response parsing, with the network mocked.
3. **Components**: behaviour the user sees: what renders for loading, empty, error and success states, and what
   happens on clicks and input.
4. **Integration**: a few flows across several modules, kept small; full end-to-end browser tests are a separate,
   heavier decision (they need browsers installed).

## 3. Writing good tests

- One behaviour per test, named as a sentence (`it("shows an error when the price feed fails")`).
  Arrange, act, assert; no logic or loops that hide what is checked.
- Test behaviour, not implementation: query components by role, label or visible text, not by CSS class or internal
  state. Avoid snapshot tests for anything that changes often; they get approved without reading.
- Deterministic tests only: no real network, no real clock, no dependence on test order or on the machine's time zone.
  Use fake timers for intervals and debounce; set dates explicitly; seed or inject randomness.
- Mock at the boundary (the `fetch` call or the API module), not deep inside the code under test. Reset mocks between
  tests. Assert both the call made and the result shown.
- Cover edge cases that matter: empty lists, `null`/missing fields from the API, zero and negative numbers, very
  large numbers, rounding, slow and failed requests.
- Await asynchronous UI updates with the library's async queries (`findBy…`, `waitFor`) instead of arbitrary sleeps.
- Keep test data small and local to the test, or in a fixture builder; never use real account data or secrets.

## 4. Numbers and money

- Compare floats with a tolerance (`toBeCloseTo`) and test the rounding rule explicitly at boundaries.
- Test display formatting separately from calculation: a correct number shown with the wrong precision or sign is
  still a defect.

## 5. Verification and reporting

- Run the suite with the project's script; report the command, pass/fail counts and any skipped tests.
- A new test must fail when the behaviour it covers is broken. When fixing a bug, write the failing test first.
- If tests could not be run (no runner approved yet), say so plainly and list the tests that are ready to add.

## Official references

- [Vitest guide](https://vitest.dev/guide/)
- [Testing Library guiding principles](https://testing-library.com/docs/guiding-principles) and [queries](https://testing-library.com/docs/queries/about)
- [Node.js test runner](https://nodejs.org/api/test.html)
