# Data Sourcing

Every skill runs on real deal context. Here is how it gathers that context, in what order, and what happens when something is missing.

## Loop is the only source

Every skill reads deal context from the Loop MCP from [Fluint](https://www.fluint.io) (`mcp.fluint.io`), and nothing else. Loop already fuses your CRM, calls, and emails into deal, meeting, email, and activity briefs, so it holds the real language of a deal.

1. **`find_briefs`** — the skill asks its question in plain words. No ids or object types needed.
2. **`get_brief`** — it reads the few briefs that matter for the play in full.
3. **`get_record`** — it pulls a raw record (an amount, a close date, a verbatim line) only by a ref from a brief's `source_records`.

Every brief carries `covers_through`, and the skills say how fresh it is.

The skills do not read other CRM, call-recording, or email tools, even if they are connected. If Loop is not connected, the skill stops and tells you how to connect it.

## What the skills do with the context

- **They mine for verbatim language.** The skills are scribes, not spin doctors. They capture the exact words the buyer used for their problem, their metric, their deadline, and build the output with those.
- **They preserve the customer's words.** The governing rule is camouflage, not a billboard. Output is written to sound like it came from inside the buyer's company.

## When a source is missing

The skills never invent a fact. When a number, a name, or a source is missing, they do two things:

1. **Flag it inline** as `[MISSING: ...]`, so you can see exactly what is unverified before you send anything.
2. **Turn the gap into a move.** Instead of a vague "get more data," the skill names the single highest-leverage way to close it: the one question, to the one person, at the next touchpoint.

A flagged gap is not a failure. It is the next thing to go get, and often the most valuable output of the run.

## A note on privacy

The skills read the deal context you give them access to and produce output in your chat. They do not send your data anywhere on their own. Connecting Loop is something you do in Claude's own settings, and Loop only ever shows you your own organization's briefs.
