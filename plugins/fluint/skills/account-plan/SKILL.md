---
name: account-plan
description: >-
  Build a point of view and a strategic account plan for a target account, or
  find and rank expansion opportunities inside an existing one. Use this skill
  whenever a seller says "build an account plan", "give me a POV on [account]",
  "account strategy for [account]", "find expansion in this account", "where can
  we grow this account", "whitespace at [account]", "what's our plan for this
  account", or is preparing to go after a new logo or grow a current customer. It
  pulls context from Loop, builds a POV on what is changing, maps the stakeholders and the
  opportunities by executive priority, and drafts the first outreach. Prefer this
  over a blank-page account plan any time a seller needs a strategy for winning or
  growing an account.
---

# Account Planning

## What this does

Turns an account into a plan you can run: a point of view on what is changing, the
opportunities ranked by executive priority, the stakeholders who own them, and the first
message to build momentum.

Two modes, same plan:
- **New target account:** build the POV and the opening plan to break in.
- **Existing account:** find the whitespace (adjacent teams, new initiatives, unaddressed
  problems) and rank where to grow next.

The deliverable is a strategic account plan plus a first outreach message.

## Step 1: Lock the target and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the account ("Acme: who uses us, what is changing, where is the
   whitespace").
2. `get_brief` every `deal_brief` at the account, open and closed.
3. `get_brief` the `meeting_brief`s and `email_brief`s, newest first.
4. `get_record` only for a contract amount or date a brief names but does not spell out.

Where each piece goes:
- `problem_statement` and `metrics` across meetings: the POV. What is changing is whatever
  they keep raising.
- `attendees` across meetings: key contacts, and the teams you have never met (stakeholder
  whitespace).
- Deal summaries: current footprint, what they bought, and what is still open.
- The top `next_plays` entry on any open deal: the opportunity already in motion.

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

Set the mode: new account, or expansion in a current one.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Build the POV

Read `references/frameworks.md` (POV + strategic vision). Find what is changing at the
account in the briefs, the problems and numbers they keep raising across meetings, that
creates a greater need for what you do. Write the point of view: the shift, the
recommended strategy you uniquely enable, the outcomes they unlock, and the cost they avoid.
Add the 3-year, board-level vision you are guiding them toward. Lead with a real signal from the briefs, not a
generic claim. If there is none, flag it `[MISSING: ...]`.

## Step 3: Map stakeholders and the compelling event

Identify the top contacts to target, their org influence, and their #1 goal, with a short
value soundbite for each. Name the compelling event: the executive pushing a strategic goal,
the internal project supporting it, the milestone and date they are working toward.

## Step 4: Build the opportunity map

Read `references/frameworks.md` (Opportunity map + whitespace). Lay out the top 2 to 3
opportunities, each tied to an executive priority, with: why change / why now, their current
state, the use case and your right to win, the future-state outcome, and a high-level plan
(key influencers, intros needed). For an existing account, rank by impact and ease of entry,
and check the three whitespace signals: product whitespace, stakeholder whitespace, and
customer-health signals.

## Step 5: Draft the first outreach

Draft the first message based on the top opportunity, built to be forwarded. For expansion,
draft the champion ask: a short note asking your existing champion to introduce you to a new
stakeholder, easy for them to forward.

## The deliverable

Produce the account plan using the skeleton in `references/output-templates.md`:
1. **POV** (the shift, the strategy, the outcomes) plus the strategic vision
2. **Compelling event** (the executive priority, the project, the date)
3. **Key contacts** (org influence, #1 goal, soundbite)
4. **Opportunity map** (top 2 to 3 by exec priority, ranked for expansion)
5. **First outreach** (the opening message, or the champion intro ask)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Lead with what is changing.** A problem matters when it blocks a priority they own.
- **Rank by exec priority, not by product fit.** Follow the money and the mandate.
- **Right to win, stated plainly.** Why you, for this use case, at this account.
- **Every plan ends in a first move.** The plan is worthless without the outreach.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
