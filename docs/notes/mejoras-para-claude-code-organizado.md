# Claude Code improvements: organized resource list

Source: `mejroas-para-claude-code.MD` (same folder). Every item from the source is kept. Repeated mentions are merged into one entry, with the other places they appeared listed under "Also in".

Links are taken from the source when it gives one. When it does not, the entry has a GitHub search link for its name. Those links were **not verified**: check the first result before installing anything.

Before installing any entry, review its license, install scripts and permissions (see `infra:dependency-license-review`). Do not run installers from the vendor folder.

---

## 1. Design and UI skills

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Impeccable | Gives the agent design taste. Adds commands such as polish, audit and critique, plus deterministic detectors for AI-style design problems. Uses references from award-winning interfaces. | https://github.com/pbakaus/impeccable | Listed 3 times in the source |
| UI UX Pro Max | Design intelligence for web, mobile and desktop. Recommends colors, typography, styles and design rules from the type of product you describe. | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Listed 2 times |
| Taste Skill | Agent Skills that make coding agents design interfaces with taste instead of generic "AI slop". Uses real open-license photos, and checks its own work in a real browser at several widths. | https://github.com/Leonxlnx/taste-skill | "taste-skill Claude skills", listed 2 times |
| Hallmark | Anti-AI-slop design skill. Forces interfaces with a human look and creative themes. | https://github.com/Nutlope/hallmark | Also "Anti-UI Slop" in the ECC list (concept similar, no link) |
| Skill UI | You mark a design you like, and it becomes a file Claude uses to recreate that style in your project. | Search on GitHub: https://github.com/search?q=%22skill+ui%22+claude&type=repositories | |
| Minimalist UI | Minimal design skill. | Search on GitHub: https://github.com/search?q=%22minimalist-ui%22+claude+skill&type=repositories | ECC list |
| Canvas Design | Design skill for canvas-style layouts. | Search on GitHub: https://github.com/search?q=%22canvas+design%22+claude+skill&type=repositories | ECC list |
| Web Design Guidelines | Reviews UI code against web interface guidelines. | Search on GitHub: https://github.com/search?q=%22web-design-guidelines%22+claude&type=repositories | ECC list |
| React Bits | Open-source library of 215+ animated, interactive React and Next.js components and backgrounds. Also built for AI agents to use. | https://github.com/DavidHDev/react-bits | Listed 2 times |
| GSAP Skills | Official GSAP skills. Teach agents to use the GreenSock animation platform correctly. | https://github.com/greensock/gsap-skills | |
| transitions.dev | UI motion library: 43+ CSS and React transitions, plus a skill for agents. | https://github.com/Jakubantalik/transitions.dev | Also "transitions.dev" in the links list |
| Magic (21st.dev) | Thousands of professional components so your site does not look AI-made. | https://21st.dev (Magic MCP) | |
| Awesome Design | Brand design systems (Apple, Notion, Stripe, etc.) in markdown, for Claude to use as reference. Tens of thousands of stars. | Search on GitHub: https://github.com/search?q=%22awesome+design%22+claude&type=repositories | |
| Diagram Design | Editorial technical diagrams (45 types) as self-contained HTML + SVG. Avoids the generic Mermaid look. | https://github.com/cathrynlavery/diagram-design | Listed 2 times |
| design-extract | Extracts the full design system from any live website in one command, using Playwright. Produces 17+ output files. | https://github.com/Manavarya09/design-extract | |
| Replica skill | Skill that replicates a design or interface. | https://github.com/Jakeschincariol/replica-skill | |
| Anti-UI Slop | Design skill that removes generic AI UI patterns. | Search on GitHub: https://github.com/search?q=%22anti-ui-slop%22&type=repositories | ECC list |
| Hallmark / Anti-UI Slop | See Hallmark above. | | |

