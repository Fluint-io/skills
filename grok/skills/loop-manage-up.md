---
name: loop-manage-up
description: >-
  Prep an AE to manage up to sales leadership: forecast calls, pipeline reviews,
  1:1s, and deal reviews that surface territory and quarter risk clearly and ask
  leadership for the backing to act on it. Use this skill whenever a seller says
  "prep me for my forecast call", "pipeline review with my manager", "1:1 with my
  VP", "deal review with leadership", "territory review", "what should I flag to
  my boss", "help me manage up", "I need an intro or budget from leadership",
  "build my quarter plan", or is getting ready to talk about their deals with
  their own sales management. It pulls the territory and deals from Loop, grades the forecast
  on buyer behavior, separates real risk from drama, names the big bets, and turns
  each risk into a specific ask of leadership delivered as a drafted asset. This is
  internal-facing: the audience is the rep's own VP or CRO, not the buyer.
---

# Manage Up

## What this does

Most reps walk into a forecast call to defend their number. There is a better move: show
leadership a clear read of the territory, name where the risk really sits, say which bets
you are making this quarter, and ask for the specific backing you need to act. Leadership is
a stakeholder. You enable them the way you enable a champion: a clear picture and an easy,
specific ask.

The deliverable is a leadership-ready review made of four concrete parts:
1. A forecast graded on how the buyers are actually behaving, not on your champion's mood.
2. Each at-risk deal sorted into a real problem you can solve or drama you have to name.
3. The two or three big bets you are planting the quarter on, with the reason for each.
4. A specific ask of leadership per risk, handed over as a finished asset (a drafted intro,
   a ghostwritten exec email, a budget line with the ROI), not a vague "I could use help."

The audience is your own leadership, so this is internal communication, not a buyer asset.
Same discipline though: bottom line up front, numbers not adjectives, nothing to skim past.

