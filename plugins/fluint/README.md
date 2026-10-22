# Olli & Loop by Fluint

Olli, Fluint's AI sales agent, and eleven sales plays that run enterprise deals the way top reps sell, brought into the AI assistant you already use. Everything reads your deals from Loop, Fluint's record of your CRM, calls, and email, already read and summarized, and is written in your buyer's own words.

## Talk to Olli

Type `/fluint:olli` and the conversation becomes Olli: brief, calm, strategic, and written the way your buyers talk. Olli stays on until you say "exit Olli". It tells you how current its read of a deal is and never invents a number it does not have.

- *"What's going on with the Globex renewal?"*
- *"Who have we actually talked to at Initech?"*
- *"Tighten this email to their CFO."*

When you ask for a finished asset, Olli runs the matching play below and hands the result back in its own voice.

## The plays

Each play is one moment in a deal, built on the frameworks from *Selling With* and *Brief & Brilliant*, and each ends in something you can send.

| Play | What you walk away with |
|------|-------------------------|
| `/fluint:plays` | Not sure what you need? Describe the deal and it points you to the right play. |
| `/fluint:call-prep` | A one-screen meeting brief: a point of view, planned discovery, the opening, and the ask. |
| `/fluint:follow-up` | A stakeholder map, the problem in the buyer's words, and a forwardable follow-up for each person on the call. |
| `/fluint:multithread` | The real buying committee, a value hypothesis for each person, and the outreach to reach them. |
| `/fluint:account-plan` | A point of view, the opportunities ranked by executive priority, and the first message to send. |
| `/fluint:champion` | The kit your champion carries into the meetings you are not in. |
| `/fluint:displace` | A plan to unseat the incumbent by changing the criteria, not by winning a feature war. |
| `/fluint:business-case` | A one-page business case in the customer's words, scored, with the next move to strengthen it. |
| `/fluint:advance` | Why the deal stalled and the moves to restart it, or a mutual action plan to close it. |
| `/fluint:qbr` | A QBR that leads with their success, gets ahead of risk, and opens expansion without a pitch. |
| `/fluint:manage-up` | A forecast-call pack: an honest read of the territory, your big bets, and specific asks of leadership. |

You do not have to remember any of these. Say what you are doing, such as *"Prep me for my call with Acme tomorrow"*, and the right one runs.

## Install

In Claude Code:

```
/plugin install fluint --marketplace Fluint-io/skills
```

For the Claude and ChatGPT apps, see the [install guide](https://github.com/Fluint-io/skills/blob/master/INSTALL.md).

## Requirements

- A Fluint account.
- The Loop connector, `https://mcp.fluint.io/mcp`, connected and signed in with your Fluint account. Olli and the plays have no other data source and stop if Loop is not connected.

## What it reads and sends

This plugin is instructions and reference material only. It runs no code, scripts, hooks, or local servers on your machine.

- **Reads:** deal, meeting, email, and activity briefs from your Fluint workspace, through the Loop connector, using your own Fluint sign-in. Those briefs come from your connected CRM, call recordings, and email, and can include names, titles, and email addresses of the people on your deals.
- **Sends:** your questions go to Loop to find the relevant briefs. The plugin makes no other external requests and stores nothing of its own.
- **Your AI assistant** processes your questions and the briefs Loop returns, including any names and email addresses in them, to write its answers and drafts, under that assistant's own data terms. Drafts stay in your conversation until you choose to send them.

## Support

[fluint.io](https://www.fluint.io) · [Source and install guide](https://github.com/Fluint-io/skills)
