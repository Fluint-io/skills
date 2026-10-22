---
name: loop-multithread
description: >-
  Map the real buying committee on an account or deal and get multithreaded
  across it. Use this skill whenever a seller says "multithread this account",
  "map the buying committee", "who else should I be talking to at [account]",
  "this deal is single-threaded", "widen this deal", "get more people involved",
  "map the stakeholders", "build the org chart for this deal", or is riding a deal
  on one contact that needs more coverage. It works from two starting points: a
  brand-new account with no coverage, or an existing live deal running on a single
  thread that needs to be widened before it stalls. It pulls context from Loop, maps the committee by
  role, writes a value hypothesis per stakeholder, and drafts the outreach to
  reach each one. Prefer this over guessing who to email next any time a deal
  depends on more than one person.
---

# Multithread

## What this does

Single-threaded deals are the highest-risk deals in the pipeline. One person gets promoted,
goes quiet, or gets overruled, and the deal dies. This skill widens the coverage:

1. Maps the real buying committee: who decides, who they listen to, who would block this.
2. Writes a value hypothesis per stakeholder, tied to the metric that person owns.
3. Drafts the outreach to reach each one, easy for a champion to forward.
4. Sequences it: who to reach first, and who to reach through the champion versus direct.

Two starting points, same map:
- **New account:** no coverage yet. You are choosing 3 to 5 entry points cold.
- **Existing deal, single-threaded:** you have one contact. You are widening through them
  before the deal stalls on one person.

The deliverable is a multithreading plan the seller can act on today.

## Step 1: Lock the target and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the account and the people ("who have we talked to at Acme").
2. `get_brief` each `deal_brief` at the account.
3. `get_brief` the `meeting_brief`s and `email_brief`s, to see who has actually been in the
   conversation.
4. `get_record` only for a contact detail a brief names but does not spell out.

Where each piece goes:
- `attendees` across every meeting brief: the real thread count. One name across every call is
  a single-threaded deal, whatever the CRM says.
- The economic-buyer-access and decision-process reasoning: who is missing from the committee.
- `problem_statement` and `metrics` per meeting: the value hypothesis per stakeholder.
- The top `next_plays` entry: who to reach first.

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
https://raw.githubusercontent.com/Fluint-io/uncommon-sales-skills/main/INSTALL.md.
Do not fall back to any other tool.

Set the entry point: new account, or an existing deal riding on one thread. If existing,
identify the single contact you have and whether they are a champion (see below).

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Map the buying committee

Read `references/frameworks.md` (Buying committee + shadow org). Map the real decision
structure, not the org chart. Identify 3 to 5 people across the roles that recur: Champion,
Economic Buyer, Technical Evaluator, Internal Skeptic, and the SLIP stakeholders (Security,
Legal, IT, Procurement) who can stall a deal late. For each, capture their likely role in the
decision and what they care about most.

## Step 3: Write a value hypothesis per stakeholder

Read `references/frameworks.md` (which-means). For each person, write one sentence that would
land with their specific priorities, tied to what is happening at the account right now. Not
generic. Chain it to their metric: this user's pain, which means this manager's number, which
means this exec's KPI.

## Step 4: Draft the outreach

Read `references/output-templates.md` and use the exec-level multithreading email patterns.
Draft a short message per stakeholder, under 100 words, leading with relevance. For a new
account, these are entry points. For an existing deal, use invitational language to widen
through your champion ("is this a focus for them? I will loop them in for feedback"). Keep the
tone easy to forward, so a buyer-side exec can pass it across their team.

## Step 5: Prioritize and sequence

Recommend who to reach first and why, then how to sequence the rest by likelihood to engage
and strategic value. Note who you approach directly versus through the champion. Two rules
from the frameworks: confirm at least three independent conversations before presenting to a
group, and never run pricing in a group.

## The deliverable

Produce the multithreading plan using the skeleton in `references/output-templates.md`:
1. **Buying-committee map** (name, role, real influence, disposition, contact status)
2. **Value hypothesis per stakeholder** (the one-line soundbite tied to their metric)
3. **Drafted outreach** (one short message per stakeholder, ready to send)
4. **Sequence** (who first and why, direct vs through the champion)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Single-threaded is the highest-risk deal you have.** Widen before it stalls.
- **Map communication flow, not the org chart.** Influence, not title.
- **Three conversations before any group meeting.** No surprises in the room.
- **Never run pricing in a group.** Some conversations are one-on-one only.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