## Step 1: Pull the territory

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` for the territory ("my deals closing this quarter", "which of my deals are
   at risk"), filtered to `brief_types: ["deal_brief"]`. Run it more than once with
   different phrasings; `limit` goes to 50.
2. `get_brief` every `deal_brief` in the quarter or territory.
3. For the flagged and big-bet deals, `get_brief` again with `covers_through` 30 days back to
   see what moved.

Where each piece goes:
- Stage in each deal summary against its weakest predictors: the forecast grade. A late stage
  with weak decision-process or economic-buyer reasoning moves back.
- The predictor reasoning: whether a blocker is a solvable problem or drama.
- The top `next_plays` entry per deal: what you are doing about it, and so what you need from
  leadership.
- There is no pipeline brief. The territory view is the set of deal briefs.

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

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Grade the forecast on buyer behavior

Read `references/frameworks.md` (Forecast on group behavior + the 60-Second Deal Review). The
most common forecasting error is trusting your champion's optimism instead of the group's
behavior. A champion always moves faster than the committee reaches consensus. So for each
deal, check the buyer behavior against the stage using the Deal Evidence checklist: written
problem statement, three roles confirming impact, a funded internal project, a real go-live
date, alternatives ruled out. Where the behavior does not match the stage, move the deal back
and flag it. Produce a 60-Second Deal Review for each flagged or big-bet deal.

Downgrades that match reality are worth more than an optimistic number leadership learns to
discount.

## Step 3: Separate real problems from drama

Read `references/frameworks.md` (Problems vs drama). For each at-risk deal, name what is
actually blocking it. A solvable problem has a next step: a missing stakeholder, no business
case, an unvalidated ROI. Drama has no next step because it is protecting something (someone's
job, a past decision, a turf line). Name which one it is. A better deck does not move drama,
and filing drama under "solvable problem" is how deals sit in the forecast for two quarters.

## Step 4: Name the big bets

Read `references/frameworks.md` (Big bets). You cannot over-invest everywhere. Pick the two
or three deals worth planting your quarter on, using the Change Equation and the two-way-door
test. Say why each is worth the bet, and what you will stop doing to fund it. Leadership backs
a rep who makes deliberate bets over one who spreads thin and hopes.

## Step 5: Turn each risk into a specific ask

Read `references/frameworks.md` and `references/output-templates.md`. This is the part reps
skip. For every risk, name the exact thing you need from leadership and hand it over as a
finished asset, using the forwardable-email patterns in the references:
- A warm intro to an exec? Draft the forwardable note for your VP to send.
- Budget or a discount approval? State the number, the deal it unblocks, and the ROI.
- Exec air-cover on a call? Draft the email your VP sends to the buyer's exec.
Deliver the ask done. "Can you help with the Acme deal" gets a shrug. "Here is the two-line
intro to their CFO, can you send it Thursday" gets action.

## The deliverable

Produce the review using the skeleton in `references/output-templates.md`. The seller walks
away with a document they can bring straight into the forecast call:
1. **Forecast at a glance** (commit / best case / at risk, graded on behavior)
2. **60-Second Deal Reviews** (one per flagged or big-bet deal, in the exact format)
3. **Risk sort: solvable vs drama** (what is really blocking each at-risk deal)
4. **Big bets** (the 2 to 3 you are planting the quarter on, and what you will drop to fund them)
5. **What I need from you** (the ask list, each with the drafted asset attached and ready to send)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Manage your leadership like a champion.** A clear picture and an easy, specific ask.
- **Forecast on group behavior, not your champion's optimism.** Move deals back when the
  behavior does not match the stage.
- **Name the drama.** A solvable problem has a next step; drama protects something. Do not
  file one as the other.
- **Deliver the ask done.** A drafted intro beats a request for help every time.
- **Grade to reality.** A forecast leadership can trust is what earns you the backing you ask for.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/frameworks.md

# Frameworks: Manage Up

## Managing up: leadership is a stakeholder

The skills that build a champion inside a buyer work inside your own company. Your VP or CRO
has Incentive (your number is their number), Influence (they control intros, budget, air
cover), and Information (they see the whole board). Treat a forecast call the way you would a
champion meeting: bring a clear picture, name what you need, make the ask easy to say yes to.
You are not defending. You are enabling them to help you.

## Forecast on group behavior, not champion behavior

The most common forecasting error is trusting your champion's optimism. A champion always
moves faster than their committee reaches consensus, so a deal can feel hot while the group
is nowhere near a decision. Forecast on what the buying group does, not on what your one
excited contact says. Where the behavior does not match the stage, move the deal back and
flag it. Downgrades that match reality build the one thing that compounds with leadership: a
forecast they can trust instead of one they learn to discount.

## The 60-Second Deal Review

The format that replaces the hour-long defend-your-deal ritual. Two parts: a Headlines block
leadership reads in seconds, and a Deal Evidence checklist that backs the call with buyer
behavior, not opinion.

**Headlines (three sentences):**
1. [Company] is going through [specific change], which means [negative outcome if unaddressed].
2. [Executive] tasked [high-influence champion] with [named project / initiative], targeting
   a rollout no later than [critical event].
3. Against [alternatives / threats], [executive] confirmed [quote about your differentiator]
   will drive [quote about the outcome they want].

**Deal Evidence checklist (yes / no / unknown for each):**
- Written problem statement built with the buying team's own data?
- Direct comments or edits from them confirming or correcting your POV?
- At least three buying roles confirming impact to a specific exec-level metric?
- A funded internal project or initiative, with a name and a team you can point to?
- A specific go-live date that, if missed, means a worse outcome for them?
- Written confirmation they have stopped exploring alternatives, because of a differentiator
  the other options do not have?
- The buying team tracking to a backdated set of milestones? Ahead or behind?

The number of "yes" answers is the forecast. A deal in the commit column with three "no"s is
not a commit, whatever the CRM stage says. This is what you grade against in Step 2.

## Problems versus drama

For every at-risk deal, name what is actually blocking it.
- **A solvable problem has a next step.** Missing stakeholder, no business case, ROI not
  validated, no compelling event. You can go get the missing piece.
- **Drama has no next step** because it is not about the deal at all. It protects something:
  someone's job security, a past decision, a turf boundary, a reputation. A better deck does
  not touch it.

The move with drama is to name it, then connect solving the underlying problem to the need
the drama protects. What does not work is treating drama like a solvable problem. That is how
deals sit in the forecast for two quarters while everyone waits for a next step that will not
land.

## Big bets

You cannot over-invest in every deal. Pick the two or three worth planting the quarter on.
- **The Change Equation:** a deal moves when Dissatisfaction x Vision x First Steps beats the
  Resistance to changing. A big bet is a deal where all three are high and you can push the
  first steps. Where resistance dominates, do not pour more in.
- **Two-way doors:** favor bets you can reverse. A pilot with pre-agreed expansion terms is a
  reversible door; you learn fast and cheap. A big-bang all-or-nothing commit is a one-way
  door. Prefer the reversible bet, and make the one-way bet only when the upside clearly
  warrants it.

For each big bet, say why it is worth it and what you will stop doing to fund it. A rep who
makes deliberate bets reads as someone running a territory, not someone hoping.

## The specific ask, delivered as a forwardable asset

Reps under-ask because a vague ask feels safer. It is not; it gets a shrug. For each risk,
name the exact thing you need and deliver it done. When the ask is an intro or exec air
cover, write the email for your VP to send, using the forwardable pattern below.

**Forwardable intro / air-cover pattern (for your VP to send to the buyer's exec):**
- **Subject:** the buyer's internal project or priority, in their language. Not your product.
- **Open on their priority:** name the initiative or trigger the exec already owns.
- **One specific point:** the root cause and the number, or the risk of delay. One, not three.
- **Give control back:** ask the exec for their read on a metric or criterion they own, so the
  note invites a reply instead of pushing.
- **Easy next step:** a small, dated ask ("15 minutes Thursday"), signed by your VP.

It reads as written by your VP because your VP is sending it. Their words, no vendor pitch,
no logo, no em dashes. Keep it to a screen.

**The ask that is not an email** (budget, approval): one tight block. Deal, amount at stake,
the exact approval requested, what it unblocks, and the ROI in numbers. Ready to approve on
sight.

## references/output-templates.md

# Output Templates: Manage Up

## The leadership review (produce this)

```
# Deal Review / Forecast: [Rep] - [quarter / territory]
Prepared for: [manager / VP]