## 2. Engineering and workflow skills

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Ponytail | Makes the agent write the least code that works: no over-engineering, reuses existing code. The author reports about 54% less code and about 22% fewer tokens in their test. | https://github.com/DietrichGebert/ponytail | Listed 4 times (incl. ECC-style lists) |
| Addy Osmani Agent Skills | 24–25 senior-engineer skills for spec, plan, build, test, review and ship (`/spec /plan /build /test /review /ship`). They activate on their own at the right stage. | Search on GitHub: https://github.com/search?q=%22addy+osmani%22+agent-skills&type=repositories | Listed 4 times |
| Superpowers | Full dev workflow: brainstorming, a spec you approve, TDD with subagents, code review. About 300k stars. | Search on GitHub: https://github.com/search?q=superpowers+claude+skills&type=repositories | |
| Matt Pocock Skills | Engineering and productivity skills: TDD, code review, architecture, handoffs. | Search on GitHub: https://github.com/search?q=%22matt+pocock%22+skills&type=repositories | |
| Karpathy Skills | One CLAUDE.md with four rules: think before coding, keep it simple, touch only what was asked, prove it works. | Search on GitHub: https://github.com/search?q=karpathy+claude.md&type=repositories | |
| Grill Me (`/grill-me`) | Asks questions until nothing is vague. | Search on GitHub: https://github.com/search?q=%22grill-me%22+claude+skill&type=repositories | Prompt-series list (2 times), ECC list |
| Caveman | Short, direct responses. By Juliuss Brussee. | Search on GitHub: https://github.com/search?q=caveman+claude+skill&type=repositories | "claud caveman", ECC list |
| Agent Browser | Lets Claude browse and check pages. | Search on GitHub: https://github.com/search?q=%22agent-browser%22+claude&type=repositories | ECC list |
| Find Skills | Helps find and install skills. | Search on GitHub: https://github.com/search?q=%22find-skills%22+claude&type=repositories | ECC list; "finding skills - versell" list (8 skills) |
| Arena | Runs competing solutions to the same task through attack, revision and independent judging until one wins. | https://github.com/Jakeschincariol/arena | Listed 2 times (also the `arena` skill in this workshop) |
| Claude Octopus | Sends the same task to up to 12 models and points out where they disagree. | Search on GitHub: https://github.com/search?q=%22claude+octopus%22&type=repositories | |
| affaan-m/ECC | Large Claude Code configuration collection (agents, skills, hooks). | https://github.com/affaan-m/ECC | |
| Task Observer | Shows what each task or agent is doing. | Search on GitHub: https://github.com/search?q=%22task+observer%22+claude&type=repositories | Listed 3 times ("Task observer Claude skill", "task observer", "task observer" in mods) |
| Not Fair (plugin) | Claude Code plugin, listed as "Not fair Claude plugin". | Search on GitHub: https://github.com/search?q=%22not+fair%22+claude+plugin&type=repositories | "finding skills" list |
| Find Claude skill | Skill to find other skills. | Search on GitHub (name too generic) | "finding skills" list |
| Genjutsu Claude skill | Skill listed in the finding-skills list. | Search on GitHub: https://github.com/search?q=genjutsu+claude+skill&type=repositories | "finding skills" list |
| UX/UI Agent | UX and UI agent. | Search on GitHub: https://github.com/search?q=%22ux+ui+agent%22+claude&type=repositories | "finding skills" list |
| Business Claude skill | Business-oriented skill. | Search on GitHub (name too generic) | "finding skills" list |
| AI Harmozi Skill | Skill listed in the finding-skills list. | Search on GitHub: https://github.com/search?q=harmozi+claude+skill&type=repositories | "finding skills" list |
| Claude Setup | Claude setup helper. | Search on GitHub: https://github.com/search?q=%22claude+setup%22+claude+code&type=repositories | Mods list |
| Collision Guard | Asks you before two chats touch the same file. | Search on GitHub: https://github.com/search?q=collision-guard+claude&type=repositories | Mods list |
| Ruflo | Turns Claude Code into an AI team: swarms, memory across sessions, 98 agents and 30 skills, hooks that route tasks, and a console. MIT licensed. Works with Claude Code and Codex. Formerly Claude Flow. About 77k stars. | Search on GitHub: https://github.com/search?q=ruflo+claude+flow&type=repositories | Also in the "motores" section below as a harness |
| Hand Off (`/handoff`) | Creates a handoff document to start the next chat. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| Write a Skill (`/write-a-skill`) | Turns a workflow into a reusable skill. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| Prompt Maker (`/prompt-master`) | Turns a messy brain dump into a clean task spec. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| How To (`/alexaiupdates`) | Maps the steps you do not know yet. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| Optimizer 4.8 (`/48`) | Polishes a prompt for Opus 4.8. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| Fable Prompter (`/fable`) | Same polish, for Fable 5. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |
| Personal Voice (`/personal-voice`) | Tunes text to sound like you. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |

