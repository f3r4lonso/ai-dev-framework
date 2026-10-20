# Persistent castle strategy MMO — design brief

Status: provisional design brief based on the product owner's direction, 2026-10-20. This is an original game
proposal inspired by the broad strategy genre; it is not a Heroes III clone. Rules, balance, title and art direction
remain subject to product review. No implementation or playtest has occurred.

## 1. Player promise and confirmed direction

The player builds a growing roster of heroes and creature forces, explores missions for rewards, develops a
permanent stronghold, and challenges other players for a scarce competitive currency. The strategic appeal is
long-term collection and preparation followed by readable tactical decisions with meaningful risk.

Confirmed by the product owner:

- Mobile game with persistent multiplayer / MMO ambitions; castles occupy stable world locations.
- Players acquire creatures, items, spells and other rewards through missions and in-game shops. More than one
  creature race and hero type is collectible and playable.
- A player may station a hero outside their castle a few map squares away to guard its entrance. Defeating that
  defender opens a second battle against the hero inside the castle.
- The game includes a spellbook for hero spells and creature dungeons/dwellings. The exact meaning and function of
  “dungeons” is open: possible interpretations include recruitment dwellings, creature missions or another
  owned-creature system. The design phase must resolve it instead of silently assuming one.
- Defeating heroes and castles awards a special currency unavailable through ordinary resource play.
- Players may trade artifacts and creatures and teach spells to one another.
- Three matching items can be combined to improve an item. Forge progression has up to ten levels, followed by
  refinement. Creatures can evolve up to five times.
- A premium currency (working examples: diamonds or stars) can be purchased. It is separate from gameplay resources.
- The product has no routine advertising. Rewarded video may be considered for exceptional optional benefits:
  returning a defeated hero to their castle without losses, or optional item chests, creature chests, missions or
  stars/premium currency. These are candidate benefits only, subject to free alternatives, caps, economy review and
  platform/legal review.
- The game should support later time-limited events, minigames and mobile-style event dashboards.

Not yet decided: iOS support and release order; audience/age rating; real-time versus asynchronous combat; exact
combat rules; open-world travel and map scale; castle assault timing and defender rules; protection from repeated
raids; currency naming and sinks; trade restrictions and fraud recovery; whether ads or purchases affect
competitive power; paid item randomness; rewarded-video rewards/caps/free alternatives; spellbook learning and
spell-teaching rules; creature dungeon/dwelling purpose; event cadence; launch content caps; team, budget and server
operation. These are product decisions, not facts to invent in implementation.

## 2. Original concept proposal

Working concept: **The Shattered Marches** (placeholder). A chain of contested frontier territories is anchored
by player strongholds. Each commander develops a personal warband from distinct original lineages and sends
heroes on short expeditions. Missions are the dependable free progression path; world challenges and castle
raids are the risky route to the exclusive prestige currency. The theme, title, factions, visual identity, names,
maps, lore and content must be original and receive an IP review before production.

Creative pillars:

1. **Prepare, then commit:** choose a hero, formation, spells and equipment for a known objective; scouting should
   reveal useful facts without guaranteeing the outcome.
2. **A living frontier:** castle positions persist and player activity changes territorial pressure, but losing a
   defense should not erase weeks of collection.
3. **Collection with choices:** races, heroes and creature evolutions create distinct tactical options; upgrades
   should widen choices more than simply make old content obsolete.
4. **Social exchange with safeguards:** trade and spell teaching support cooperation, with clear consent, limits,
   provenance and recovery rules.
5. **Fair optional spending:** paid currency and rewarded ads are visibly optional, with a free progression path
   and no deceptive or loss-triggered pressure.

## 3. Proposed player loop

1. Collect mission rewards and daily free provisions; inspect new items, creatures and spell knowledge.
2. Choose a hero and mission, or prepare a raid squad from owned units.
3. Set formation, equipment, learned spells and creature abilities; review known risks and likely rewards.
4. Resolve a mission or challenge using the eventual battle mode. The initial design should favor short, turn-based
   encounters that work well with touch input; synchronous/asynchronous rules remain open.
5. Spend earned resources on recruitment, shops, training, forge work or creature evolution. Compare the result
   before confirming irreversible upgrade costs.
6. Visit the persistent world, scout a target, then raid a guard hero and (if victorious) the castle's inner hero.
7. Receive the special challenge currency only from eligible PvP hero/castle victories; use it in a dedicated shop
   with its own balance and anti-farming rules.
