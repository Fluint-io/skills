---
name: loop-follow-up
description: >-
  Turn a call or group demo into the follow-up that actually moves the deal. Use
  this skill whenever a seller says "follow up after my call", "debrief this
  call", "write a recap email", "who was on the demo and what do I send each of
  them", "post-call follow-up", "send a follow-up to each stakeholder", "help me
  after this discovery call", or wants to process what just happened on a buyer
  conversation. It pulls the meeting from Loop, maps who cared about what, locks the confirmed
  problem in the buyer's own words, surfaces the skeptics and objections that
  showed up, drafts forwardable per-stakeholder follow-ups, and debriefs where
  discovery went thin. Prefer this over a generic recap email any time a call or
  demo just happened.
---

# Call Follow-Up

## What this does

A call just happened. Most reps send one bland recap to one person and move on. That is a
missed follow-up. This skill produces a set of forwardable assets instead:

1. A stakeholder map: who was there and what each one actually cared about.
2. The problem locked in the buyer's own words, so it survives being forwarded.
3. The skeptics and objections that showed up, spoken or not, with the opening to engage.
4. A forwardable follow-up per stakeholder, tied to what they care about.
5. A discovery debrief on where the call was thin, so the next one is sharper.

Follow-up is how you keep selling in the meetings you will not be in. Write for the person
who was in the room and for whoever they forward it to next.

## Step 1: Lock the target and pull the meeting

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the call ("the demo with Acme on Tuesday"), filtered to
   `brief_types: ["meeting_brief"]`.
