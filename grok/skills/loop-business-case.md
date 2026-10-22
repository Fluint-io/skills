---
name: loop-business-case
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

**Loop not connected?** Stop and tell the seller to connect it before going further: in Grok add it at grok.com/connectors (New Connector, then Custom, URL `https://mcp.fluint.io/mcp`), or follow
https://app.fluint.io/install.
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

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/framework-template.md

# The 1-Page Business Case: Framework Template

Build the case in this exact structure. Keep the whole thing to one page: each
section is a few tight sentences or a short table. The bracketed prompts show what
each field needs; replace them with the customer's own words and numbers, or with a
flagged `[MISSING: ...]` placeholder if the evidence isn't there.

---

## Title
> **[A priority-driven, executive-level headline goes here.]**
>
> Developed by: [ Champion Name ], [ Key Deal Players ]

The title is the one line an executive reads first. It should name the stakes, not
the product.

## Headline (the one-line thesis)

Use this formula verbatim as the skeleton:

> **Because of [ this change / shift ], we should [ follow a recommended approach ]
> by [ timeline ]. After, we'll avoid [ negative outcomes ] while unlocking
> [ positive outcomes ].**

This single sentence has to stand on its own if it's the only thing forwarded.

## The Problem Statement

Describe what's changed that created an emerging, high-cost, high-priority problem
that's getting worse. Include *who's* impacted and how it hits a company-wide goal.
Use one of these proven formats:

> Every [ frequency ], at least [ reach ] are affected by [ problem ], costing us
> [ cost ]. If that's not addressed by [ timing ], then [ it gets worse ].

or:

> Despite trying [ failed solution ], our team still can't [ desired outcome ]
> because [ problem ], which has cost us [ cost of problem ].

## Recommended Approach

Outline the solution design, how it's been tested/proven, and the factors that must
be true for it to work. Include a short note on good-fit customers and proof points.

Sequence matters: **first get agreement on the approach agnostic of vendor**, then
transition with *"we found [ your company ] meets / exceeds all requirements,"* tied
back to your differentiators. Leading with the vendor makes it a pitch; leading with
the required capabilities makes it a shared conclusion.

## Target Outcomes

Paint a vivid before-vs-after for daily users, then show time-to-impact on
executive-level metrics in a table:

| Key Metric      | Current Measure | Target by [ Date ] |
|-----------------|-----------------|--------------------|
| Executive KPI #1 | X               | XX  (+Y%)          |
| Executive KPI #2 | X               | XX  (+Y%)          |
| Executive KPI #3 | X               | XX  (+Y%)          |

The narrative half builds emotion; the table half gives the CFO something to
underwrite. Both are needed.

## Required Investment

Who needs to invest what, by when? List time and people resources, with relevant
scenarios as part of the commercials + go-live plan. Anchor the go-live date to a
customer-provided *critical event*, and back-date the steps required to hit the
customer's outcome from that date.

---

## Extraction checklist: what to mine from context (Step 2)

As you read the Loop briefs and their source records, hunt specifically for these. Capture
verbatim quotes and note the source (which call/email/field) so claims stay
defensible.

**For the Headline / Title**
- [ ] A named internal initiative, project, or company priority the deal ladders up to
- [ ] A critical event or deadline creating urgency
- [ ] An executive sponsor / economic buyer by name and title

**For the Problem Statement**
- [ ] The customer's own description of the problem (quote it)
- [ ] Any metric quantifying its cost/frequency/reach: validated by the customer
- [ ] Who is impacted, and whether multiple people have voiced it (consensus)
- [ ] Evidence the problem is worsening over time
- [ ] Multiple levels of impact (individual → team → company goal)

**For the Recommended Approach**
- [ ] The high-priority capabilities the customer said they require
- [ ] How those map to your differentiators
- [ ] Which stakeholders have weighed in (end users through Security/IT/Procurement)
- [ ] Alternatives the customer considered and why they were ruled out

**For Target Outcomes**
- [ ] Specific outcome metrics the customer cares about
- [ ] Current-state baselines vs target future-state numbers (customer-validated)
- [ ] Applicable scenarios / sensitivities (best/expected case)
- [ ] Emotive, vivid language from the customer about the future state: beyond "ROI"

**For Required Investment**
- [ ] Budget / commercials and whether the budget owner + procurement have signed off
- [ ] People resources reserved for rollout
- [ ] A go-live date tied to a customer-provided critical event
- [ ] The back-dated sequence of steps to reach the outcome

Anything you can't find becomes a `[MISSING: ...]` placeholder and a scorecard gap.

## references/next-actions-playbook.md

# Next-Actions Playbook

