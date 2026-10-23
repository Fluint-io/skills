---
name: advance
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

**Loop not connected?** Stop and tell the seller to connect it before going further: in
Claude Code run `/mcp` and authenticate `loop`, or follow
https://raw.githubusercontent.com/Fluint-io/skills/main/INSTALL.md.
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