## 3. Writing and text skills

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Humanizer | Removes typical AI-text signs (empty phrases, predictable structure) so text reads as written by a person, without changing content. | https://github.com/blader/humanizer | Listed 2 times |
| I Have ADHD | Makes Claude open with the next step, use numbered instructions and short answers. | Search on GitHub: https://github.com/search?q=%22i+have+adhd%22+claude&type=repositories | Listed 3 times (also "I have adhd Claude skill") |
| No AI Slop | Improves AI-generated text so it sounds more natural. | Search on GitHub: https://github.com/search?q=%22no+ai+slop%22&type=repositories | Apps list |
| Anti-AI (`/anti-ai`) | Strips AI tells from a draft. | Search on GitHub (part of the prompt series) | Prompt-series list (2 times) |

## 4. Security skills and tools

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Security Audit Skill (Cloudflare) | Turns the coding agent into a security auditor that reports verified findings. | Search on GitHub: https://github.com/search?q=cloudflare+security+audit+skill&type=repositories | |
| Strix | Attacks your app like a hacker and reports where the holes are. **Use only on your own apps.** | Search on GitHub: https://github.com/search?q=strix+security+agent&type=repositories | Listed 3 times |
| REA (Reverse Engineer Anything) | MCP + CLI that lets agents analyze binaries, apps and runtime behavior with Ghidra, Hopper, IDA, etc. | https://github.com/morluto/rea | |

## 5. Research, data and scraping

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Playwright CLI | Official Playwright CLI for coding agents. Lets Claude open a browser, test the app and catch visual or functional errors before you do. | https://github.com/microsoft/playwright-cli | Listed 3 times ("Playwright CLI", "Playwright", "playwright-cli") |
| Scrapling | Resilient scraping framework. Adapts when sites change layout. Has an MCP server. About 89k stars. | https://github.com/D4Vinci/Scrapling | Listed 2 times |
| Last 30 Days | Researches a topic in recent Reddit, X, YouTube and Hacker News discussions and returns a sourced summary. | https://github.com/mvanhorn/last30days-skill | |
| PaddleOCR | OCR that turns PDFs and images into structured JSON or Markdown for LLMs. 100+ languages. About 90k stars. | https://github.com/PaddlePaddle/PaddleOCR | |
| changedetection.io | Watches web pages and alerts you on change (Discord, Slack, email, Telegram, webhook). Has AI filtering. | https://github.com/dgtlmoon/changedetection.io | |
| Open Notebook | Turns PDFs, videos and websites into a private research assistant. | Search on GitHub: https://github.com/search?q=%22open+notebook%22+ai&type=repositories | |
| Book to Skill | Turns books into reusable knowledge. | Search on GitHub: https://github.com/search?q=%22book+to+skill%22&type=repositories | Apps list |
| Video Lens | Video analysis skill. | Search on GitHub: https://github.com/search?q=%22video+lens%22+claude&type=repositories | ECC list |
| Video Use | Video use skill. | Search on GitHub: https://github.com/search?q=%22video+use%22+claude+skill&type=repositories | ECC list |
| Context7 | Gives up-to-date library documentation, so code does not use old versions. | Search on GitHub: https://github.com/search?q=context7+mcp&type=repositories | |
| Perplexity (connector) | Research connector, marked as "investigado" (researched) in the source. | Connector inside Claude | Connectors list |
| Firecrawl | Scrapes complex JavaScript-heavy sites. Available as a connector and as a plugin. | https://github.com/mendableai/firecrawl | Listed 2 times (connector and plugin) |
| Graphify | Turns a codebase, docs and schemas into a knowledge graph. The agent queries it instead of re-reading files. The source reports 71.5× fewer tokens per query. About 119k stars. | Search on GitHub: https://github.com/search?q=graphify+knowledge+graph+claude&type=repositories | Listed 3 times |