8. Stop at a clear session boundary; missions remain the fallback activity if the player does not want PvP.

The return motivation is roster mastery, discovering mission/story content, coordinating trades and choosing when
to risk a prepared team in the frontier. This is a design hypothesis, not validated engagement evidence.

### Worked examples (illustrative proposals, not canon)

- **Mission, “Salt Road Signal”:** choose a scout hero, three creature groups and two prepared spells. Recon shows a
  ranged raider and hazardous ground. A fast flank may win sooner, while a larger slow force is safer but costs
  more recovery resources. The player can spend a spell to interrupt the raider or save it for a second hazard
  wave. A win grants ordinary resources plus a creature recruit token and possible item; a loss has a clear free
  recovery path. If “creature dungeon” means a recruitment structure, the mission could instead unlock its stock;
  that connection is a decision to resolve.
- **Two-stage raid:** scout a fixed-coordinate castle; review the exterior guard and inner hero under defined
  visibility rules, known risks, possible losses and the unresolved carry-over policy before confirming. Defeating
  the exterior guard opens the inner battle; losing it ends the assault. Decide whether surviving stacks carry
  casualties/spell use into stage two or receive a limited reset, and show that rule before commitment. Only an
  eligible victory awards PvP-only currency, subject to repeat-target and collusion checks. These battle rules are
  illustrative and require owner decisions and playtesting.

### Spellbook and creature dungeon options

- **Spellbook option A (proposed default):** each hero learns spells into a personal library and prepares a small
  loadout before each mission/raid. This makes scouting and preparation meaningful. Spell teaching could grant a
  permanent lesson, temporary access or transfer a spell-bearing item; choose only after economy and abuse review.
- **Spellbook option B:** a shared account codex with each hero limited by school/slots. This emphasizes collection
  over hero-specific knowledge but may blur hero identities.
- **Creature dungeon/dwelling option A:** owned race-specific habitats unlock or replenish recruitable creatures.
- **Option B:** instanced PvE dungeon missions award recruit tokens, eggs, shards or creatures.
- **Option C:** habitats provide the roster interface and dungeon missions are an active acquisition route. This
  combines both but adds content and service scope. Ask the owner which meaning matches their intent.

## 4. System contracts and unresolved rules

### World, castles and raids

- Stable castle coordinates are a confirmed requirement. Define map partitions, travel cost, scouting visibility,
  online/offline defender behavior and how a castle may be relocated (if ever) before implementation.
- A raid has two ordered stages: outside guard hero, then inside castle hero. The second stage must not start unless
  the attacker wins the first. Specify whether surviving units, spells, consumables, wounds and battle losses carry
  between stages; show the outcome before the attack is confirmed.
- Define defense windows, shields/cooldowns, matchmaking and repeat-target limits so a player cannot be farmed while
  offline. Keep new or inactive players protected without making the special currency trivially farmable.
- The special currency is awarded only for eligible victories over player-controlled heroes/castles. Define
  diminishing returns, attacker/defender eligibility, season resets and fraud detection. Never award it for self-
  arranged trades or repeat collusion.

### Combat and roster

- Combat format is open. Candidate for evaluation: asynchronous, server-resolved, turn-based battles with a replay
  log and clear pre-battle information. This supports persistent online play without requiring both players online,
  but can reduce defender agency; test this trade-off before locking it.
- Heroes lead creature stacks; hero type, skills, equipment and spells modify tactical options. Spell teaching is a
  consent-based transfer or lesson with explicit cost, eligibility and duplicate-learning feedback (rules open).
- Creature races, roles, counters, morale, speed, range, terrain, abilities and casualty recovery need a bounded
  first-release ruleset. No faction roster is canon yet.
- Evolution has at most five stages per creature line. Each stage needs a preview of stat/ability changes, costs,
  prerequisites and whether the prior form remains selectable. Avoid permanently invalidating a rare creature.

### Items, forge and economy

- Three identical items combine into one improved item. Define “identical” by stable item ID and upgrade state;
  explain what happens to enhancement/refinement investments in the inputs.
- Forge levels are capped at 10 before refinement. Define success certainty, materials, caps, costs and visible
  stat outcomes. Avoid hidden breakage or paid random failure. Refinement is a separate tier and should not be
  conflated with forge level.
- Separate soft resources, the PvP-only currency and purchasable premium currency in names, wallets, UI, earning
  sources and spend sinks. No conversion between them is approved.
