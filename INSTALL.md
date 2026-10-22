---
name: olli-loop-setup
description: Install Olli and the Loop plays, and connect the Loop MCP.
---

# Install Olli and Loop

Olli, Fluint's AI sales agent (`/fluint:olli`), and eleven Loop sales plays (`/fluint:*`), all running on your live deal data through Loop, Fluint's MCP.

https://github.com/Fluint-io/skills

You are an agent following these steps for the user. Run the commands yourself; only hand a step to the user when it needs their browser or an admin console.

## In a chat app? Read this first, then stop.

If you cannot run shell commands, you are in a chat app: claude.ai, the Claude desktop or mobile app, ChatGPT, or Grok (grok.com and the Grok apps). Everything after this section is for terminal agents (Claude Code, Grok Build) only. Do not run, show, or summarize any of it, including its starter message and its slash commands.

If you are Claude or ChatGPT, reply with only the block for the app you are running in, copied as-is. Add nothing before or after it, and never show the other app's block. Before you send it, check your own tools: if Loop tools (for example `find_briefs`) are already available in this chat, drop the connector step and renumber.

**If you are Claude** (claude.ai, the Claude desktop or mobile app):

~~~text
I can't install plugins from inside a chat, but it takes about a minute in settings:

1. Settings → Customize → Plugins → Add, and link the GitHub repo Fluint-io/skills. Then add "Olli & Loop by Fluint" from the Discover tab.
2. Settings → Connectors → Add custom connector → https://mcp.fluint.io/mcp, then sign in with your Fluint account.

Then start a new chat and ask for what you need, for example:
• "Let me talk to Olli about the Acme deal."
• "Prep me for my next call."
• "Why is my biggest open deal stuck?"
• "Build the business case for my top deal."
~~~

**If you are ChatGPT:**

~~~text
Olli and Loop are added to ChatGPT by a workspace admin:

1. Admin → Plugins → Add → Import marketplace → https://github.com/Fluint-io/skills.
2. Add https://mcp.fluint.io/mcp as a connector, then sign in with your Fluint account.

Once your admin has done that, start a new chat and ask for what you need, for example:
• "Let me talk to Olli about the Acme deal."
• "Prep me for my next call."
• "Why is my biggest open deal stuck?"
• "Build the business case for my top deal."
~~~

**If you are Grok** (grok.com, the Grok apps), do the setup yourself instead of replying with a block:

1. **Loop.** If Loop tools (for example `find_briefs`) are already available in this chat, skip this. Otherwise tell the user: go to grok.com/connectors, choose New Connector, then Custom, enter `https://mcp.fluint.io/mcp`, and sign in with their Fluint account.
2. **Skills.** Fetch each file below and save it as one of your skills. Use the `name` in the file's frontmatter as the skill name and the whole file as its content. Each file is self-contained, with its reference material included. If a skill with that name already exists, replace it.

- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/olli.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-plays.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-call-prep.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-follow-up.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-multithread.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-account-plan.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-champion.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-displace.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-business-case.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-advance.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-qbr.md
- https://raw.githubusercontent.com/Fluint-io/skills/main/grok/skills/loop-manage-up.md

3. **Clean up.** Delete any skills from earlier versions with these names: `sales-plays`, `multithread`, `account-planning`, `call-prep`, `call-follow-up`, `champion-enablement`, `competitive-displacement`, `deal-advancement`, `qbr-prep`, `manage-up`, `one-page-business-case`.
4. If you cannot save skills yourself, tell the user to add each file above in Grok's Skills settings instead.
5. Then reply with only this, copied as-is (drop the connector line if Loop was already connected):

~~~text
Olli and the Loop plays are saved as skills in Grok.

If Loop isn't connected yet: grok.com/connectors → New Connector → Custom → https://mcp.fluint.io/mcp, then sign in with Fluint.

Start a new chat and ask for what you need, for example:
• "Let me talk to Olli about the Acme deal."
• "Prep me for my next call."
• "Why is my biggest open deal stuck?"
• "Build the business case for my top deal."

These are copies, so they don't update themselves. To update, paste the install line again.
~~~

---

# Claude Code

## 1. Confirm Claude Code

Run alone:

~~~bash
claude --version
~~~

If it prints a version, do steps 2 to 4. If not, run `grok --version`: if that prints a version, you are in Grok Build, so go to "Grok Build" at the end. If neither works, go back to "In a chat app?" at the top and follow only that.

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

Before 1.3.0, Olli and the plays were two plugins, `olli` (`/olli:chat`) and `loop` (`/loop:...`). They are now one plugin, `fluint` (`/fluint:olli`, `/fluint:call-prep`, ...). Remove the old ones; each may report that nothing is installed:

~~~bash
claude plugin uninstall olli@fluint
claude plugin uninstall loop@fluint
~~~

Then install:

~~~bash
claude plugin marketplace add Fluint-io/skills
claude plugin install fluint@fluint
~~~

One plugin, one prefix: `/fluint:olli` for Olli and `/fluint:<play>` for the plays (`/fluint:call-prep`, `/fluint:business-case`, ...). Olli runs the plays for deliverables.

Already on `fluint`? Update instead of reinstalling:

~~~bash
claude plugin marketplace update fluint
claude plugin update fluint@fluint
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

## 4. Getting started (Claude Code only)

New skills load in a new session. Tell the user to start one (or restart Claude Code), then put this in your final reply, copied as-is:

~~~text
Olli and Loop are installed.

Try one:
1. /fluint:olli Talk a deal through with Olli.
2. /fluint:plays Help me figure out what this deal needs next.
3. /fluint:call-prep Prep me for my next call.
4. /fluint:advance Why is my biggest open deal stuck?
5. /fluint:business-case Build the business case for my top deal.

Or just describe the deal in your own words. The right play picks itself.
~~~

---

# Grok Build

Grok Build reads Claude Code marketplaces, plugins, and MCP servers. If the user already set up Olli and Loop in Claude Code on this machine, they may already be available: check Grok's Marketplace tab before installing anything.

If the old `olli` or `loop` plugins (from before 1.3.0) are installed, remove them first, in Grok Build and in Claude Code, since Grok reads both. Each command may report that nothing is installed:

~~~bash
grok plugin uninstall olli --confirm
grok plugin uninstall loop --confirm
claude plugin uninstall olli@fluint
claude plugin uninstall loop@fluint
~~~

Then, unless `fluint` is already available, add the marketplace and install the plugin. Grok installs by plugin name, and stops before installing unless `--trust` is given:

~~~bash
grok plugin marketplace add Fluint-io/skills
grok plugin install fluint --trust
~~~

If the Plugins tab then shows `fluint` as off, enable it there.

If these commands are not recognized, open the Marketplace tab in Grok Build's TUI, add `Fluint-io/skills`, and install **fluint** there (or tell the user to).

For Loop, Grok Build uses MCP servers configured for Claude Code. If no Loop server is available, add `https://mcp.fluint.io/mcp` as a remote MCP server and have the user sign in with their Fluint account.

Then reply with the same starter message as step 4 of the Claude Code section, and tell the user to start a new Grok session.
