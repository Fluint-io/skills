---
name: business-case
description: >-
  Build a customer-specific 1-Page Business Case for a live sales deal. Use this
  skill whenever the user says "business case": including "build a business
  case", "write the business case for [account]", "turn this deal into a
  business case", "help me justify this deal to their exec team", or "make a
  1-pager for [company]". Also trigger when a user wants to summarize a deal into
  an executive-ready justification, arm a champion with something forwardable,
  score how strong a deal's business case is, or find the gaps blocking a deal
  from advancing. The skill pulls context from Loop; drafts the case in the customer's own language;
  scores it against a 5-part rubric to expose gaps; and prescribes creative next
  actions to advance the cycle. Prefer this skill over freehand writing any time
  the phrase "business case" appears in a sales or deal context.
---

# The 1-Page Business Case

## What this does

Turns the scattered evidence of a live deal, as Loop has briefed it (CRM fields, calls,
email threads), into a single, executive-ready **1-Page Business Case** written
in *the customer's own words*, then **scores it against a rubric** so the user can
see exactly where the deal is thin, and **prescribes the next action** that turns
the document into a tool for advancing the cycle.

The output is not marketing copy. A great business case is something a champion
can forward to their economic buyer with a one-line intro and have it land. It
reflects the buyer's language, their metrics, their priorities: not the vendor's
pitch. Your job is to be a faithful scribe of what the customer has already said,
structured into a shape that travels.

Work through the five steps below in order. Don't skip the context-gathering step
:  a business case invented from the vendor's imagination is worse than useless,
because it teaches the champion nothing and exposes them if they forward it.

---

## Step 1: Identify the deal

Before anything else, pin down **which account/deal** this is for.

- If the user named the company in their message, use that.
- Otherwise, ask: *"Which account or deal is this business case for?"*
- Then resolve the exact deal: `find_briefs` on the account name and pick the
  `deal_brief`. Confirm the match
  with the user (e.g. *"Found the Acme Corp: Expansion deal, $120k, Stage:
  Evaluation, owner Jordan. Right one?"*) before pulling everything else.

Resolving the real deal matters because every downstream step keys off it: the meeting and
email briefs you read next all hang off that deal.

## Step 2: Gather all available context

The strength of the business case is capped by the evidence behind it.

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the deal ("Acme deal: the problem, the numbers, who has to sign
   off").
2. `get_brief` the `deal_brief`.
3. `get_brief` the `meeting_brief`s and `email_brief`s where the buyer stated the problem, a
   number, or a deadline.
4. `get_record` on a meeting's own source record for a verbatim quote, or on the deal's own
   record for the exact amount and close date.

Where each piece goes:
- `problem_statement` across meetings: the Problem Statement, in their words.
- `metrics`: the numbers in Target Outcomes and the cost of the problem.
- The pain, metrics, economic-buyer, decision-criteria, and paper-process reasoning: what is
  capping each rubric section.
- The top `next_plays` entry: the first next action you prescribe.

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

While reading, mine specifically for the raw material each section needs (see the
extraction checklist in `references/framework-template.md`). Capture **verbatim
quotes** wherever a customer states a problem, a number, a goal, or a deadline : 
these become the spine of the case and its credibility.

> **Preserve their language.** This is the rule that makes or breaks the output.
> If the buyer says "release trains" don't write "deployment cycles." If they call
> it "the churn fire drill," use that. When you swap their words for polished
> vendor vocabulary, the champion no longer recognizes their own world in the
> document and it stops being forwardable. Quote them.

If Loop has no brief for part of the story (no calls briefed, no deal brief yet), note it and continue. It becomes a flagged gap in the scorecard, not a blocker, and every gap gets the single highest-leverage move to close it: the one question, to the one person, at the next touchpoint.

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the economic buyer or sponsor is absent or untouched, that is the headline, not a footnote.

## Step 3: Draft the 1-Page Business Case

Read `references/framework-template.md` and build the case using that exact
structure. The six components are:

1. **Priority-Driven Headline**: one executive line, tied to a named initiative,
   timebound, sponsored.
2. **Headline formula**: *Because of [shift], we should [approach] by [timeline].
   After, we'll avoid [negatives] while unlocking [positives].*
3. **Problem Statement**: a measured, worsening, high-cost problem with named
   stakeholders.
4. **Recommended Approach**: the capabilities required (vendor-agnostic first),
   then the transition to why this vendor fits.
5. **Target Outcomes**: before/after for daily users + a 3-row executive KPI
   table.
6. **Required Investment**: who invests what, by when, anchored to a go-live event.

**Keep every section concise.** One page means one page. Each section is a few
tight sentences or a short table, not an essay. Executives skim; density kills.

**Handle missing inputs with placeholders, never invention.** When the evidence
doesn't support a section: no quantified cost, no named sponsor, no validated KPI
:  insert a clearly bracketed placeholder like `[MISSING: quantified cost of the
problem: not stated on any call]` rather than fabricating a plausible number.
Placeholders are honest, and they double as the deal's to-do list. A confident
made-up metric is the fastest way to get a champion embarrassed in front of their
CFO.

Present the full draft in the chat as clean, copyable markdown.

## Step 4: Score it against the rubric

Read `references/scorecard-rubric.md` and score the draft. Each of the **five
sections gets a 1-5** against its rubric, and the total rolls into a **readiness
percentage** (sum ÷ 25).

Present the score as a table, and for every section below a 5, name **the specific
missing input** that's holding the score down: tie it back to what wasn't found in
Step 2. The point isn't the grade; it's converting each gap into a concrete thing
the user can go get.

```
| Section              | Score | What's capping it |
|----------------------|-------|-------------------|
| Priority Headline    | 3/5   | No executive sponsor named on any call |
| Problem Statement    | 2/5   | Cost of problem never quantified |
| Recommended Approach | 4/5   | Security/IT sign-off not yet confirmed |
| Target Outcomes      | 2/5   | KPIs are vendor estimates, not customer-validated |
| Required Investment  | 3/5   | Go-live not anchored to a critical event |
| **Readiness**        | **56%** | |
```

## Step 5: Prescribe the next action

This is where the document becomes an *asset*, not a artifact. Read
`references/next-actions-playbook.md` and recommend **1-3 specific next moves**,
prioritized by the **lowest-scoring section**: because the biggest gap is usually
the biggest lever on the deal.

Be prescriptive and creative. Don't say "gather more info." Say *which* play,
*with whom*, *why it advances the cycle*, and give the user the actual asset to do
it: a drafted data-request email, a co-editing agenda, a forwardable version with
a one-line champion intro. The playbook has a menu of plays mapped to each type of
gap; use it to make the recommendation concrete and immediately actionable.

## Step 6: Offer the deliverable formats

The draft lives in chat for live editing. Once the user is happy, offer to export a
formatted **1-page `.docx`** they can forward. Use the `docx` skill to generate it,
matching the framework layout (headline, sections, KPI table). Keep placeholders
visible in the export unless the user has filled them: a champion filling in
`[MISSING: ...]` on a shared doc is itself a multi-threading move.

---

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Scribe, not spin.** Your credibility is the customer's own words. Quote,
  don't paraphrase into vendor-speak.
- **Gaps are the product.** The scorecard and placeholders exist to show the user
  what to go get. A 56% case with a clear next action beats a 90% case built on
  invented numbers.
- **One page, always.** Concision is the format. If a section is running long,
  it's carrying detail that belongs in an appendix, not the case.
- **Every output ends in a move.** Never leave the user with just a document. Leave
  them with a document *and* the specific next thing to do with it.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
