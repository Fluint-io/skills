# Uncommon Sales Skills

**Ten skills that run enterprise-level sales plays the way top reps _actually_ win.**

Your favorite LLMs are trained with market average inputs, which creates generic outputs. These skills encode the specific, hard-earned wisdom that separates reps who close complex deals from reps who get stuck: selling in the buyer's own language, selling during the meetings you're not in the room for, and crafting forwardable, sticky messages. They'll pull from your live deal data, and give you tactical assets for each deal.

Built by [Nate Nasralla](https://www.fluint.io), author of *Selling With* and *Brief & Brilliant*, on the frameworks from both books.

---

## What to expect from the library of _uncommon_ skills

- **They sell with the buyer's language, not yours.** These skills mine your call transcripts and emails for the exact words the buyer used, override the LLMs default tendencies, and write in a way that makes it easy for champions to forward your message. Which makes all the difference.

- **They're built on what's _not_ in training data.** Every skill is anchored to a specific framework tested by 1,000's of sellers and built into *Selling With* and *Brief & Brilliant*.

- **A single system, built with judgment.** Each skill builds on top of the others to create a single, end-to-end system that mirrors what a seasoned seller has: judgment. The ability to weave together multiple skillsets into a single deal.

- **Every skill builds in a tangible asset.** Not analysis you still have to figure out how act on. A forwardable follow-up, a champion toolkit, a leadership brief, etc... You finish with the thing, ready to ship.

- **They run on your real data.** The skills pull every deal from Loop, Fluint's MCP, which already fuses your CRM, calls, and email. When a fact is missing, they flag it and tell you what to do next.

---

## The plays

Not sure which one you need? Start with **loop-plays**, the front door. Describe your deal and it routes you to the right play.

Every skill carries a `loop-` prefix, so they group together in the slash-command menu and never collide with another plugin's `call-prep` or `qbr`.

| Skill | What it does |
|-------|--------------|
| **loop-plays** | The front door. Describe a deal situation and it names the moment and routes you to the right play below. |
| **loop-multithread** | Map the buying committee on a new account or a single-threaded deal, then draft the outreach to widen it. |
| **loop-account-plan** | Build a POV and a strategic account plan, or find and rank expansion whitespace in an existing account. |
| **loop-call-prep** | Walk into a call with a Meeting Brief: a point of view, planned discovery, an opening frame, and the ask. |
| **loop-follow-up** | Turn a call or demo into a stakeholder map, a confirmed problem in the buyer's words, and forwardable per-person follow-ups. |
| **loop-champion** | Build the internal-selling kit your champion uses in the meetings you are not in: soundbite, objection reframes, a one-pager. |
| **loop-displace** | Unseat an incumbent by changing the criteria, not winning a feature war. Differentiation, a switching story, and trap-setting questions. |
| **loop-advance** | Diagnose why a deal stalled and generate moves to restart it, or build a backdated mutual action plan to close it. |
| **loop-qbr** | Prep a customer quarterly review that leads with their success, gets ahead of risk, and opens expansion without a pitch. |
| **loop-manage-up** | Prep for a forecast call or deal review: an honest read of the territory, the big bets, and specific asks of leadership. |
| **loop-business-case** | Build a customer-specific one-page business case from your deal data, scored against a rubric, with the next move to strengthen it. |
| **olli** | Turn the chat into a conversation with Olli, Fluint's AI sales agent: brief, calm, strategic, in the buyer's words. Olli reads your deals from Loop and runs the plays above when you ask for a deliverable. |

---

## Install

Paste this into Claude Code (or Codex):

```
Install and set up Uncommon Sales Skills and the Loop MCP by following https://raw.githubusercontent.com/Fluint-io/uncommon-sales-skills/main/INSTALL.md
```

That installs all eleven `/loop-*` plays plus `/olli` and connects Loop, Fluint's MCP (`https://mcp.fluint.io/mcp`). The only step left to you is signing in to Fluint in the browser. Using the Claude app or a ChatGPT workspace instead? [INSTALL.md](INSTALL.md) has the click-through steps.

### Renamed skills

If you installed an earlier version, the skills were renamed to the `loop-` prefix:

| Was | Now |
|-----|-----|
| sales-plays | `loop-plays` |
| multithread | `loop-multithread` |
| account-planning | `loop-account-plan` |
| call-prep | `loop-call-prep` |
| call-follow-up | `loop-follow-up` |
| champion-enablement | `loop-champion` |
| competitive-displacement | `loop-displace` |
| deal-advancement | `loop-advance` |
| qbr-prep | `loop-qbr` |
| manage-up | `loop-manage-up` |
| one-page-business-case | `loop-business-case` |

---

## Using a skill

You do not have to run a command. Describe what you are doing, and Claude reaches for the right skill. Every skill triggers on natural language:

- *"Prep me for my call with the VP of Ops at Acme tomorrow."* → **loop-call-prep**
- *"Help me follow up after that demo, there were four people on it."* → **loop-follow-up**
- *"This deal is single-threaded, help me multithread it."* → **loop-multithread**
- *"Why is the Acme deal stuck?"* → **loop-advance**
- *"Build the business case for Acme."* → **loop-business-case**
- *"Prep me for my forecast call, I need an intro from my VP."* → **loop-manage-up**

Prefer to pick the play yourself? Type `/loop-` and choose from the menu, e.g. `/loop-call-prep Acme, Thursday, VP of Ops`. In Codex, use `$loop-call-prep`.

The skill gathers your deal context, applies the framework, and hands you the deliverable. If something it needs is missing, it tells you the one question to go ask.

---

## How the data sourcing works

Loop is the only data source. Every skill reads the deal the same way:

1. **Find the briefs.** Loop, Fluint's MCP, already fuses your CRM, calls, and emails into deal, meeting, email, and activity briefs. `find_briefs` asks the question in plain words. No ids or object types needed.
2. **Read what matters.** `get_brief` reads the few briefs that matter for the play in full: a deal brief's summary, its next plays, and Loop's read on the deal; a meeting brief's problem statement, attendees, next steps, and the buyer's own numbers; an email brief's outstanding asks.
3. **Focus on the next play.** A deal brief's `next_plays` is what the seller should focus on next. Every deal play is built around moving it. Loop's read on the deal (pain, champion, economic-buyer access, and so on) decides where the play digs in, and is always put in plain words, never as a score.
4. **Pull evidence only when needed.** `get_record` pulls one raw record (an amount, a close date, a verbatim line), and only by a ref a brief points to. The brief is the answer; the record is the evidence.
5. **Flag the gaps.** Every brief says how fresh it is (`covers_through`). When something is stale or was never captured, the skill marks it `[MISSING: ...]` and names the single highest-leverage move to close it. It never invents a number.

If Loop is not connected, the skill stops and tells you how to connect it. It does not go looking in other tools.

---

## Who this is for

Account executives, sales engineers, and account managers running complex, multi-stakeholder, mid-market and enterprise deals. If your deals get made in rooms you are not in, and won or lost on whether your champion can carry the message, these are built for you.

---

## The thinking behind it

These skills are the productized version of the system in two books:

- ***Selling With*** — the art of selling with champions to shape the internal buying conversations that decide enterprise deals.
- ***Brief & Brilliant*** — how to simplify complex deals and sell through the noise, in the buyer's own language.

---

## Contributing and feedback

Found a rough edge, or a play you would run differently? Open an issue. These are living skills, tuned from real deals.

## License

MIT. Use them, adapt them, run them on your own pipeline.
