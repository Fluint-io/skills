---
name: plays
description: >-
  The front door to the Loop plays. Use this skill when a
  seller describes a deal situation but has not named a specific play, or asks
  which play they need: "help me with this deal", "what should I do next on
  [account]", "I'm stuck, not sure what I need here", "coach me through this
  deal", "which play fits", "where is this deal and what's my move". It reads the
  situation, names the deal moment, and routes to the right skill in the toolbox.
  Prefer a specific skill (fluint:call-prep, fluint:multithread, fluint:advance, etc.) when
  the seller clearly names that need; use this router only when the need is
  ambiguous or the seller wants to be pointed to the right play.
---

# Sales Plays (the front door)

## What this does

This is the router for the Loop plays. When a seller describes a deal but
has not picked a play, it figures out where the deal actually is and points to the right skill.
It exists so a rep never has to memorize ten skill names. Describe the situation, and this gets
you to the move.

If the seller has clearly named a specific need (for example "prep me for my call" or "why is
this deal stuck"), let that skill fire instead. This router is for the ambiguous case.

## Read the deal first

Before routing, read the deal from Loop (`mcp.fluint.io`), the only data source:
`find_briefs` naming it, then `get_brief` on its `deal_brief`. The `next_plays` section is what
the seller should focus on next on this deal. Read the first entry's `label` and `narrative`,
route to the play that moves it, and say so ("Loop's next play here is getting the economic
buyer engaged, so start with fluint:multithread"). If it holds only an `unsupported_reason`, or
there is no deal yet, route from the table.

If Loop is not connected, stop and tell the seller to connect it: in Claude Code run `/mcp` and
authenticate `loop`, or follow
https://raw.githubusercontent.com/Fluint-io/skills/main/INSTALL.md.

## How to route

First, get just enough context to place the deal. Ask one or two questions if the moment is
unclear: what account, what just happened or is about to happen, and what the seller is trying
to get to next. Then match to the play.

| The seller's situation | Route to |
|------------------------|----------|
| New account, or a live deal riding on one contact that needs more coverage | **fluint:multithread** |
| Needs a POV, an account plan, or wants to find expansion whitespace | **fluint:account-plan** |
| Has a call, demo, or discovery coming up and wants to walk in ready | **fluint:call-prep** |
| Just had a call or group demo and needs to follow up and lock the problem | **fluint:follow-up** |
| Needs to arm a champion to sell internally, or handle a skeptic or blocker | **fluint:champion** |
| Up against an incumbent or competitor and needs to change the game | **fluint:displace** |
| Ready to make the executive case for the deal | **fluint:business-case** |
| Deal has stalled, or needs a mutual action plan to drive to close | **fluint:advance** |
| Prepping a customer quarterly review or renewal conversation | **fluint:qbr** |
| Prepping a forecast call or deal review with their own leadership | **fluint:manage-up** |

When more than one fits, name the two most likely and let the seller pick. A deal often needs a
sequence (for example: fluint:multithread now, then fluint:call-prep for the exec meeting, then
fluint:business-case). Say so, and start with the one that unblocks the rest.

## The through-line

Every play in this toolbox runs the same way, so set the expectation up front:
- It reads the deal from Loop's briefs, and builds around the deal's top `next_plays` entry.
- It writes in the buyer's own language, built to be forwarded. Camouflage, not a billboard.
- It flags what is missing and names the one move to close the gap.
- It ends in a deliverable, plus an operator's read: the judgment a summary hides.

## Operating principles

- **Place the deal first.** A play run on the wrong moment wastes the run. One or two questions
  beats a confident guess.
- **Point, do not lecture.** Name the play and hand off. The chosen skill does the work.
- **Name the sequence.** Deals move through moments. Say what comes after the play you start with.
