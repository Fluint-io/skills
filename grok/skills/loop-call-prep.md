---
name: loop-call-prep
description: >-
  Prep for an upcoming sales call, discovery call, or demo so you walk in with a
  point of view, not a list of questions. Use this skill whenever a seller says
  "prep me for this call", "help me prepare for my meeting with [name]", "build
  an agenda for the [account] call", "what should I ask on discovery", "brief me
  before this demo", "I've got a call with [name] tomorrow", or wants a pre-call
  brief, a discovery plan, or a meeting agenda. It pulls the account and attendee
  context from Loop,
  builds a POV on what is changing at the account, plans discovery on the
  Problem/Process/Payoff roadmap, and writes the opening frame and the ask.
  Prefer this over freehand prep any time a seller is getting ready for a
  buyer conversation.
---

# Call Prep

## What this does

Turns "I have a call with them" into a pack you can walk in with: a point of view on
what is changing in their world, a tight agenda, an internal brief, planned discovery,
and the exact ask you will make before you leave.

The goal is to lead with insight, not a generic question. Anyone can show up and ask
"so what are your priorities?" You show up already knowing something true about their
business, and you spend the call testing it. Discovery that sparks curiosity beats
qualification that reads like a checklist.

Work the steps in order. Steps 1 and 2 carry the weight. Skip them and the agenda sits on
nothing.

## Step 1: Lock the target and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` with who and what the call is ("call with Dana Lee at Acme about the
   security review"). No ids or types needed.
2. `get_brief` the `deal_brief` for the opportunity, if one exists.
3. `get_brief` the two or three most recent `meeting_brief`s and `email_brief`s with these
   people or this account.
4. `get_record` only for an exact quote: a meeting's own record (from its `source_records`)
   carries the call, usually with the transcript.

Where each piece goes:
- `attendees` across past meetings: who is in the room, their title, and whether they have
  ever spoken up.
- `problem_statement` and `metrics`: the raw material for the POV and the Problem questions.
- `next_steps` marked committed but not yet done, and outstanding `correspondence`: the open
  loops to raise in the first five minutes.
- The weakest predictors: what the Process questions must uncover.
- The top `next_plays` entry: the meeting objective.

How to read what comes back:
- **`next_plays`** (on the `deal_brief`) is what the seller should focus on next on this deal,
  ranked. Read the first entry's `label`, `narrative`, and `facts`, and build this play around
  moving it. If it holds only an `unsupported_reason`, there is no pick yet; say so.
- **`predictors`** (on the `deal_brief`) are Loop's read on eight things: pain validated,
  metrics quantified, champion strength, economic-buyer access, decision criteria known,
  decision process known, paper process known, and competitive position. Each carries a
  score and its reasoning. Use the weakest to decide where to focus. **Never show the seller a
  score or a predictor name.** Say what the reasoning says, in plain words: "the economic buyer
  has not been in a conversation since January", not "economic_buyer_access: 20".
- **Skip `plays`.** It tags what each past event was, not what to do next.
- **Freshness.** Every brief carries `covers_through`. Say how current it is. If the seller
  mentions something newer than the brief, flag it as `[MISSING: ...]`.
