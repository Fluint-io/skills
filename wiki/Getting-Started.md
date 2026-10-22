# Getting Started

## Requirements

- **A paid Claude plan** (Pro, Max, Team, or Enterprise) to install plugins.
- **Loop**, Fluint's MCP, connected with your [Fluint](https://www.fluint.io) account. It is where every skill gets its deal data.

## Install the marketplace

1. In Claude, open **Settings → Customize → Plugins** and click **Add**.
2. Link the GitHub repository:
   ```
   Fluint-io/skills
   ```
3. On the **Discover** tab, add both **Olli** and **Loop**.

### Single-skill option

Each skill is also a standalone `.skill` file. To test just one, download it and use **Settings → Capabilities → Upload skill**.

## Connect Loop

The skills read every deal from Loop. Add a custom connector (in Claude: **Settings → Connectors → Add custom connector**) with the URL `https://mcp.fluint.io/mcp`, then sign in with your Fluint account. Loop already fuses your CRM, calls, and emails into briefs, so there is nothing else to connect.

## Run your first skill

You do not type a command. You describe the situation, and Claude picks the right skill.

Try one of these:

- *"Prep me for my call tomorrow with the VP of Ops at Acme."*
- *"Help me follow up after today's demo, there were four people on it."*
- *"Why is the Acme deal stuck?"*
- *"Build the business case for Acme."*

The skill will:

1. **Gather context** from your connected sources (or ask you for it).
2. **Apply the framework** for that play.
3. **Hand you the deliverable**: a brief, a set of follow-ups, a plan, a business case.
4. **Flag any gaps** and tell you the one question to ask next.

## Next

- Read [[The Philosophy]] to understand what the skills are doing and why.
- Skim the [[Skill Reference]] to see all ten and when each fires.
