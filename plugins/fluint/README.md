# Olli by Fluint

Olli is Fluint's AI sales agent, brought into the AI assistant you already use. Type `/fluint:olli` and the conversation becomes Olli: brief, calm, strategic, and written the way your buyers talk. Olli stays on until you say "exit Olli".

Ask about a deal and Olli answers from Loop, Fluint's record of your CRM, calls, and email, already read and summarized. It tells you how current that read is and never invents a number it does not have.

- *"What's going on with the Globex renewal?"*
- *"Who have we actually talked to at Initech?"*
- *"Tighten this email to their CFO."*
- *"What should I do next on Acme?"*

When you ask for a finished asset, such as call prep, a follow-up, or a business case, Olli runs the matching play from the **Loop by Fluint** plugin and hands the result back in its own voice. Install both.

## Install

In Claude Code:

```
/plugin install fluint --marketplace Fluint-io/skills
```

Install `loop` the same way; the two work together. For the Claude and ChatGPT apps, see the [install guide](https://github.com/Fluint-io/skills/blob/master/INSTALL.md).

## Requirements

- A Fluint account.
- The Loop connector, `https://mcp.fluint.io/mcp`, connected and signed in with your Fluint account. Olli has no other data source and stops if Loop is not connected.

## What it reads and sends

Olli is instructions only. It runs no code, scripts, hooks, or local servers on your machine.

- **Reads:** deal, meeting, email, and activity briefs from your Fluint workspace, through the Loop connector, using your own Fluint sign-in. Those briefs come from your connected CRM, call recordings, and email, and can include names, titles, and email addresses of the people on your deals.
- **Sends:** your questions go to Loop to find the relevant briefs. Nothing is sent anywhere else, and the plugin stores nothing of its own.

## Support

[fluint.io](https://www.fluint.io) · [Source and install guide](https://github.com/Fluint-io/skills)
