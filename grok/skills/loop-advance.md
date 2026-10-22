---
name: loop-advance
description: >-
  Diagnose why a deal is stuck and get it moving, or build a mutual action plan to
  drive it to close. Use this skill whenever a seller says "why is this deal
  stuck", "this deal stalled", "the deal went quiet", "re-engage a stalled deal",
  "how do I get this moving again", "build a mutual action plan", "MAP", "close
  plan", "work-back timeline", or "write a changed-direction email". It pulls
  context from Loop,
  and runs one of two modes: diagnose a stall and generate re-engagement moves, or
  build a backdated mutual action plan from a compelling event. Prefer this over
  generic "just follow up" advice any time a deal has stalled or needs a plan to
  close.
---

# Deal Advancement

## What this does

Two jobs, one skill, because they are the same problem from two ends: a deal that is stuck, and
a deal that needs a plan so it does not get stuck.

- **Stuck-deal mode:** diagnose where and why it stalled, and generate specific moves to test
  each cause and get it moving. Including the direct "changed direction?" message when nothing
  else works.
- **Mutual-action-plan mode:** build a backdated plan from a real compelling event, with
  milestones, owners, and dates, that the buyer helps you build and validate.

The deliverable is either a diagnosis with re-engagement moves, or a mutual action plan.

## Step 1: Lock the deal and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the deal ("why has the Acme renewal stalled"), filtered to
   `brief_types: ["deal_brief"]`.
2. `get_brief` the `deal_brief`, then the same `entity_ref` with
   `brief_type: "activity_brief"` for the timeline of logged touches.
3. `get_brief` the deal brief again with `covers_through` set 30 to 60 days back. What
   changed between the two versions is where it stalled.
4. `get_brief` the most recent `meeting_brief`s and `email_brief`s for the account.
5. `get_record` on the deal's own source record only for an exact close date, stage, or amount.

Where each piece goes:
- The top `next_plays` entry: the first re-engagement move, or the first MAP milestone.
- The weakest predictors: the seeds of your three root-cause hypotheses.
- `timeline` and the last meeting's `next_steps`: where the momentum actually stopped, and
  which committed step never happened.
- Outstanding `correspondence`: the silence, in their words.
- `metrics` and dates across meeting briefs: the compelling event for a MAP.

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

Set the mode: diagnose a stall, or build a plan to close.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2 (stuck-deal mode): Diagnose

Read `references/frameworks.md` (Stuck-deal diagnosis). Lay out the current state and where it
stalled, from the last few interactions. Then generate 3 root-cause hypotheses, direct: is it
priority, politics, a missing stakeholder, a weak business case, or something else. Sort each
into a solvable problem or drama. For each hypothesis, give one specific move to test it and get
the deal moving. If nothing lands, draft the "changed direction?" message: respectful, direct,
built to get a real answer.

## Step 2 (MAP mode): Build the plan

Read `references/frameworks.md` (Mutual action plan). Start from the compelling event, the one
you discovered with the buyer, never a manufactured deadline. Work backward from their go-live
date through the standard phases (problem statement, business case, proof of value, executive
readout, security, contracting, kickoff), assigning milestones, owners on both sides, and dates.
A mutual action plan is a training plan, not a close plan: it is a plan to solve their problem,
not to sell your software. Then draft the message to your champion asking them to validate the
timeline.

## The deliverable

Produce whichever the mode calls for, using the skeletons in `references/output-templates.md`:

**Stuck-deal diagnosis:**
1. **Deal breakdown** (current state, where it stalled)
2. **Root-cause hypotheses** (3, each sorted solvable vs drama)
3. **Re-engagement moves** (one specific move per hypothesis)
4. **Changed-direction message** (the direct last-resort email)

**Mutual action plan:**
1. **Success criteria** (their top payoffs)
2. **Compelling event** (discovered, with the date)
3. **Milestones** (backdated by phase, with owners and dates)
4. **Alignment message** (to the champion, to validate the plan)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **A stall is a math problem or drama.** Solve the math; name the drama.
- **The number one competitor is no decision.** Rebuild momentum, do not just chase.
- **A MAP is a training plan, not a close plan.** It solves their problem, not your quota.
- **Backdate from a real compelling event.** Discovered with the buyer, never manufactured.
- **When stuck, get a real answer.** A clean no beats a slow maybe.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/frameworks.md

# Frameworks: Deal Advancement

## Stuck-deal diagnosis

The number one competitor in any pipeline is no decision. Deals rarely die to a rival; they die
to inertia and irrelevance. So a stall is a signal to diagnose, not a reason to chase harder.

