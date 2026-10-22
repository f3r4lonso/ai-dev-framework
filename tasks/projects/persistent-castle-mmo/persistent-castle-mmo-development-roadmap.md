# Persistent castle strategy MMO — development roadmap

Status: provisional roadmap for planning the original mobile MMO. Replaces the 2026-10-19 solo/offline Godot
proposal, which no longer reflects the owner's direction. No engine, backend, repository, vendor or cloud service
has been selected or approved. No implementation work has started.

The current product requirements and design status are in the [design brief](persistent-castle-mmo-design-brief.md).
Run the [planning task](persistent-castle-mmo-planning.md) before authorizing development.

## Roadmap

| Phase | Goal | Deliverable and exit evidence | Approval boundary |
|---|---|---|---|
| 0. Design and planning | Resolve player loop and propose original systems | Reviewed design package, worked mission and two-stage raid, audiovisual briefs, decision register | Owner approves scope, unresolved defaults and commercial boundaries |
| 1. Online architecture decision | Compare client/server, engine, identity, persistence, commerce and service operations | Cited technology comparison and architecture decision record; threat/data-flow review; operational ownership/cost drivers | Owner approves platform, architecture, budget envelope and operator |
| 2. Project preparation | Establish a repository, toolchain, content conventions, environments and build/test workflow | Approved project setup; reproducible local build; dependency/license inventory; security and recovery plan | Explicit approval before repo initialization, installs, accounts, cloud or paid services |
| 3. Vertical slice | Implement one mission and representative battle plus a fixed-location castle raid in a controlled test environment | Device-tested touch flow; authoritative resolution; interruption/retry behavior; economy fixture; moderated play sessions | Owner reviews experience, risks, measured service use and whether to continue |
| 4. Closed MVP | Add bounded roster/progression, shops, item fusion, forge/evolution and safeguarded social functions | Acceptance matrix, abuse/security review, recovery and moderation procedures, measured device/service budgets | Separate approval for external testing and real-money features |
| 5. Release readiness | Prepare distribution, support and operations | Current store/policy checks, privacy disclosures, account support, incident/rollback plan, asset provenance and signed build process | Separate explicit approval to publish and operate |
| 6. Events and expansion | Add events, minigames, broad content, seasons or expanded commerce only with evidence | One scoped feature proposal with economy/ops impact and player evidence | Separate approval for each expansion |

## Planning constraints

- MMO persistence, player trades and castle attacks require authoritative server rules, identity, abuse prevention,
  recovery and ongoing operations; an offline-first architecture assumption is obsolete.
- The two-stage raid, PvP-only currency, forge, creature evolution, trading and rewarded-video proposals have
  material economy, security and player-protection implications. Their rules must be designed before they are built.
- Start with a representative vertical slice. Do not begin with all races, ten forge levels, five evolution stages,
  a global live world, events, minigames or monetization systems at once.
- Research current engine, backend, billing, advertising and store requirements from official sources at the phase
  where a decision is made. Prior research for the solo prototype does not constitute MMO validation.
- No cost, scale, performance, legal, accessibility or balance outcome is established in this roadmap.