The business case is only worth the *move it triggers*. This playbook turns the
scorecard into action: find the lowest-scoring section, pick the play that closes
that gap, and hand the user the actual asset to run it. Recommend **1-3 plays**,
lowest-scoring gap first: that's the biggest lever on the deal.

For every play, give the user four things: **the play, who it involves, why it moves
the cycle, and the asset** (a drafted email, an agenda, a forwardable version). Don't
describe the move: *build* the move.

---

## Universal plays (work on almost any case)

**1. Live co-edit on the next call.**
Screenshare the draft and fill the `[MISSING: ...]` placeholders *together* with the
champion. Why it works: it converts a monologue into a mutual document, and every
blank you fill live is a discovery question that surfaces the next stakeholder. The
placeholders become your agenda. → *Asset: a short call agenda ordered by the
lowest-scoring sections.*

**2. Arm the champion to forward it.**
Package a clean version plus a one-line intro the champion can paste when forwarding
to their economic buyer or exec sponsor. Why it works: champions rarely forward
because writing the framing is friction: remove the friction and the case travels
internally without you in the room. → *Asset: the forwardable doc + a drafted
2-sentence champion intro in the champion's voice.*

**3. Use it as the deal's Mutual Action Plan spine.**
The Required Investment section already back-dates steps from go-live; turn that into
a shared, dated checklist owned jointly. Why it works: it makes the timeline the
customer's, not yours, and gives you a legitimate reason for recurring contact. →
*Asset: the back-dated step list as a checklist with owners and dates.*

---

## Gap-specific plays

### If the Priority Headline is weakest (no initiative / no sponsor / no date)
- **Sponsor-mapping ask:** *"Whose top-3 priority list does this sit on this year?"*
  Get a name. Why: an unsponsored case dies in procurement. → *Asset: a drafted
  message to the champion asking who the executive owner is and why.*
- **Initiative-anchoring:** tie the headline to a public or stated company initiative
  (from the 10-K, an all-hands, a press release, or something said on a call). → *Ask
  the user if they want a quick research pass to find the initiative to anchor to.*

### If the Problem Statement is weakest (unquantified / single voice)
- **The data request** (highest-leverage play in the deck): send the champion a tiny,
  specific request for the *number* that quantifies the problem: not a survey, one
  metric. Why: it forces the customer to build your business case for you, and pulling
  the number usually requires them to loop in the person who owns it (multi-threading
  for free). → *Asset: a drafted 3-line data-request email naming the exact metric and
  why it helps them.*
- **Consensus check:** *"Who else feels this pain daily?"* → turn one voice into three.
  → *Asset: a drafted intro-request message.*

### If the Recommended Approach is weakest (no sign-off / alternatives open)
- **Requirements-first pre-read:** send the vendor-agnostic capability list to
  Security/IT/Procurement *before* the vendor conversation, to get the required-
  capabilities agreed as a neutral standard. Why: winning the criteria wins the deal.
  → *Asset: the capabilities section extracted as a standalone requirements checklist.*
- **Bury the alternative:** name the alternative the customer is weighing and add the
  one line that rules it out, in their words. → *Draft the ruling-out sentence.*

### If Target Outcomes is weakest (vendor estimates, not validated)
- **KPI validation with the economic buyer:** take your 3 KPIs to the buyer and ask
  *"are these the numbers your board would care about, and are our baselines right?"*
  Why: a KPI the buyer edited is a KPI the buyer owns. → *Asset: a drafted message
  presenting the KPI table for their validation.*
- **Before/after in their voice:** pull a vivid future-state quote from a call to
  replace generic benefit language. → *Surface the candidate quotes.*

### If Required Investment is weakest (no critical event / no procurement)
- **Anchor to a critical event:** find the customer deadline that go-live must beat
  (fiscal year, product launch, contract expiry, board meeting) and back-date from it.
  Why: urgency the customer owns beats end-of-quarter pressure they don't. → *Asset: a
  drafted question to surface their critical event.*
- **Procurement pre-wire:** get the budget owner + procurement contact named and
  looped early. → *Asset: a drafted message asking the champion to introduce procurement.*

---

## Framing the recommendation

Lead with the *why now*: "Your case is at 56%: the thing capping it most is the
Problem Statement, because the cost was never quantified. The single highest-leverage
move is [the data request], because it makes the customer build the number for you and
naturally pulls in the person who owns it. Here's the email: want me to tailor it?"

Then offer to execute: draft the asset, tailor the tone to the account, or export the
`.docx`. Always end on a concrete offer, never a shrug.

## references/scorecard-rubric.md

# Business Case Scorecard: Rubric