**Where did it stall?** Read the last few interactions. Momentum has a shape: title level of
who you are talking to, times the number of buyer interactions, times deal stage, over the
weeks it has taken. When that stops climbing, name the point it stopped.

**Root cause: solvable problem or drama.** Generate three hypotheses and sort each:
- **A solvable problem has a next step.** Missing stakeholder, no written business case, an
  unvalidated ROI, a priority that outranks yours. Go get the missing piece.
- **Drama has no next step** because it protects something: someone's job, a past decision, a
  turf line. A better deck does not move it. Name the drama, then connect solving the underlying
  problem to the need the drama protects.

Be direct about which it is. Consider priority, politics, a missing stakeholder, a weak business
case, or a compelling event that never existed. Then, for each hypothesis, one specific move to
test it, not generic advice.

**The change equation.** A deal moves again when dissatisfaction with today, times a vision of
the after, times an easy first step, beats the resistance to changing. If it is stuck, one of
those three is low. Raise it.

**The "changed direction?" message.** When nothing else lands, ask for the truth respectfully. A
clean no is worth more than a slow maybe, because a slow maybe sits in your forecast and burns
your quarter. Keep it short, remove the pressure, and make it easy to say where things really
stand.

## Mutual action plan

A mutual action plan is the how (the project plan). The business case is the why. You need both,
and the why comes first. The plan is a training plan, not a close plan: it is a plan to solve
their problem, not to sell your software. Say that out loud to the buyer and it changes how the
plan lands.

**Start from the compelling event.** Discovered with the buyer, never manufactured. Their fiscal
deadline, a product launch, a contract expiry, a board meeting. If there is no event, the plan
has no gravity.

**Backdate from go-live.** Work backward through the phases, assigning milestones, owners on both
sides, and dates:
- Problem statement (built with their data, group input and feedback)
- Business case built
- Proof of value (share demo data, calculate ROI)
- Executive readout (review POC data, share final report)
- Security and compliance (audit, documentation)
- Contracting (pricing, legal, finance, execution)
- Kickoff and implementation date

**Use it as a diagnostic, not an admin tool.** The plan surfaces friction: a chronic ball-dropper,
a step that keeps slipping, a stakeholder who has not engaged. Set a cutoff time together early,
and use it to disqualify gracefully when the buyer will not move. Then ask your champion to
validate the timeline, framed as helping them hit their goals.

## references/output-templates.md

# Output Templates: Deal Advancement

## Stuck-deal diagnosis (produce this)

```
# Stuck-Deal Diagnosis: [Account] - [deal]

## Deal breakdown
Current state: [stage, close date, last activity]. Stalled at: [the point momentum dropped].
Last interactions: [what the last few exchanges showed].

## Root-cause hypotheses
1. [Hypothesis] - solvable / drama - test: [one specific move to run].
2. [Hypothesis] - solvable / drama - test: [...].
3. [Hypothesis] - solvable / drama - test: [...].

## Re-engagement moves (in priority order)
- [The move most likely to move it, and why].

## Changed-direction message (last resort)
Subject: [short, low-pressure]
[Name], I do not want to keep chasing if the timing has moved. Totally fine if [priority] took
over. If it makes sense to pick this back up later, just say the word. And if it is off the
table for now, that is useful for me to know too.
[Rep]

## Open gaps
- [MISSING: ...]
```

## Mutual action plan (produce this)

```
# Mutual Action Plan: [Account] - [deal]
This is a plan to solve [their problem], worked back from [go-live date].

## Success criteria (their payoffs)
- [Payoff 1] · [Payoff 2] · [Payoff 3]

## Compelling event
[The event discovered with the buyer] on [date]. Why it matters: [what happens if missed].

## Milestones (backdated)
| Phase | Milestone | Owner (buyer / you) | Start | End | Done? |
|-------|-----------|---------------------|-------|-----|-------|
| Problem statement | built with their data | [owner] | | | |
| Business case | drafted and reviewed | | | | |
| Proof of value | demo data, ROI | | | | |
| Executive readout | final report | | | | |
| Security / compliance | audit, docs | | | | |
| Contracting | pricing, legal, finance | | | | |
| Kickoff | implementation date | | | | |

## Alignment message (to the champion)
[Short note presenting the plan, asking them to validate the timeline, framed as helping them
hit their goal. One easy next step.]
```

## Reminders

- Sort every stall into solvable or drama before proposing a move.
- A MAP without a real compelling event has no gravity. Find the event first.
- Frame the MAP as solving their problem, not closing your deal.
- No em dashes, no jargon.