- Shops should state stock, refresh, eligibility, price and free alternatives. Mission rewards must remain a viable
  progression path. Balance and drop rates need simulation and player testing; no values are set here.

### Trading and social systems

- Trades require both players to review the final offer and confirm after any change. Lock the offer during final
  confirmation; log transfers and provide a support/reversal policy for exploit or account compromise.
- Bind or cooldown select items/creatures if required to prevent wash trading and PvP-currency farming. Do not add
  a player-to-player market until fraud, moderation, economy and jurisdiction needs are assessed.
- Spell teaching should disclose exactly what each participant gives and receives, and avoid a hidden paywall for
  core combat knowledge.

### Monetization and rewarded ads

- Do not show routine/interstitial advertising. Ads are explicit opt-in reward actions with the reward, limits,
  eligibility and alternative stated before the player chooses; closing or declining has no penalty.
- Hero-death recovery by ad is only a candidate proposal. It must not appear as a pressure prompt during grief or
  obscure the free recovery path. Define a non-ad recovery option, daily cap, what “without losses” restores and
  whether it changes PvP defense state. No resurrection promise is final until reviewed.
- Daily reward ads should be in an optional rewards area, never required to claim the free daily reward. Do not
  promise premium currency through ads until economy and platform rules are reviewed.
- Purchasable premium currency must be clearly distinguished from earned resources. No prices, bundles, loot-box
  probabilities, purchase bonuses or pay-to-win advantages are approved. Store billing, refunds, parental controls,
  age/audience and ad-data practices require current platform and qualified legal review before implementation.
- Evaluate all requested rewarded-video candidates without treating any as approved placement: optional item
  chests, creature chests, extra missions and stars/premium currency, as well as hero recovery. Each needs a free
  equivalent, transparent limit, no penalty for declining and an economy/platform review. Premium-currency rewards
  from ads remain undecided.

## 5. Events and minigames

Design the client and service boundaries so later events can be configured without a client update where practical,
but do not build a generalized event platform in the first playable slice. Future event definitions need start/end
time, eligibility, rules, reward table, localization, time-zone display, claim state and failure behavior. Dashboards
must not imply urgency with deceptive timers. Minigames must have distinct entry/exit behavior, session length and
reward budget so they do not become an unbounded economy exploit.

## 6. Illustrative encounter

An attacker scouts a fixed-location castle and sees that a guard hero protects its gate. The attacker compares two
prepared squads: a stronger force with slow movement and a spell-focused force with fewer troops. They choose the
spell-focused team because the visible guard lineup suggests a weakness, then review the two-stage warning and
possible losses. On winning, the surviving force proceeds to the inner hero under the confirmed carry-over rules;
those rules must be chosen before this example can become an implementation acceptance case. A victory grants the
exclusive PvP currency only if eligibility checks pass. A loss offers a clear free recovery route; an optional ad
reward, if approved, is never the only way to recover.

## 7. Provisional content and production sample

Create a vertical slice with one original race, two hero archetypes, a compact creature roster, a small set of
spells/items, several missions, a player castle and one PvP raid path. Exact counts are for the detailed-design
phase to propose and the owner to approve. Include one item fusion, one forge progression example and one creature
evolution line to prove the rules are understandable. Defer full trading, all ten forge tiers, all five evolution
stages, a large world, live events, minigames, guilds, ranked seasons and broad monetization until the core loop is
playable and the online threat/economy model is reviewed.

## 8. Original audiovisual direction — provisional creative pass

All work must create an original visual/audio identity, not reproduce Heroes III artwork, factions, interface,
iconography, maps, character silhouettes or music. Working direction: **weathered frontier fantasy**—hand-built
materials, bold readable silhouettes, restrained ornament, warm settlement lights against cool open terrain, and
distinct faction shapes/markings alongside color (never color alone). Surface detail must not obscure game state.
A top-down/three-quarter strategic view may keep castle layout and squads legible on phones; rendering and battle
camera remain open.

### First-slice graphic assets

Prioritize a compact, original production sample:

1. Battle readability: a small creature sprite/model set, two hero archetypes, selection/target states, health or
   status indicators and one representative battlefield.
2. World/castle: one fixed player castle, exterior guard position, inner battle context, compact terrain set, map
   markers and ownership/raid eligibility states.
3. Core UI: original icons for resources/currencies, heroes, creatures, spells and items; panels for roster, mission
   preparation, battle results, forge preview and rewards.