2. `get_brief` that `meeting_brief`. It is the record of the call.
3. `get_brief` the `deal_brief` it belongs to (named in the meeting brief's `source_records`).
4. `get_record` on the meeting's own source record when you need a verbatim line for a
   follow-up. It usually carries the transcript.

Where each piece goes:
- `attendees`: the stakeholder map. Someone listed who did not speak is a finding.
- `problem_statement` and `metrics`: the confirmed problem, in their words, with their numbers.
- `next_steps`: who owes what by when. Each committed step belongs in a follow-up.
- The deal's weakest predictors: what this call did or did not move, for the debrief.
- The top `next_plays` entry: what every follow-up should be pulling toward.

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

You need the `meeting_brief` for this call to do this well. If Loop has no record of the call at
all, say so and ask the seller for their raw notes rather than inventing what was said.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Map the stakeholders

Read `references/frameworks.md` (Stakeholder mapping). For every person on the call, capture:
who they are, what they seemed to care about most, the questions they asked, and any
reaction worth noting. Then chain each person's interest to the metric they own using the
"which means" connector: this user's daily pain, which means this manager's number, which
means this exec's KPI. That chain is what lets one follow-up speak to a whole committee.

## Step 3: Lock the confirmed problem

Read `references/frameworks.md` (Problem Statement). Write the problem back in the buyer's
own words, built from the five elements: Frame, Data, Benchmark, Trajectory, Connection.
Quote them. If a number was never given, do not invent it: write `[MISSING: cost of the
problem not quantified on the call]`. A confirmed problem the buyer recognizes as theirs is
what earns the next meeting.

## Step 4: Surface the skeptics and objections

Note who pushed back and on what, spoken or unspoken, and where the opening is to engage
them. Keep this light here. If a real blocker showed up, the deep work belongs in the
`loop-champion` skill (Targeting the Skeptic). Hand it off with a one-line pointer.

## Step 5: Draft the forwardable follow-ups

Read `references/output-templates.md` and use the two forwardable-email patterns in
`references/frameworks.md` (one for non-technical contacts, one for technical evaluators).
Draft a short follow-up per stakeholder (under 120 words each): reference something specific
they said, tie it to their metric, and give one clear next step. Then a separate champion
debrief message asking their read on how it went and what the logical next step is.

If a recap already went out, do not send another. The next message's job is to arm the people
who were on the call to sell the people who were not. Write through your attendee, to the
decider: hand your attendee the two-sentence version of the case, in the buyer's own words,
ready to forward without editing. That is how you sell the room you were not invited to.

Write these to be forwarded. That means their words, not yours. Camouflage, not a billboard.
No vendor chest-thumping, no jargon, no em dashes.

## Step 6: Debrief the call

Read `references/frameworks.md` (Discovery Lookback). Grade the call across Problem, Process,
Payoff. Name the two or three moments to go deeper next time and the exact reframe that would
have opened them. Not self-criticism, just the list of what to close on the next call.

## The deliverable

The seller walks away with a ready-to-send follow-up pack, built to the skeleton in
`references/output-templates.md`:
1. **Stakeholder map** (who, what they cared about, their metric)
2. **Confirmed problem** (in their words, five elements, gaps flagged)
3. **Skeptics / objections that showed up** (and the opening)
4. **Forwardable follow-up drafts** (one per stakeholder + the champion debrief, ready to send)
5. **Discovery debrief** (graded stages + the reframes to use next time)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Follow-up is selling in the room you are not in.** Write to be forwarded.
- **Their words, not ours.** Camouflage, not a billboard.
- **One recap to one person leaves the committee unsold.** Map them, write to each.
- **Score the call as it went.** The missed reframe is the next call's opening.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/frameworks.md

# Frameworks: Call Follow-Up

## Stakeholder mapping and the "which means" chain

After a call, you are not summarizing. You are mapping. For each person on the call:
- Who they are and their role.
- What they cared about most (from what they said and how they reacted).
- The questions they asked. Questions reveal priorities better than statements.

Then connect each person to the person above them with **"which means"**. This is how you
turn a room full of separate interests into one coherent story:

> The ops user is losing two hours a day to manual work,
> which means the ops manager misses their throughput number,
> which means the VP's cost-per-unit target slips this quarter.

Same problem, three altitudes. A follow-up built on this chain can speak to a user and to
the exec who will approve the deal, without sounding like two different emails.

Not every stakeholder owns a metric, so do not force one. Chain each person to what they are
personally measured on or judged by, and when there is no clean number, name the personal
stake instead: an enablement lead owns whether the message gets adopted, an event owner owns
whether it sticks, a champion owns their own credibility for having backed you. A borrowed KPI
reads generic. The real stake, whether a metric or a reputation, reads true.

## The confirmed problem: five elements

Write the problem back in the buyer's own words so it survives being forwarded. Build it
from five elements, then assemble into prose (not a list):

1. **Frame.** The specific situation you win, narrow enough that they think "that is us."
2. **Data.** A number on it. Never "significant" or "a lot." If it is not quantified, flag
   it as missing.
3. **Benchmark.** Compared to what? Comparative data creates urgency that absolute data
   cannot. "Peers at your stage do X. You are the outlier."
4. **Trajectory.** Why it gets worse with time. A static problem is easy to defer. A
   compounding one demands attention. Name the deadline if there is one.
5. **Connection.** The executive priority it attaches to. Operational problems get
   deprioritized. Problems tied to a funded initiative get funded.

Test: say it out loud. If it sounds like marketing copy, simplify. If it survives three
handoffs without losing its edge, it is ready.

## Skeptics and objections

Note who resisted and on what. Some objections are spoken; the important ones often are
not (the person who went quiet, the evaluator who asked three feasibility questions in a
row). Mark the opening to engage each one. Do not try to resolve them here. If there is a
real blocker, that is a job for the `loop-champion` skill, which owns the
skeptic-conversion playbook. Hand it off.

## Forwardable email patterns

Everything you draft here may get forwarded to someone who was not on the call. The goal of a
forwardable email is to position your champion to run the internal sale: you are writing
through them, to others. Two patterns, picked by who receives it.

**Pattern 1: non-technical contact (economic buyer, exec sponsor).**
- **Subject:** the internal project or priority, in their language. Not your product.
- **Reference a priority:** "[their internal project / trigger] surfaced something worth a look."
- **Build curiosity with a number:** the specific $ / % / # impact on an outcome they own,
  and the timeframe to move it.
- **Be specific, three points:** the root cause and its cost, a quick win, the strategic value.
- **Link the ask to the deal:** the small next step (a pilot, a review), tied to the business case.
- **Sign as the champion** where you are ghostwriting for them.

**Pattern 2: technical evaluator.**
- **Subject:** the technical outcome plus "next steps."
- **Validate their concern:** name the exact objection they raised and why it is fair.
- **Technical bridge, three points:** how the approach protects their responsibility, their
  team, and their own risk.
- **Give control back:** ask what specific criteria or metrics would prove it out, so they
  set the bar.
- **Optional P.S.:** name the cost or risk of waiting for their preferred alternative.

Rules for both: BLUF (the point in the first line), their words not yours (camouflage, not a
billboard), one next step not three, under 120 words, no em dashes, no jargon, no "just
circling back." If it reads like it came from your marketing team, it will not get forwarded.

## The Discovery Lookback

Grade the call so the next one is sharper. For each stage, mark Strong / Adequate / Weak
and name what you would do differently.

**Problem (current state).** Did you lead with insight from their world, or a generic
question? Did you quantify the gap in dollars? Did you test "why now"?

**Process (building a path).** Did you test whether they are serious, or jump to the
solution? Did you ask what must be true of a solution? Did you map who else has to agree?

**Payoff (future state).** Did you make the outcome concrete and numbered? Did you show the
math: cost to act versus value gained? Did you learn whether this is leadership-level?

Then the diagnosis: which stage broke down, what reframing question would have changed the
conversation, and the specific move for next time. The goal is to see where you get stuck so
you can fix it, not to relitigate the call.

## references/output-templates.md

# Output Templates: Call Follow-Up

## The follow-up pack (produce this)

```
# Follow-Up: [Account] - [call/demo] on [date]

## Stakeholder map
| Person | Role | What they cared about | Their metric ("which means") |
|--------|------|-----------------------|------------------------------|
| [name] | [title] | [specific interest / quote] | [the number they own] |

## Confirmed problem (in their words)
[Prose, built from Frame + Data + Benchmark + Trajectory + Connection. Quote them.
Flag any missing element, e.g. [MISSING: no cost figure given].]

## Skeptics / objections that showed up
- [who] pushed on [what]. Opening: [how to engage]. → deep work: loop-champion skill.

## Follow-up drafts
### To [stakeholder 1] - [role]
Subject: [noun phrase, their language]
[Under 120 words. Reference something specific they said. Tie to their metric. One next step.]

### To [stakeholder 2] - [role]
Subject: [...]
[...]

### Champion debrief - to [champion]
[Short. Ask their read on how it landed, what concerns surfaced after you left, and what
they think the logical next step is. Make it easy to reply to.]

## Discovery debrief (for you, not to send)
| Stage | Grade | What to do differently |
|-------|-------|------------------------|
| Problem | Strong/Adequate/Weak | [the reframe you missed] |
| Process | ... | ... |
| Payoff | ... | ... |
Biggest gap to close before next contact: [one thing]
```

## Per-stakeholder email skeletons

Pick the pattern by who receives it (full detail in `frameworks.md`).

**Non-technical contact (economic buyer, sponsor):**
```
Subject: [their internal project / priority, their language]
[Name],
[Their priority] surfaced something worth a look: based on [team]'s review, we found
[$ / % / # impact] on [outcome they own] we can move within [timeframe].
Three points: [root cause is costing X] · [quick win] · [strategic value].
Next step: [small step tied to the business case], with [champion].
[Champion name]
```

**Technical evaluator:**
```
Subject: [technical outcome], next steps
[Name],
Your point on [their objection] resonated, especially given [their experience].
Three details worth emphasizing: [protects their responsibility] · [protects their team] ·
[protects their own risk].
What specific [criteria / metrics] would prove this out for you?
[Champion name]
P.S. [cost or risk of waiting for their preferred alternative]
```

Do not send the same email to five people with the name swapped. Each person should see their
own problem reflected back. That is what gets forwarded.

## Reminders

- Write to be forwarded. Camouflage, not a billboard.
- One next step per message, not a list of asks.
- No em dashes, no jargon, no filler.
