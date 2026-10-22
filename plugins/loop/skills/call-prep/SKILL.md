---
name: call-prep
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

**Loop not connected?** Stop and tell the seller to connect it before going further: in
Claude Code run `/mcp` and authenticate `loop`, or follow
https://raw.githubusercontent.com/Fluint-io/skills/main/INSTALL.md.
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
