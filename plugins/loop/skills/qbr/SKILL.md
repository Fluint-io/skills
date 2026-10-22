---
name: qbr
description: >-
  Prep a quarterly business review with a customer: surface the value delivered,
  the risks, and the expansion openings, then build the agenda. Use this skill
  whenever a seller or account manager says "prep for my QBR", "quarterly business
  review", "build a QBR agenda", "customer review prep", "renewal review", "prep
  my check-in with [account]", or is getting ready to sit down with an existing
  customer to review the relationship. It pulls context from Loop, ties the value delivered back to their
  original goals, assesses risk from engagement and outcome signals, finds the
  expansion openings, and drafts an agenda that leads with their success. This is
  customer-facing (the QBR is with the buyer), distinct from an internal deal
  review. Prefer this over a generic status-deck outline any time a customer review
  is coming up.
---

# QBR Prep

## What this does

A quarterly business review is a chance to prove value, get ahead of risk, and open the next
expansion, or a status deck nobody remembers. This skill builds the first kind:

1. Ties the value you delivered this quarter back to the goals they bought for.
2. Assesses the risks going in: low engagement, missed goals, competitive threats.
3. Finds the expansion openings: new use cases, teams, and problems.
4. Drafts an agenda that leads with their success and opens the door to more, without a pitch.

This is a customer-facing review with the buyer, distinct from an internal forecast or deal
review (for that, use the `loop:manage-up` skill). The deliverable is a QBR pack the seller can
walk the customer through.

## Step 1: Lock the account and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the account ("Acme: what they bought, results so far, risks ahead
   of the QBR").
2. `get_brief` the `deal_brief` for the original purchase and any renewal or expansion deal.
3. `get_brief` the same deal with `covers_through` at the close date: what they bought for,
   in their words at the time.
4. `get_brief` the `meeting_brief`s and `email_brief`s since then, newest first.
5. `get_record` only for a contract date or amount.

Where each piece goes:
- `metrics` and `problem_statement` at purchase: the goals the value has to tie back to.
- `metrics` in recent meetings: the results, in their numbers.
- `attendees` over time: engagement. A champion who stopped showing up is the first risk.
- The renewal deal's weakest predictors and top `next_plays` entry: the risk to address and
  the move to make.

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
- **There is no account brief.** Loop briefs deals, calls, threads, and activity, not
  companies. Build the account view from every `deal_brief`, `meeting_brief`, and
  `email_brief` that `find_briefs` returns for the account name.

**Loop not connected?** Stop and tell the seller to connect it before going further: in
Claude Code run `/mcp` and authenticate `loop`, or follow
https://raw.githubusercontent.com/Fluint-io/skills/main/INSTALL.md.
Do not fall back to any other tool.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Value delivered

Read `references/frameworks.md` (Value tied to their goals). Summarize the value delivered this
quarter, and tie each win back to the original goals and success criteria they bought for. A win
they do not connect to a goal they care about is a feature, not value. Use their metrics.

## Step 3: Risk assessment

Read `references/frameworks.md` (Risk signals). Name the risks going into the review: low
engagement, missed goals, a quiet champion, a leadership change, a competitive threat. Back each
with evidence from behavior, not a hunch. Better to name a risk yourself and bring a plan than to
have the customer raise it.

## Step 4: Expansion openings

Read `references/frameworks.md` (Expansion). Identify the expansion opportunities: new use cases,
adjacent teams, problems you have not solved yet. Rank by impact and ease. The strongest opening
is usually a new executive with a new mandate, or a proven outcome you can extend to a next team.

## Step 5: Build the agenda

Read `references/output-templates.md`. Draft a QBR agenda that leads with their success,
addresses any risk proactively, and opens the expansion conversation, without turning into a
sales pitch. Lead with them, not with you.

## The deliverable

Produce the QBR pack using the skeleton in `references/output-templates.md`:
1. **Value delivered** (wins tied to their original goals, in their metrics)
2. **Risk assessment** (the risks, with behavior evidence and a plan for each)
3. **Expansion openings** (ranked, with who to engage)
4. **QBR agenda** (leads with their success, addresses risk, opens expansion)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Lead with their success, not your roadmap.** The review is about their outcomes.
- **A win they do not connect to a goal is a feature.** Tie value to what they bought for.
- **Name the risk before they do.** Bring the risk and the plan together.
- **Open expansion, do not pitch it.** The next use case, framed as their next outcome.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