- A `meeting_brief` holds `problem_statement`, `attendees` (name, title, whether they spoke),
  `next_steps` (owner, step, committed, due), and `metrics` (the buyer's own numbers, labelled).
- An `email_brief` holds `correspondence`: what is still outstanding on the thread.
- An `activity_brief` holds a `timeline` of logged tasks and notes. It lives on the deal's own
  `entity_ref`: call `get_brief` with that ref and `brief_type: "activity_brief"`.
- A deal brief does not list its meetings. Find them with `find_briefs` naming the account,
  filtered to `brief_types: ["meeting_brief", "email_brief"]`. A meeting brief's
  `source_records` names its deal (`hubspot_deal:123` is the deal at `hubspot:deal:123`).

**Loop not connected?** Stop and tell the seller to connect it before going further: in Grok add it at grok.com/connectors (New Connector, then Custom, URL `https://mcp.fluint.io/mcp`), or follow
https://app.fluint.io/install.
Do not fall back to any other tool.

Confirm the basics before building: who you are meeting (name, role), the account, the
stage, and what this meeting is for. If any are unclear, ask.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Build the POV

Read `references/frameworks.md` (POV section). A point of view is a short, specific read on
what is changing at the account that makes your thing matter more now than six months ago.
Not a pitch.

Lead with something you actually found in the briefs: a line in a `problem_statement`, a
number in `metrics`, a theme that keeps coming up across meetings, a pattern in the deal
summary. Then draw the line: what does that
change mean for them, and whose priority does it touch. A problem only gets funded when
it blocks a priority someone already owns.

If the briefs hold no real signal, say so (`[MISSING: no recent trigger in Loop]`) rather
than inventing one. A made-up POV dies the moment they poke it.

## Step 3: Plan the discovery

Read `references/frameworks.md` (Discovery Roadmap section) and plan questions across the
three stages, in order:
- **Problem (current state):** help them see the gap between where they are and where
  they should be. Lead with your insight, then reframe.
- **Process (building a path):** test whether they are serious. What must be true of a
  solution? What would stop this internally? Who else has to agree?
- **Payoff (future state):** make the outcome concrete and numbered. What does success
  look like, and is it big enough to warrant leadership attention?

Pull specific reframing questions from the bank in `references/output-templates.md`. Every
question should earn a "huh, I have not thought about that." If it has a known answer you
could have Googled, it is qualification, not discovery. Cut it.

## Step 4: Write the opening frame

Draft the first 90 seconds: a 4 to 5 sentence insight statement that names the change,
quantifies the opportunity or risk, and asks permission to go deeper. This is what earns
you the room. See the template.

## Step 5: Name the ask

Decide the single commitment you will request before you leave, and make it cost them
something small. Not "does this sound good." A next meeting with a named person, a data
pull, an intro. Pick the right rung on the Commitment Ladder (`references/frameworks.md`)
for where the deal actually is.

## The deliverable

The seller walks away with a Meeting Brief they can open on the way in, built to the skeleton
in `references/output-templates.md` (the same structure as the Exec Brief and Pre-Demo
Planning Sheet):
1. **Meeting objective** (the next buying behavior this call should unlock, and the evidence
   that it worked)
2. **POV** (what is changing, why now, whose priority) plus the 4-sentence soundbite
3. **Attendees** (who is in the room, role, and the #1 question in each person's head)
4. **Opening frame** (the 4 to 5 sentence insight statement for the first 90 seconds)
5. **Discovery plan** (questions grouped by Problem / Process / Payoff)
6. **Threats and alternatives** (what you lose to if this stalls: a competitor, a build, a
   competing priority)
7. **The ask** (the specific commitment, and the Commitment Ladder rung it sits on)

Keep it to one screen. A brief you cannot skim on the way to the meeting is too long.

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Lead with insight, not a question.** Come with a read on their world and test it.
- **Discovery sparks curiosity. Qualification checks boxes.** If you know the answer, do
  not ask it.
- **Every call ends in a commitment.** Know the ask before you walk in.
- **No invented signals.** A flagged gap beats a confident guess that collapses on contact.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/frameworks.md

# Frameworks: Call Prep

The models this skill runs on. Apply them; do not just cite them.

## POV: lead with what is changing

A point of view has three moves. Keep it to three or four sentences.

1. **The change.** Something specific and recent at the account: a hire, a reorg, a
   launch, a raise, a number from their earnings call, a pattern in the deal history.
   Real and cited, not "the market is evolving."
2. **The "which means."** What that change does to them. Chain it forward: this change
   means this pressure, which means this cost or this risk.
3. **Whose priority it touches.** Name the executive initiative or metric it lands on. A
   problem only gets funded when it blocks a priority someone already owns. An orphaned
   problem, however real, gets deferred.

If you cannot find a real change, do not manufacture one. Flag it and go get it.

## The 4-sentence soundbite

Compress the POV into four sentences you could say in the room or drop at the top of the brief:
1. Because of [the major shift / change in their business or market],
2. now is the time for [account] to [the strategy you uniquely enable],
3. when they do, they will avoid [negative outcomes that worsen over time],
4. while unlocking [positive outcomes that align with a priority they own].

## The Meeting Brief

The brief assembles the prep into one page the seller opens on the way in. It is the same
structure as an Exec Brief or Pre-Demo Planning Sheet:
- **Objective:** the next buying behavior this call should unlock, and the evidence that it
  worked. Also, what the key contact should feel after, and why.
- **Current state / negative outcomes:** despite trying [failed solution], they still cannot
  [outcome] because of [problem], costing [impact].
- **Why now:** the executive pushing a priority, the internal project name, the compelling
  event they are working toward.
- **Future state / positive outcomes:** their metrics, current measure, and target by a date.
- **Threats and alternatives:** if you lose, it is to a competitor, a build, or a competing
  priority. Name which, and your edge against it.
- **Attendees and the #1 question** in each person's head (e.g. "how is this different from
  the last time we tried?").
- **Value map:** for the one or two things you will cover, line up problem, root cause,
  impact, the capability required, your differentiator, and the outcome. This keeps the call
  anchored to their problem, not your feature list.

## The Discovery Roadmap: Problem, Process, Payoff

Three stages, always in order. You are moving the buyer from where they are to where they
want to go, and the bridge in the middle is what most sellers skip.

**Stage 1 - Problem (current state).** Help them see the gap. Lead with your insight,
then reframe what they say to go deeper.
- What insight from their data or world are you leading with?
- What does that pattern mean for the business?
- What is the cost of the gap, in numbers?
- Why is this the priority now versus six months from now? (deadline, trigger, worsening trend)

**Stage 2 - Process (building a path).** Test whether they are serious. This is where you
surface friction, alternatives, and the buying group.
- What must be true of a solution for this to be worth pursuing?
- Are there better alternatives we should consider? (do nothing, build it, a competitor)
- What will stop our progress, internally or externally?
- Who else has to be comfortable with this before it moves?
- Has anything like this been tried before? What happened?

**Stage 3 - Payoff (future state).** Make the outcome concrete and numbered.
- How do we measure success? What does the outcome look like in numbers?
- Will this make or save money, and how much?
- What is the cost to act versus the payoff?
- Is this big enough to warrant leadership attention?
- What is the timeline to realize the value?

## The reframe

Discovery is a series of reframes, not a question list. When the buyer makes a flat
statement, reframe it into a sharper question that splits the problem open. "We need to
cut costs" becomes "are you looking to spend less, or get more from what you already
spend?" Those are two different deals. The reframe is what turns a surface answer into the
real problem. See the reframe bank in `output-templates.md`.

The single best follow-up, always available: **"What is an example of that?"** It turns a
generality into the specific, repeatable story you can actually use.

## The opening frame

The first 90 seconds decide whether you get the room. Structure it as a 4 to 5 sentence
insight statement:
- Name the change you have spotted.
- Quantify the opportunity or the risk.
- Draw the line to a priority they own.
- Ask permission to go deeper.

Confident, specific, and short. Then stop talking and let them react.

## The Commitment Ladder

Not all commitments are equal. Do not jump rungs, climb them. After the call you should
have secured one, and know which one you are targeting going in.

1. **Time** - a deep-dive or follow-up with a key person.
2. **Data** - they share documents, numbers, or access for analysis.
3. **Introduction** - your contact introduces you to another stakeholder, putting their
   credibility behind you.
4. **Calendar hold** - real hours blocked for planning.
5. **Group / exec presentation** - your contact presents your recommendation internally.
6. **Approval** - signed.

The ask you name in prep should be the next rung up from where the deal actually sits, and
it should cost them something small. A commitment that costs nothing tells you nothing.

## references/output-templates.md

# Output Templates: Call Prep

## The Meeting Brief (produce this)

```
# Meeting Brief: [Account] - [meeting purpose]
Meeting: [date/time] · With: [names + roles] · Stage: [stage]

## Objective
Unlock [next buying behavior]. Success = we see [evidence] by the end.
[Key contact] should feel [emotion] after, based on [context].

## POV - what is changing
[3 to 4 sentences. The change (cited) → what it means → whose priority it touches.]
Soundbite: Because of [shift], now is the time for [account] to [strategy]. When they do,
they avoid [negative outcomes] while unlocking [positive outcomes].

## Who is in the room
| Person | Role | #1 question in their head |
|--------|------|---------------------------|
| [name] | [title] | ["how is this different from the last time?"] |

## Opening frame (first 90 seconds)
[4 to 5 sentences. Name the change. Quantify it. Draw the line to a priority. Ask to go deeper.]

## Discovery plan
**Problem (current state)** - [question led by your insight] · [reframe]
**Process (building a path)** - What must be true of a solution? · [who else has to agree]
**Payoff (future state)** - [how success gets measured, in numbers] · [is this leadership-level]

## Threats and alternatives
- [competitor / build / competing priority], and your edge against it.

## The ask
[The single commitment you will request, and the Commitment Ladder rung it sits on.
Make it cost them something small.]

## Open gaps
- [MISSING: ...] items to close before or during the call
```

## Reframe bank (generalize to the account in front of you)

Pull and adapt. When the buyer says the thing on the left, ask the thing on the right.

| They say | You reframe | What it uncovers |
|----------|-------------|------------------|
| "We need to cut costs." | "Spend less, or get more from what you already spend?" | Cost-cut vs ROI. Two different deals. |
| "We want to keep things simple." | "Simple meaning fewer tools, fewer decisions, or fewer people involved?" | A structural preference vs a bandwidth problem. |
| "We handle that internally." | "Who actually owns it, and how often does it reach leadership?" | Whether it is a real program or falls through the cracks. |
| "We have always done it this way." | "Because it is right, or because nobody revisited it when things changed?" | Deliberate choice vs institutional inertia. |
| "This is a priority." | "What would you deprioritize to make room for it?" | Whether it is actually funded or just agreeable. |
| "We are worried about [risk]." | "Have you tested that, or is it the fear of it?" | Moves theoretical fear to data. Often the fear is unfounded. |
| "[Their big initiative] is the priority right now." | "Is this separate from that, or actually part of getting it right?" | Reframes your work as enabling their priority, not competing with it. |

## Notes

- Keep the whole pack to one screen.
- Every discovery question should earn a "I have not thought about that." If it has a
  known, Google-able answer, it is qualification. Cut it.
- No em dashes, no jargon, no filler in anything the seller might paste into a calendar
  invite or forward to a manager.
