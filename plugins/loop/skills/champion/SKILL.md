---
name: champion
description: >-
  Build the internal-selling kit your champion needs for the meetings you will
  not be in. Use this skill whenever a seller says "help me arm my champion",
  "champion enablement", "build a one-pager my champion can share internally",
  "prep my champion for their internal meeting", "how do I handle the skeptic on
  this deal", "the blocker I need to win over", "give me objection responses",
  "help my champion sell this up", or is trying to influence a buying decision
  that happens when they are not in the room. It pulls the deal from Loop, maps the internal buying
  group, writes a 30-second problem soundbite, builds objection reframes in the
  champion's own words, plans the skeptic, and drafts a forwardable one-pager.
  Prefer this over freehand internal-selling advice any time the deal depends on
  someone else carrying the message internally.
---

# Champion Enablement

## What this does

Buyers close deals, not reps. The decision gets made in an internal meeting you are not
invited to, and your champion is the one carrying your message into that room. If they
carry it badly, you lose. So this skill builds the kit that lets them carry it well:

1. A read on whether your contact is actually a champion, or just a friendly coach.
2. A map of who they have to sell internally, and what each of those people cares about.
3. A 30-second problem soundbite they can say to a skeptical exec.
4. Objection reframes, in their words, for the pushback they will face.
5. A plan for the specific skeptic or blocker on this deal.
6. A forwardable one-pager: problem, cost of inaction, why now. Not a product pitch.

No champion, no deal. You are enabling a person to carry your message, not enabling a product.

## Step 1: Lock the deal and qualify the champion

**Read the briefs.** Loop (`mcp.fluint.io`) is the only data source. It turns the CRM,
calls, and email into briefs: a `deal_brief` per opportunity, a `meeting_brief` per call, an
`email_brief` per thread, and an `activity_brief` per deal's logged tasks and notes. Do not
reach for any other tool, even if one is connected. The brief is the answer; a raw record is
only evidence.

1. `find_briefs` naming the deal and the people ("who is championing the Acme deal and
   who is pushing back").
2. `get_brief` the `deal_brief`.
3. `get_brief` the recent `meeting_brief`s and `email_brief`s, especially any the champion
   was in.
4. `get_record` on a meeting's own source record when you need the champion's or skeptic's
   exact words.

Where each piece goes:
- The champion-strength reasoning: the starting point for the 3 I's. It usually names who is
  carrying the deal and who has gone quiet.
- `attendees` across meetings: who the champion has brought in, and who never appears.
- `problem_statement` and `metrics`: the soundbite and the one-pager, in their words.
- Objections in the deal summary and meeting briefs: the reframes and the skeptic plan.
- The top `next_plays` entry: what the champion needs to carry into the next internal meeting.

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

Then qualify your champion against the 3 I's (`references/frameworks.md`): Incentive,
Influence, Information. A contact with Influence and Information but no Incentive is a
coach, not a champion, and coaching you is not the same as spending capital for you. If the
person is not a real champion, say so. The first move may be to develop or replace them, not
to arm them.

**Loop missing a fact? Flag it, and make the gap a move.** Mark it inline as `[MISSING: ...]` and continue. Every gap gets the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint. Not "get more data."

**Who can actually say yes?** Name the people with the power to approve this, or to block it, and mark whether they are engaged yet. Start from the deal summary, which usually names the economic buyer, and the economic-buyer-access and decision-process reasoning, which say whether they have been in the conversation. Power is often not in the room. If the deciders are absent or untouched, that is the headline, not a footnote.

## Step 2: Map the internal meetings

Read `references/frameworks.md` (Influence Map + buying-group roles). Map who your champion
has to win: the Economic Buyer, the Technical Evaluator, the Internal Skeptic, and any
others. For each, note what outcome they care about and the proof point that lands. Same
recommendation, different emphasis per person. That is respect for how different people
decide, not manipulation.

## Step 3: Write the 30-second problem soundbite

Read `references/frameworks.md` (4-Sentence Soundbite). Write the thing your champion can say
in 30 seconds to a skeptical exec. Four sentences:
- Because of [the change],
- now is the time to [the approach] by [the date],
- if we do, [the good outcomes],
- if we do not, [the bad outcomes, getting worse].

Their language, not yours. Something they can actually say out loud without cringing.

## Step 4: Build the objection reframes

Read `references/frameworks.md` (Acknowledge-Diagnose-Redirect + the Urgency Equation).
Anticipate the top three objections your champion will face internally. For each, give them
the reframe: acknowledge it, diagnose which urgency force is weak underneath it, and redirect
to the real problem. Write the response in the champion's voice, not a rep's rebuttal.

## Step 5: Plan the skeptic

There is usually one blocker who matters. Profile them: role, what they are protecting, the
objections they will raise (spoken and unspoken). Give a reframe for each, and an engagement
plan: do you go direct, or coach your champion to approach them. Convert the skeptic early
and they become your best quality control and often your strongest advocate. They are not
your enemy.

## Step 6: Draft the forwardable one-pager

Read `references/output-templates.md`. Draft a one-pager the champion can forward internally.
It is about the problem, the cost of inaction, and why now. It is not a product pitch, and it
does not carry your logo. Camouflage. Put the champion's name on it, not yours. The best
color scheme is their branding and their words, so it reads as internally authored.

## Output format

Produce the kit using the skeleton in `references/output-templates.md`:
1. **Champion read** (3 I's assessment + what to shore up)
2. **Internal meeting map** (who to sell, what they care about, proof point)
3. **30-second soundbite** (the 4 sentences)
4. **Objection reframes** (objection / diagnosis / the champion's response)
5. **The skeptic plan** (profile, reframes, engagement)
6. **The forwardable one-pager**

## The operator's read

Before you hand it over, add the part a summary cannot: the one thing an experienced operator would notice that the data does not show on its own. The non-obvious risk. The stakeholder who matters more than their title. The deal that is not what it looks like. The strength that is quietly a trap. One or two sentences of judgment, called out plainly. Anyone can produce the map. This is the read.

## Operating principles

- **No champion, no deal.** Qualify the person before you arm them.
- **Enable a person, not a product.** Everything is built for them to carry, not for you.
- **Camouflage, not a billboard.** Their name, their words, no logo.
- **The skeptic is quality control, not the enemy.** Convert them early.

- **Voice guard.** Anything the buyer will read opens with their words, from the call or their own materials, in the first line. Banned openers: "Great connecting," "As discussed," "I wanted to follow up," "Hope this finds you well," "Circling back." If a sentence would survive being pasted into a different deal, it is too generic. Cut it.