## 6. SEO, business and content

| Resource | What it does | Link | Also in |
|---|---|---|---|
| OpenSEO / open-seo | Open-source alternative to Semrush and Ahrefs. SEO analysis, audits and competitors. Has skills and MCP. Needs your own DataForSEO key. About 24.5k stars. | https://github.com/every-app/open-seo | Listed 2 times |
| SEO Audit | SEO audit skill. | Search on GitHub: https://github.com/search?q=%22seo+audit%22+claude+skill&type=repositories | ECC list |
| AI SEO | AI-search SEO skill. | Search on GitHub: https://github.com/search?q=%22ai+seo%22+claude+skill&type=repositories | ECC list |
| Content Strategy | Content strategy skill. | Search on GitHub: https://github.com/search?q=%22content+strategy%22+claude+skill&type=repositories | ECC list |
| Pricing | Pricing skill. | Search on GitHub: https://github.com/search?q=%22pricing%22+claude+skill&type=repositories | ECC list |
| AI Job Search | Analyzes job offers and helps with applications. | Search on GitHub: https://github.com/search?q=%22ai-job-search%22&type=repositories | Apps list |
| linkedin-roast skill | Roasts your LinkedIn profile. By Alex Chen (@nocodealex). | https://github.com/alexyc9381/linkedin-roast-skill | "/linkedin-roast" entry |
| Dataset: Day Trader skills | 11 free Claude skills, each with one job. | https://github.com/Jakeschincariol/day-trader-skills | Listed 1 time |

## 7. Trading (note: unrelated to Claude Code improvements, kept for completeness)

| Resource | What it does | Link | Also in |
|---|---|---|---|
| TradingAgents | Open-source (Apache-2.0) multi-agent LLM framework that simulates a trading firm. | https://github.com/TauricResearch/TradingAgents | |

## 8. Apps and platforms

| Resource | What it does | Link | Also in |
|---|---|---|---|
| trycompai/crm | Agentic-first open-source CRM (Next.js, NestJS, Prisma). About 12k stars. | https://github.com/trycompai/crm | |
| ai-website-cloner-template | Clones any website into a clean Next.js app with one command from an agent. About 36–37k stars. | https://github.com/JCodesMore/ai-website-cloner-template | |
| ppt-master | Turns documents or topics into native PowerPoint files. Supports your own .pptx templates. About 64k stars. | https://github.com/hugohe3/ppt-master | |
| Onyx | Self-hosted open-source AI chat connected to your knowledge sources (RAG). Works with any LLM. | https://github.com/onyx-dot-app/onyx | |
| Open Generative AI | Experiment with image and video generation. | Search on GitHub: https://github.com/search?q=%22open+generative+ai%22&type=repositories | Apps list |
| Obsidian (plugin) | Turns your folders into a second brain connected to Claude Code. | Search on GitHub: https://github.com/search?q=obsidian+claude+code+plugin&type=repositories | Plugins list |

## 9. Claude Code plugins and mods

