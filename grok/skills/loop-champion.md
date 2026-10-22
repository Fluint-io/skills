---
name: loop-champion
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

**Loop not connected?** Stop and tell the seller to connect it before going further: in Grok add it at grok.com/connectors (New Connector, then Custom, URL `https://mcp.fluint.io/mcp`), or follow
https://app.fluint.io/install.
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

---

# Reference files

The `references/...` files this skill reads are included below, in full.

## references/frameworks.md

# Frameworks: Champion Enablement

## The 3 I's: is this a champion?

A champion has all three. Miss one and you have something weaker.
- **Incentive.** They personally win if this happens. Not "they like it." They gain, or
  they avoid a loss, when the deal closes.
- **Influence.** People inside listen to them. Discount this by believability: a person can
  have a title and still not be believed on this topic. Influence is who they can actually
  move, on this decision.
- **Information.** They know how the buying really works: who decides, what the process is,
  where it will stall.

Incentive + Information but no Influence = a coach. Helpful, but cannot carry the deal.
Influence + Information but no Incentive = an advocate who will not spend capital for you.
If your contact is not a real champion, developing or replacing them comes before arming
them. Test a champion by asking them to lay out the buying process, or to introduce you to
someone else. A real champion can and will.

Every step they take internally spends social capital, win or lose. So give them something
in return each time. You live in this deal; they do not.

## The buying group (Influence Map)

Map the real decision structure, not the org chart. Four roles recur:
- **Champion.** Advocates internally, opens doors, has the 3 I's.
- **Economic Buyer.** Controls the budget or the approval to spend it. Their yes is
  required. Often not the person who signs.
- **Technical Evaluator.** Judges whether it actually solves the problem. Focused on
  feasibility and implementation.
- **Internal Skeptic.** Pushes back, points out what you are missing. Not your enemy: your
  best quality control. Convert them early and they become your strongest advocate.

Single-threaded deals are the highest-risk deals in the pipeline. The rule: never present
to a group until you have had a one-on-one with every person who will be in that room. No
surprises in the meeting.

## The Messaging Matrix

Same core recommendation, tuned per stakeholder. For each person: what outcome they care
about, the number or proof that lands, and the one-line message in their language. The
Economic Buyer hears impact and recommendation. The Evaluator hears feasibility and rigor.
The Skeptic hears data so specific they cannot argue with it. Tailoring speaks to how each
person actually decides, not spin.

## The 4-Sentence Soundbite

The 30-second version your champion says to a skeptical exec. Four sentences:
1. **Because of [the change]** - the shift that makes this matter now.
2. **Now is the time to [the approach] by [the date]** - the recommendation, timebound.
3. **If we do, [the good outcomes]** - what they gain.
4. **If we do not, [the bad outcomes]** - what worsens, and it compounds.

Write it in the champion's voice. If they cannot say it out loud without it sounding like
your marketing, it is wrong. Simplify until it sounds like them.

## Objections: Acknowledge, Diagnose, Redirect

Every objection follows the same three-step response:
1. **Acknowledge.** Validate the concern. Do not argue or minimize. "That is fair. A lot of
   teams raise the same thing."
2. **Diagnose.** Figure out which urgency force is actually weak (below). The stated
   objection is usually not the real one.
3. **Redirect.** Once they have named the gap in their own words, point back to the real
   problem. "So the question is not whether you can afford to do this. It is whether you can
   afford not to."

**The Urgency Equation:** Urgency = (Dissatisfaction x Excitement x Direction) / Priority.
Each objection tells you which term is weak:
- **Low Dissatisfaction** ("let us revisit next quarter"): current state is not painful
  enough. Quantify the cost of inaction. Put a clock on it.
- **Low Excitement** ("we tried something like this before"): they do not see the upside, or
  they got burned. Deeper value discovery, a reference from a similar situation.
- **Low Direction** ("we handle that internally", "too expensive"): they do not see how you
  are different, or the value relative to cost. Show the business case and the differentiation.
- **High Priority Level** ("we need to think about it", "let me run it by people"): too much
  competing, or they have not aligned the right people yet. Help them prioritize, and equip
  them with the questions those people will ask.

Write each response in the champion's voice, as something they can deliver, not as your rebuttal.

## The skeptic

