---
title: "EA mode vs manual mode"
summary: "How a Ball Boy league runs in EA companion mode versus manual mode, and what differs between them."
weight: 10
---
<!-- Grounding: CLAUDE.md (EA-mode predicate; Companion tenant provisioning;
     Companion GCS consumption; /league attach_ea; Manual-season auto-seed;
     Season phase calendar and mode-branched advance/rollback); spec
     04-ea-ingest.md; spec 20-season-phase-calendar.md. -->

Every Ball Boy league runs in one of two modes — **manual** or **EA companion** —
and the mode decides where a season's teams, schedule, and results come from. It's
a single check the bot makes everywhere it needs to branch, not a different kind of
league.

## What it is

A league starts in manual mode by default. It moves into EA mode only by running
`/league attach_ea` — that is the *only* way a league ever enters EA mode; there is
no flag on `/league create` for it. From that point on, the league's active season
pulls its data from whatever the EA companion app uploads, instead of from manual
commands.

## Key ideas

- **One predicate, checked everywhere.** Whether a league is in EA mode is a single
  runtime check, not a separate season type — the same season document shape works
  in both modes.
- **`/league attach_ea` is the sole entry point into EA mode.** Running it writes a
  companion-export upload target and a connection record; because that's external
  I/O, the command acknowledges the interaction before it finishes.
- **The two modes diverge on data source, not on what a season *is*.** Both modes
  still have phases, weeks, games, and standings — they just get filled in
  differently.

## How it behaves

- **Team seeding.** In manual mode, `/season create` immediately seeds all 143
  template teams (138 FBS programs plus 5 non-playable FCS placeholders) as
  CPU-owned teams, ready for `/team claim`. EA-mode leagues skip this step
  entirely — their teams arrive from the companion export instead.
- **The bundled team dataset is College Football, regardless of the league's
  game.** Ball Boy ships a single set of team templates — the 143-team College
  Football dataset described in
  {{< relref "/docs/concepts/teams-and-conferences" >}} — and manual-mode seeding
  always draws from it. A manual-mode **Madden** league still gets seeded with
  those same 143 College Football teams; there is no separate Madden team dataset
  yet. This is a known limitation for manual-mode Madden leagues today — an
  EA-mode Madden league is unaffected, since its teams come from the companion
  export instead of the bundled templates.
- **Schedule source.** Manual mode imports its schedule via `/season schedule` (a
  CSV upload). EA-mode leagues get their schedule automatically from the companion
  export and can't use `/season schedule`.
- **Results.** Manual mode results are entered with `/season result`. EA-mode
  results are ingested automatically as the companion app uploads new payloads —
  there's no manual entry step for them.
- **Advance and rollover.** Both modes advance with `/season advance`, but the
  mechanics differ: an EA-mode season advances by the companion export's own week
  index, while a manual-mode season advances through a fixed phase calendar (see
  {{< relref "/docs/concepts/seasons-and-phases" >}}) and can be blocked by an
  "import gate" until the operator imports the next phase's games.

## Related commands

- {{< relref "/docs/commands/league" >}} — `/league attach_ea` is the only way into
  EA mode.
- {{< relref "/docs/commands/season" >}} — `/season create`, `/season schedule`,
  `/season result`, and `/season advance` all branch by mode.
- See {{< relref "/docs/flows" >}} for end-to-end walkthroughs.