| Resource | What it does | Link | Also in |
|---|---|---|---|
| Codex plugin (codex-plugin-cc) | Connects Claude with OpenAI so both work as a team that reviews and improves each other's output. | https://github.com/openai/codex-plugin-cc | Listed 2 times (it is also a link in the source) |
| claude-mem | Remembers past sessions, so you do not re-explain the project each morning. | Search on GitHub: https://github.com/search?q=claude-mem&type=repositories | Listed 2 times |
| headroom | Context-related plugin. | Search on GitHub: https://github.com/search?q=headroom+claude+code&type=repositories | Mods list |
| Habblaud | Each agent is a character in a pixel-art office. | Search on GitHub: https://github.com/search?q=habblaud+claude&type=repositories | Mods list |
| claude-pets / intermission | A pet that levels up, or a Doom game, while you wait. | Search on GitHub: https://github.com/search?q=claude-pets+claude+code&type=repositories | Mods list |
| Archify | Mod to be looked up in the source ("buscar el repo y para qué sirve"). | Search on GitHub: https://github.com/search?q=archify+claude+code&type=repositories | Mods list |
| Mod: the "portero" (gatekeeper) | Concept: send easy tasks to a cheaper model so your limit lasts longer. Build it with a hook or a mod. | No specific repo in the source | Mods list |
| Mod: Claude talks to Claude | Concept: one model plans and another builds. | No specific repo in the source | Mods list |
| Mod: your own panel | Concept: see what each agent does without asking. | No specific repo in the source | Mods list |

## 10. Model gateways and engines

| Resource | What it does | Link | Also in |
|---|---|---|---|
| OmniRoute (Omni Route) | One local endpoint for about 150–352 providers, with free tiers. Switches models when your Claude limit is hit. Up to 1.6B free tokens a month. About 68k stars. | Search on GitHub: https://github.com/search?q=omniroute+ai+gateway&type=repositories | Listed 3 times |
| Meta AI (engine) | Meta's AI assistant. | https://www.meta.ai/ | "motores nuevos" |
| Grok (engine) | xAI's assistant. | https://grok.com/ | "motores nuevos" |
| Typesafe AI (engine) | AI engine listed as new. | https://typesafe.ai/ | "motores nuevos" |

## 11. Slash commands (Claude Code)

| Command | Use | Also in |
|---|---|---|
| `/compact` | Summarize the conversation to free context. | Commands list |
| `/clear` | Clear the conversation. | Commands list |
| `/context` | Show context usage. | Commands list |
| `/init` | Create a CLAUDE.md for the project. | Commands list |
| `/permissions` | Manage permissions. | Commands list |
| `/goal` | Set a goal for the session. | Commands list |
| `/loop` | Run a prompt on a repeating interval. | Commands list |
| `/doctor` | Check the Claude Code installation. | Commands list |
| `/rewind` | Go back to an earlier point. | Commands list |
| `/usage` | Show usage. | Commands list |

## 12. Concepts and tips (no single resource)

- Install a skill: find it on GitHub, copy the repo, and ask Claude to install it. (Source: "Graphify" how-to.)
- Use the prompt-series skills in order when you have a messy idea: Prompt Maker → Grill Me → How To → Optimizer → Fable Prompter or Personal Voice → Anti-AI → Write a Skill → Hand Off.
- Keep the prompt-series skills in the list above only once. The source repeats the same list twice.

---

## Duplicates merged

- Ponytail, Impeccable, UI UX Pro Max, Graphify, Playwright CLI, Scrapling, Humanizer, OpenSEO, Codex plugin, claude-mem, Firecrawl, Taste Skill, React Bits, Diagram Design, I Have ADHD, Task Observer, Strix, OmniRoute, Addy Osmani Skills, the prompt-series list, and the Hallmark/Anti-UI Slop pair: each appeared in several places and is listed once.
- Playwright CLI, Playwright and playwright-cli are merged into the single entry in section 5 (https://github.com/microsoft/playwright-cli).
