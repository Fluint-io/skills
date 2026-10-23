---
name: displace
description: >-
  Build the narrative and the plan to unseat an incumbent or beat a competitor in
  a live deal. Use this skill whenever a seller says "we're up against
  [competitor]", "displace the incumbent", "how do I unseat [vendor]", "they're
  already using [tool]", "competitive deal", "compete against [X]", "win against
  the incumbent", or is in an evaluation where another provider is the default. It
  pulls context from Loop, reads the incumbent's strengths and gaps, builds a differentiation
  narrative based on approach and outcome (not a feature war), writes the switching
  story, and gives you trap-setting questions that surface the incumbent's gaps
  without badmouthing. Prefer this over a feature-comparison battlecard any time a
  deal is competitive.
---

# Competitive Displacement

## What this does

When you are up against an incumbent, the feature war is the losing game. The buyer already
owns the incumbent, switching feels risky, and a battlecard turns the conversation into a
checklist you may not win. This skill builds the other approach: change the criteria, make the
status quo feel riskier than the switch, and let the buyer surface the incumbent's gaps
themselves.

1. Reads the incumbent: what they are strong at, and where they fall short for this buyer.
2. Builds differentiation on approach and outcome, not features.
3. Writes the switching story: why now is the right time to move.
4. Gives you trap-setting questions that expose the gaps without badmouthing anyone.

The deliverable is a displacement plan you can run in the next conversation.

## Step 1: Lock the deal and pull context

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the deal and the competitor ("Acme deal, what are they using today
   and how do they feel about it").
2. `get_brief` the `deal_brief`.
3. `get_brief` the `meeting_brief`s and `email_brief`s that mention the incumbent.
4. `get_record` on a meeting's own source record for the buyer's exact words about the
   incumbent.

Where each piece goes:
- The competitive-position reasoning: who you are really up against, including the status quo
  and tools they already own.
- The decision-criteria reasoning: whether the criteria are set, and so whether there is still
  room to change them.
- `problem_statement` and `metrics`: the villain and the switching story, in their words.
- The top `next_plays` entry: what the next conversation has to accomplish.

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

Confirm who the incumbent or competitor is. If it is unknown, that is the first thing to find.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Read the incumbent

Read `references/frameworks.md` (Read the incumbent). Name who you are up against, what they
are genuinely strong at (respect it, do not pretend it away), and where they fall short for
this specific buyer. Note what a switch would cost the buyer, because that cost is the real
opponent, not the competitor.

## Step 3: Build the differentiation

Read `references/frameworks.md` (Be different, not better). Write the 2 to 3 ways you are
meaningfully different in approach or outcome, tied to what this buyer cares about. Not a
feature list. Then name the villain: the status-quo problem the incumbent structurally cannot
solve. Different beats better, because better invites a comparison and different reframes it.

## Step 4: Write the switching story

Read `references/frameworks.md` (The switching story). Tell the story of why now is the right
time to move: what has changed in their business or market that makes the status quo the risky
choice. Frame it with the change equation: dissatisfaction with today, a vision of the after,
and an easy first step have to outweigh the resistance to switching.

## Step 5: Set the traps

Read `references/output-templates.md`. Write 3 discovery questions that surface the gaps and
frustrations with the current solution, without badmouthing the competitor. The best of these
is the "what must be true of a solution for this to work" question, which gets the buyer to
name the requirements the incumbent cannot meet.

## The deliverable

Produce the displacement plan using the skeleton in `references/output-templates.md`:
1. **Incumbent read** (strengths, gaps for this buyer, the cost of switching)
2. **Differentiation** (2 to 3 differences in approach/outcome + the named villain)
3. **Switching story** (why now, framed as status-quo risk)
4. **Trap-setting questions** (3 questions that surface the gaps, no badmouthing)

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **Be different, not better.** Better invites a feature war. Different reframes the criteria.
- **Sell the approach before the product.** Win "what must be true" and the search narrows to you.
- **The real opponent is the switching cost, not the competitor.** Make the status quo the risk.
- **Never badmouth.** Let the buyer surface the gaps. Their conclusion beats your accusation.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