## Forecast at a glance
| Category | Deals | Amount | Confidence (graded on behavior) |
|----------|-------|--------|---------------------------------|
| Commit | [n] | [$] | [why you trust it: the "yes" evidence] |
| Best case | [n] | [$] | [what would have to break right] |
| At risk | [n] | [$] | [moved back from commit because...] |

## 60-Second Deal Reviews (flagged + big-bet deals)
### [Deal] - [$] - close [date] - owner [rep]
Headlines
1. [Company] is going through [change], which means [negative outcome].
2. [Executive] tasked [champion] with [named project], targeting [critical event].
3. Against [alternatives], [executive] confirmed [differentiator] drives [outcome].
Deal Evidence: written problem [y/n] · buyer edits [y/n] · 3 roles on a metric [y/n] ·
funded project [y/n] · go-live date [y/n] · alternatives ruled out [y/n] · on backdated plan [y/n]
Call: [where it really sits, and the single biggest risk]
Ask: [what you need, or "on track"]

## Risk sort: solvable vs drama
| At-risk deal | What is blocking it | Solvable or drama | The move |
|--------------|---------------------|-------------------|----------|
| [deal] | [missing stakeholder / no business case / turf] | [solvable/drama] | [go get X / name the drama] |

## Big bets this quarter
- **[Deal]:** why it is worth over-investing (Change Equation: dissatisfaction, vision, first
  steps). Reversible or one-way door: [which]. What I will stop doing to fund it: [x].

## What I need from you
| Risk it unblocks | The ask | Drafted asset (ready to send) |
|------------------|---------|-------------------------------|
| [deal / risk] | Warm intro to [exec] | [see draft below] |
| [deal / risk] | Approve [$ / discount] | [number + ROI + deal it unblocks] |
| [deal / risk] | Exec air cover on [call] | [see draft below] |
```

## Drafted-asset stubs (hand these over done, not as requests)

**Forwardable intro / air-cover email for your VP to send:**
```
Subject: [buyer's internal project / priority, their language]

[Name],

[One line on the priority the exec already owns.]
[One specific point: the root cause and a number, or the risk of delay.]
[Give control back: ask their read on a metric or criterion they own.]
[Small dated next step, e.g. "worth 15 minutes Thursday?"]

[VP name]
```

**Budget / approval ask (one block):**
```
Deal: [name] · Amount at stake: [$] · Ask: [approve $X / Y% discount]
Unblocks: [what specifically moves if approved]
ROI / rationale: [the math, not adjectives]
```

## Reminders

- Grade confidence on the Deal Evidence "yes" count, not your champion's mood.
- Name the drama. Do not file it as "solvable, next step will fix it."
- Deliver every ask as a finished asset. A drafted intro beats "can you help."
- Bottom line up front. Numbers, not adjectives. No em dashes, no filler.