There is almost always one blocker who decides the deal. Profile what they are protecting
(their job, a past decision, their team's workload, their reputation). Their objection is
rarely the real thing. Give a reframe that shifts how they see the situation, not a
defensive answer. Then decide: engage them directly, or coach the champion to. Converting a
skeptic early turns your biggest risk into your best advocate.

## The one-pager: a consulting-style exec summary

The document the champion forwards internally. Structure it as Situation, Complication,
Recommendation (the way a strategy consultant frames a memo), with the champion's name on it:
- **Situation:** the change happening in their business, and the goal or vision the executive
  is driving toward. A few factual bullets, no spin.
- **Complication:** the problem standing in the way of that goal, the root causes behind it,
  and what it costs if left unchecked.
- **Recommendation:** given their requirements, the approach (as decision criteria, not a
  product), then a line that you have found a solution proven to drive the outcome for similar
  companies, and a note on the alternatives considered and why this path wins.

Rules:
- About the problem, the cost of inaction, and why now. Not your product.
- No logo, no vendor branding. The best color scheme is camouflage: their words, so it reads
  as internally authored. Please do not send a billboard.
- The champion's name in the byline, not yours. You are ghostwriting.
- One page. People read in passes: headline, bold, bullets, then the rest.

When the deal warrants the full version (a scored problem statement, KPI table, required
investment), point the seller to the `loop-business-case` skill. This one-pager is the
lightweight exec summary; that skill builds the complete case.

## Forwardable email patterns (when the champion sends a written note)

If your champion is emailing a stakeholder rather than meeting them, give them the note. Two
patterns by recipient:
- **Non-technical (economic buyer, sponsor):** subject = their internal project in their
  language; open on their priority; one specific number and its root cause; tie the small next
  step to the business case; signed by the champion.
- **Technical evaluator:** subject = the technical outcome plus next steps; validate their
  specific objection; three points on how the approach protects their responsibility, team,
  and risk; hand control back by asking what criteria would prove it out.
Both: BLUF, their words, one next step, under 120 words, no logo, no em dashes.

## references/output-templates.md

# Output Templates: Champion Enablement

## The champion kit (produce this)

```
# Champion Kit: [Account] - [deal]
Champion: [name, role]

## Champion read (3 I's)
- Incentive: [strong/weak + why]
- Influence: [who they can actually move, discounted by believability]
- Information: [do they know how the buying really works]
Verdict: [real champion / coach / needs developing]. Shore up: [the weak I].

## Internal meeting map
| Who they must sell | Buying role | What they care about | Proof point that lands |
|--------------------|-------------|----------------------|------------------------|
| [name] | Economic Buyer | [outcome] | [number / reference] |
| [name] | Technical Evaluator | [feasibility concern] | [proof] |
| [name] | Internal Skeptic | [what they protect] | [data they cannot argue] |

## 30-second soundbite (for the champion to say)
Because of [change], now is the time to [approach] by [date].
If we do, [good outcomes]. If we do not, [bad outcomes, and they compound].

## Objection reframes
| Objection they will hear | Urgency force that is weak | The champion's response (their words) |
|--------------------------|----------------------------|---------------------------------------|
| [objection] | [Dissatisfaction / Excitement / Direction / Priority] | [Acknowledge → Diagnose → Redirect, in their voice] |

## The skeptic plan
- Who: [name, role]. Protecting: [job / past decision / workload / reputation].
- Likely objections: [spoken] / [unspoken].
- Reframe: [shift how they see it, not a defense].
- Engagement: [go direct, or coach the champion to approach]. Timing: [when].

## Forwardable one-pager (champion forwards this)
[See skeleton below.]
```

## The forwardable one-pager skeleton (Situation / Complication / Recommendation)

```
Executive Summary: [the business priority, in their language]
Prepared by [Champion name]

Situation
[The change happening in their business. A few factual bullets. Then the goal or vision the
executive is driving toward.]

Complication
[The problem standing in the way. The root causes behind it. If left unchecked, what it costs
(a number if you have one; a flagged gap if you do not).]

Recommendation
[Given their requirements, the approach as decision criteria, not a product.]
[We found [solution], proven to drive [outcome] for similar companies via [differentiator].]
[Alternatives considered: [X], but this path wins because [reason].]
```

Rules for the one-pager: no logo, no vendor branding, no product feature list. It reads as if
someone inside the account wrote it. Camouflage, not a billboard. Champion's name on it. For
the full scored version, use the `loop-business-case` skill.

## Reminders

- Qualify the champion (3 I's) before building the rest. Arming a coach wastes the kit.
- Every internal move costs your champion capital. Make each one easy and worth it.
- No em dashes, no jargon, no logo. Their words.
