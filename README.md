# Loop, in the AI you already use

**Bring Olli and your Loop deals into Claude, ChatGPT, and Grok.**

You already know Olli: the sales agent in Fluint that writes like your best rep and thinks a few moves ahead on every deal. This brings Olli, and everything Loop knows about your deals, into the AI assistant you already use every day. Same voice. Same judgment. Same deals. No new tab, no copy-paste.

Ask about a deal and the answer comes from Loop: your CRM, calls, and email, already read and summarized. Ask for a business case, a follow-up, or call prep, and you get the finished asset, written in your buyer's own words.

Built by [Nate Nasralla](https://www.fluint.io), author of *Selling With* and *Brief & Brilliant*, on the frameworks from both books.

---

## Get started

Paste this into Claude, ChatGPT, or Grok, in the app or the terminal:

```
Install Olli and Loop by following https://app.fluint.io/install
```

It adds one plugin, **fluint**: Olli (`/fluint:olli`) and the plays (`/fluint:...`), and connects your Loop account. Prefer to install the plugin yourself? In Claude Code:

```
/plugin install fluint --marketplace Fluint-io/skills
```

The paste-in line above also connects Loop for you. The only thing left to you is signing in to Fluint. In the Claude or ChatGPT apps, it walks you through a few clicks in settings. In Grok, it saves Olli and the plays as Grok skills for you. [INSTALL.md](INSTALL.md) has every path.

---

## Talk to Olli

Type `/fluint:olli` and the conversation becomes Olli: brief, calm, strategic, and written the way your buyers talk. Olli stays on until you say "exit Olli".

- *"What's going on with the Globex renewal?"*
- *"Who have we actually talked to at Initech?"*
- *"Tighten this email to their CFO."*
- *"What should I do next on Acme?"*

Olli reads the deal from Loop before answering, tells you how current that read is, and never invents a number it does not have. When you ask for a deliverable, Olli runs the matching play below and hands it back in its own voice.

---

## The plays

Each play is one moment in a deal, built on a framework from *Selling With* and *Brief & Brilliant*, and each ends in something you can send. Olli picks the right one for you, or you can call one directly.

| Play | What you walk away with |
|------|-------------------------|
| **/fluint:plays** | Not sure what you need? Describe the deal and it points you to the right play. |
| **/fluint:call-prep** | A one-screen meeting brief: a point of view, planned discovery, the opening, and the ask. |
| **/fluint:follow-up** | A stakeholder map, the problem in the buyer's words, and a forwardable follow-up for each person on the call. |
| **/fluint:multithread** | The real buying committee, a value hypothesis for each person, and the outreach to reach them. |
| **/fluint:account-plan** | A point of view, the opportunities ranked by executive priority, and the first message to send. |
| **/fluint:champion** | The kit your champion carries into the meetings you are not in: soundbite, objection reframes, a one-pager. |
| **/fluint:displace** | A plan to unseat the incumbent by changing the criteria, not by winning a feature war. |
| **/fluint:business-case** | A one-page business case in the customer's words, scored, with the next move to strengthen it. |
| **/fluint:advance** | Why the deal stalled and the moves to restart it, or a mutual action plan to close it. |
| **/fluint:qbr** | A QBR that leads with their success, gets ahead of risk, and opens expansion without a pitch. |
| **/fluint:manage-up** | A forecast-call pack: an honest read of the territory, your big bets, and specific asks of leadership. |

You do not have to remember any of these. Say what you are doing and the right one runs:

- *"Prep me for my call with the VP of Ops at Acme tomorrow."*
- *"Help me follow up after that demo, there were four people on it."*
- *"Why is the Acme deal stuck?"*
- *"Build the business case for Acme."*

---

## What makes it different

- **It already knows your deals.** Everything comes from Loop, so there is nothing to paste and nothing to explain. If Loop has not seen something yet, it says so and tells you the one question that would fill the gap.
- **It focuses where Loop says to.** When Loop has a next play for a deal, that is what Olli and the plays build around.
- **It writes in your buyer's words.** Their phrases, their numbers, their priorities. Built to be forwarded by a champion without editing.
- **It is built on what is not in training data.** Every play is anchored to a framework tested by thousands of sellers, not the market-average advice a general AI gives.
- **It ends in something you can send.** Not analysis to figure out later. A follow-up, a champion kit, a business case, ready to ship.

---

## Who this is for

Loop customers running complex, multi-stakeholder, mid-market and enterprise deals: account executives, sales engineers, and account managers. If your deals get made in rooms you are not in, and won or lost on whether your champion can carry the message, this is built for you.

---

## Upgrading from an earlier version

It is now one plugin, `fluint`: `/fluint:olli` for Olli and `/fluint:...` for the plays. Reinstall it once (the install line above handles this), then:

| Was (1.0) | Was (1.1) | Now |
|-----|-----|-----|
| sales-plays | `loop-plays` | `fluint:plays` |
| multithread | `loop-multithread` | `fluint:multithread` |
| account-planning | `loop-account-plan` | `fluint:account-plan` |
| call-prep | `loop-call-prep` | `fluint:call-prep` |
| call-follow-up | `loop-follow-up` | `fluint:follow-up` |
| champion-enablement | `loop-champion` | `fluint:champion` |
| competitive-displacement | `loop-displace` | `fluint:displace` |
| deal-advancement | `loop-advance` | `fluint:advance` |
| qbr-prep | `loop-qbr` | `fluint:qbr` |
| manage-up | `loop-manage-up` | `fluint:manage-up` |
| one-page-business-case | `loop-business-case` | `fluint:business-case` |

---

## The thinking behind it

Olli and the plays are the productized version of the system in two books:

- ***Selling With*** — the art of selling with champions to shape the internal buying conversations that decide enterprise deals.
- ***Brief & Brilliant*** — how to simplify complex deals and sell through the noise, in the buyer's own language.

---

## Feedback

Found a rough edge, or a play you would run differently? Open an issue. These are living skills, tuned from real deals.

## License

MIT.
