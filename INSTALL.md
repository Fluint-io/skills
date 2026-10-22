---
name: uncommon-sales-skills-setup
description: Install the Uncommon Sales Skills plugin and connect the Loop MCP.
---

# Install Uncommon Sales Skills

Eleven enterprise sales plays (`/loop-*`) that run on your live deal data through Loop, Fluint's MCP.

https://github.com/Fluint-io/uncommon-sales-skills

You are an agent following these steps for the user. Run the commands yourself; only hand a step to the user when it needs their browser or an admin console.

## 1. Find the host

Run alone:

~~~bash
claude --version
~~~

If it prints a version, you are in Claude Code: do steps 2 and 3. If not, skip to "Other hosts".

## 2. Install the plugin (Claude Code)

~~~bash
claude plugin marketplace add Fluint-io/uncommon-sales-skills
claude plugin install uncommon-sales-skills@uncommon-sales-skills
~~~

Already installed? Update instead of reinstalling:

~~~bash
claude plugin marketplace update uncommon-sales-skills
~~~

If the user still has the original `nnasrall/uncommon-sales-skills` marketplace, that copy has the old skill names (`call-prep`, `sales-plays`, ...). Remove it first with `claude plugin marketplace remove uncommon-sales-skills`, then add this one.

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

Loop is required. It is the only data source the skills use, and they stop if it is not connected. If the user has no Fluint account, tell them they need one before the skills will work.

## Other hosts

You cannot install these yourself. Give the user these steps verbatim.

**Claude app (claude.ai, desktop):**
1. Customize → Plugins → Add marketplace → `Fluint-io/uncommon-sales-skills`. Install **Uncommon Sales Skills** and turn on **Sync automatically**.
2. Settings → Connectors → Add custom connector → `https://mcp.fluint.io/mcp`, then sign in with Fluint.

**ChatGPT / Codex (workspace admin):**
1. Admin → Plugins → Add → Import marketplace → `https://github.com/Fluint-io/uncommon-sales-skills`.
2. Add `https://mcp.fluint.io/mcp` as a connector and sign in with Fluint.

## 4. Getting started

New skills load in a new session. Tell the user to start one (or restart Claude Code), then put this in your final reply, copied as-is:

~~~text
Uncommon Sales Skills is installed. Eleven plays, each ending in something you can send.

Try one:
1. /loop-plays Help me figure out what this deal needs next.
2. /loop-call-prep Prep me for my next call.
3. /loop-advance Why is my biggest open deal stuck?
4. /loop-business-case Build the business case for my top deal.

Or just describe the deal in your own words. The right play picks itself.
~~~