Score each of the **five sections 1-5** against the ladders below. Pick the highest
level the draft *fully* satisfies: if it meets some but not all of a level's
criteria, it scores at the level below. Then compute readiness.

**Readiness % = (sum of the five section scores) ÷ 25**

(Each section maxes at 5; five sections → 25 points → expressed as a percentage,
matching the source scorecard where `total = (SUM(scores)/5)/5`.)

A 5 in every section is the definition of a fully-built, forwardable, exec-ready
case. Most live deals score far lower: that's expected and useful. The gap between
the current score and 5 *is the deal plan*.

---

## 1. Priority-Driven Headline

Target (5/5): Aligned to an existing business initiative or project. Timebound with
a critical event date. Executive sponsor identified.

- **1**: Generic headline with no clear business focus or urgency.
- **2**: Mentions a business initiative but lacks specifics. No timeframe or sponsor.
- **3**: Aligned to a business initiative but lacks either timeframe or sponsor.
- **4**: Aligned to a business initiative with either a timeframe or a sponsor
  identified, but not both.
- **5**: Aligned to an existing initiative. Timebound with a critical event date.
  Executive sponsor identified.

## 2. Problem Statement

Target (5/5): Measured, high-cost problem with customer-validated metrics.
Who's-impacted identified with consensus from multiple people. Framed around
multiple levels of impact. Getting worse with time.

- **1**: Vague problem description without any metrics or stakeholder identification.
- **2**: Minimal metrics. No clear stakeholder identification or consensus.
- **3**: Some metrics, but not customer-validated. Limited stakeholder ID. No
  multi-level impact framing.
- **4**: Customer-validated metrics. Stakeholders identified but lacking full
  consensus. Some multi-level framing. No indication of worsening over time.
- **5**: Customer-validated metrics. Impact identified with consensus from multiple
  people. Multiple levels of impact. Problem is getting worse with time.

## 3. Recommended Approach

Target (5/5): High-priority required capabilities align with competitive
differentiators. Sign-off from everyone across end users through Security/IT/etc.
Alternatives openly discussed and ruled out.

- **1**: Generic solution, no alignment to specific capabilities or differentiators.
  No stakeholder input.
- **2**: Some capabilities mentioned but not tied to priorities. Limited stakeholder
  input. No discussion of alternatives.
- **3**: Priority capabilities mentioned but not clearly tied to differentiators.
  Some stakeholder input, not comprehensive. Brief mention of alternatives.
- **4**: High-priority capabilities aligned with some differentiators. Input from
  most key stakeholders, but not all. Alternatives discussed but not thoroughly
  ruled out.
- **5**: Required capabilities align with competitive differentiators. Sign-off from
  everyone (end users → Security/IT). Alternatives openly discussed and ruled out.

## 4. Payoff / Target Outcomes

Target (5/5): Specific outcome metrics identified. Customer-validated change from
current to future state. Applicable scenarios and sensitivities labeled. Vivid
language building emotion beyond "ROI."

- **1**: Generalized benefits, no specific metrics or validation. No scenarios.
- **2**: Some outcome metrics but not specific or customer-validated. No scenarios or
  sensitivities. Purely factual, no emotion.
- **3**: Specific metrics but not fully customer-validated. Limited scenario/
  sensitivity analysis. Some attempt at emotive language.
- **4**: Specific, customer-validated metrics. Limited scenario/sensitivity analysis.
  Some emotive language but not consistently vivid.
- **5**: Specific outcome metrics. Customer-validated current→future change.
  Scenarios and sensitivities labeled. Vivid language building emotion beyond ROI.

## 5. Required Investment

Target (5/5): Budget and commercials signed off by budget owner + procurement.
Dedicated people resources reserved for rollout. Go-live anchored to a
customer-provided critical event. Back-dated steps to reach the outcome.

- **1**: General cost mentioned, no specifics. No resource allocation or timeline.
- **2**: Some cost details but not signed off. Vague resources. No timeline or
  critical event.
- **3**: Detailed costs but lacking full sign-off. Some resource allocation. Go-live
  mentioned but not tied to a critical event. No rollout steps.
- **4**: Detailed costs with partial sign-off. Resources specified. Go-live tied to a
  critical event. Some rollout steps but not comprehensive.
- **5**: Budget/commercials signed off by budget owner + procurement. Resources
  reserved. Go-live anchored to a customer-provided critical event. Back-dated steps
  included.

---

## How to present the score

Show a table with each section's 1-5, the readiness %, and: for every section under
5: the **specific missing input** dragging it down, traced to Step 2 ("not stated on
any call," "no procurement contact in CRM," etc.). Then hand off to the next-actions
playbook: the lowest-scoring section is where the recommended next move should aim.