4. Progression feedback: one item fusion, forge preview/confirmation, creature evolution and reward sequence.
5. Combat effects: limited spell VFX, hit/defense feedback, defeat/victory, and clear outer-guard-to-inner-castle
   transition.
6. Social placeholders: trade and spell-teaching confirmation states; event dashboard/minigame art can wait for
   approved event scope.

“Sprays” is ambiguous; it may mean sprites (2D character/creature/effect images, often arranged in animated sprite
sheets), particle effects or decorative decals. Confirm the intended asset type before production. Do not lock 2D/3D
rendering from this direction alone.

Sound priorities: clear, short feedback for selection, movement, reward, forge preview/confirm, evolution, trade
confirmation, raid warning, battle turn, damage, victory/defeat and optional reward claim. Keep critical state
available visually and through haptics where appropriate so muted play remains understandable. Avoid notification
sounds that imitate system alerts or pressure a return.

Representative sound-effect families to develop: UI select/confirm/invalid; map move/scout reveal; recruitment and
evolution; spellbook open/learn and spell cast; forge/fusion/refinement; trade offer/lock/confirmation; castle
warning; outer-guard and inner-castle battle starts/turns/results; prestige-currency award; recovery choice/result;
reward claim; event entry/exit. Reuse families rather than creating a unique sound for every creature or item.

### Music states and transition intentions

| State | Provisional direction |
|---|---|
| World exploration | Spacious, low-density frontier motif; return gently after brief UI or network interruptions. |
| Castle management/preparation | Warmer, steadier arrangement of the same motif family. |
| Mission/raid battle | Add rhythmic tension at battle start while leaving space for turn, impact and spell cues. |
| Exterior guard defeated | Short controlled breakthrough, then a pause/transition before the inner battle; not a final victory fanfare. |
| Battle result/reward | Brief resolution phrase, then return to the prior exploration/management state. |
| Optional recovery/ad choice | Calm neutral treatment; no loss-pressure sting. |
| Future event | Restrained variation of core palette; no alarm-like urgency cue. |

Use arrangement changes within a compact motif family before adding many unrelated themes. Exact instrumentation,
tempo, key, loop length and stem design are composer proposals to validate in context.

**Sample cue brief — outer guard victory:** one-shot controlled breakthrough cue after the guard result resolves;
brief breath, then silence or low-density preparation while the player reviews carry-over; end before the inner
battle start cue. It must not imply the full raid is over, and the state transition must remain clear with audio
muted.

**Readability/accessibility:** ownership, guard presence and attack eligibility need labels/icons as well as color;
important tactical/economy information remains available muted; haptics reinforce but never carry sole meaning.
Support separate music/effects levels, mute, reduced motion and short non-obscuring effects. Validate contrast,
text size, animation and performance on representative phones; no target-device budget is measured yet.

Music should support exploration, preparation, settlement management and battle with a small original motif family.
Use adaptive layers only when they clarify state and can transition without masking tactical cues. Provide an
explicit mute/music/effects balance and interruption/resume behavior. These are direction principles only: a later
game-art-music-director phase will produce a compact art bible, music bible, asset/cue inventory and production
acceptance criteria after combat presentation and scope decisions are made.

## 9. Assumptions, risks and next decisions

Assumptions for planning only: Android-first; no ads except opt-in rewarded placements; missions are a reliable
free path; PvP currency is competitive prestige, not purchasable. A persistent MMO requires authoritative online
state, identity, anti-cheat, matchmaking/rules resolution, recovery, moderation/support, observability and ongoing
hosting even if battles are asynchronous. This greatly changes scope, cost and privacy compared with the previous
offline prototype proposal.

Highest risks: MMO operating cost and service ownership; unequal progression/pay-to-win; repeat-raid harassment;
trade fraud and account theft; content/economy inflation; age-related purchase/ad constraints; weak agency in
asynchronous castle defense; overscope before a fun battle loop; imitation/IP risk. No technical stack, budget,
legal clearance, balance or engagement result is established.

Resolve before implementation: platform/age audience; battle mode and exact two-stage raid carry-over; first-release
scope and team capacity; world travel and castle protection; currencies and fair progression; trade safety; ad
and purchase rules; server/client authority and operating owner. The next task uses Homero to structure these
requirements, game-designer to develop rules and playable examples, game-art-music-director to specify art, sound
and music production, and game-developer to assess the MMO architecture. Independent prompt review is required;
implementation is a later, separately approved task.
