---
name: olli-loop-setup
description: Install Olli and the Loop plays, and connect the Loop MCP.
---

# Install Olli and Loop

Olli, Fluint's AI sales agent (`/olli:chat`), and eleven Loop sales plays (`/loop:*`), all running on your live deal data through Loop, Fluint's MCP.

https://github.com/Fluint-io/skills

You are an agent following these steps for the user. Run the commands yourself; only hand a step to the user when it needs their browser or an admin console.

## 1. Find the host

Run alone:

~~~bash
claude --version
~~~

If it prints a version, you are in Claude Code: do steps 2 and 3. If not, skip to "Other hosts".

## 2. Install the plugins (Claude Code)

First, clear out older versions. Earlier releases used a marketplace and plugin both named `uncommon-sales-skills`. Run:

~~~bash
claude plugin marketplace list
~~~

If `uncommon-sales-skills` is listed, remove whatever came from it. Each command may report that nothing is installed; that is fine.

~~~bash
claude plugin uninstall uncommon-sales-skills@uncommon-sales-skills
claude plugin uninstall olli@uncommon-sales-skills
claude plugin uninstall loop@uncommon-sales-skills
claude plugin marketplace remove uncommon-sales-skills
~~~

Then install:

~~~bash
claude plugin marketplace add Fluint-io/skills
claude plugin install olli@fluint
claude plugin install loop@fluint
~~~

Two plugins, two prefixes: `olli` gives `/olli:chat`, `loop` gives the plays (`/loop:call-prep`, `/loop:business-case`, ...). Install both; Olli runs the plays for deliverables.

Already on `fluint`? Update instead of reinstalling:

~~~bash
claude plugin marketplace update fluint
claude plugin update olli@fluint
claude plugin update loop@fluint
~~~

## 3. Connect Loop (Claude Code)

Check first. The user may already have Loop as a claude.ai connector:

~~~bash
claude mcp list
~~~

If any server points at `mcp.fluint.io`, or a connector named Loop is listed, skip to step 4. Otherwise:

~~~bash
claude mcp add --transport http --scope user loop https://mcp.fluint.io/mcp
~~~

Loop signs in with OAuth in a browser, which you cannot do. Tell the user: run `/mcp`, choose `loop`, choose Authenticate, and sign in with their Fluint account.

Loop is required. It is the only data source Olli and the plays use, and they stop if it is not connected. If the user has no Fluint account, tell them they need one first.

## Other hosts

You cannot install these yourself. Give the user these steps verbatim.

**Claude app (claude.ai, desktop):**
1. Customize → Plugins → Add marketplace → `Fluint-io/skills`. Install both **olli** and **loop**, and turn on **Sync automatically**.
2. Settings → Connectors → Add custom connector → `https://mcp.fluint.io/mcp`, then sign in with Fluint.

**ChatGPT / Codex (workspace admin):**
1. Admin → Plugins → Add → Import marketplace → `https://github.com/Fluint-io/skills`.
2. Add `https://mcp.fluint.io/mcp` as a connector and sign in with Fluint.

## 4. Getting started

New skills load in a new session. Tell the user to start one (or restart Claude Code), then put this in your final reply, copied as-is:

~~~text
Olli and Loop are installed.

Try one:
1. /olli:chat Talk a deal through with Olli.
2. /loop:plays Help me figure out what this deal needs next.
3. /loop:call-prep Prep me for my next call.
4. /loop:advance Why is my biggest open deal stuck?
5. /loop:business-case Build the business case for my top deal.

Or just describe the deal in your own words. The right play picks itself.
~~~
