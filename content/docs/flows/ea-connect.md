---
title: "Connecting a league to EA"
summary: "The end-to-end flow for moving a league from manual mode to EA companion mode with /league attach_ea."
weight: 5
---
<!-- Grounding: CLAUDE.md (Companion tenant provisioning; Companion GCS
     consumption; EA-connection access pattern; EA-mode predicate);
     spec 04-ea-ingest.md; src/discord/commands.rs (attach_ea). -->

Ball Boy leagues start in manual mode, where you enter schedules and results
yourself. `/league attach_ea` is the one command that flips a league into **EA
companion mode**, where teams, schedules, and results arrive automatically from
the EA companion app instead. This flow covers what you need before you run it,
what happens after, and how to tell it's actually working.

## Prerequisites

- A league already created with {{< relref "/docs/commands/league" >}}
  `/league create` — `attach_ea` connects an *existing* league, it doesn't create
  one. There's no flag on `create` that puts a new league straight into EA mode.
- Commissioner access on that league.
- The EA companion app (or whatever tool your league uses to push companion
  exports) configured to upload for the platform and EA league you're about to
  connect.

## Step by step

1. **Run `/league attach_ea <league> <platform> <ea_league_id> [ea_league_name]
   [game]`.** `platform` is a free-text field — pass whatever platform slug your
   companion export uploads under (the command's own option hint gives `ps5`,
   `xbsx`, and `pc` as examples). `ea_league_id` is the EA companion league id —
   the same id the companion app's upload path is keyed on. Both are required and
   can't be blank. `ea_league_name` is an optional friendly label, and `game` lets
   you override the release game if it isn't already set on the league.
2. **Ball Boy records the connection and provisions a companion upload target.**
   Two things happen: an `EaConnectionDoc` is written recording the
   `(game, platform, ea_league_id)` mapping, and a GCS tenant marker is written
   so the companion pipeline knows this league is allowed to upload. Because this
   does external I/O, the command acknowledges the interaction before it finishes
   (you won't see an instant reply).
3. **From this point, the league is in EA mode.** This is the only command that
   flips the mode — every other part of Ball Boy checks the same underlying
   connection to decide how to behave, rather than treating EA leagues as a
   separate kind of league.
4. **The companion app uploads exports for this league.** Uploads land at
   `v1/{game}/{league_id}/{platform}/{ea_league_id}/...` in Ball Boy's companion
   GCS bucket — the tenant marker from step 2 is what makes that path valid for
   this league.
5. **Ball Boy's scheduler tick picks the exports up.** A periodic tick calls the
   companion-consumption pipeline, which lists new objects, guards against
   reading a payload that's still being written (a torn read), dedupes by content
   hash so a re-uploaded or replayed export never gets processed twice, and
   normalizes whatever it finds — league teams, standings, rosters, week
   schedules, and week stats — into Ball Boy's own team, game, and season
   records.
6. **Discord side effects follow automatically.** A schedules export showing a
   higher week than the season's current week triggers an idempotent advance
   (archiving the old week's threads, opening the new week's); a schedules export
   showing a final score for a game settles that game the same way a manual
   result would — updating the thread, posting to the results channel if one's
   configured, and archiving+locking the thread.

## What changes day to day

Once a league is in EA mode:

- **No more manual schedule import.** `/season schedule` is for manual-mode
  leagues only — an EA league's schedule comes from the companion export.
- **No more manual result entry.** `/season result` is manual-mode only too;
  results are settled automatically as the companion app uploads score data.
- **Team seeding is automatic.** EA-mode leagues don't get the 143-template
  manual seed on `/season create` — teams arrive from the companion export.
- **Advance still works the same way from your side** — `/season advance` (or the
  `@everyone` auto-advance trigger) still exists and still posts the same kind of
  advance announcement, but the underlying mechanics track the companion export's
  own week index rather than a fixed phase calendar.

See {{< relref "/docs/concepts/ea-vs-manual" >}} for the full comparison of what
differs between the two modes.

## Troubleshooting

- **Nothing shows up after attaching.** Data only appears once the companion app
  has actually uploaded something for this `(platform, ea_league_id)` pair, and
  only after the next scheduler tick processes it — there's no immediate backfill
  at attach time. Double-check the platform and EA league id you attached with
  match exactly what the companion app is uploading under.
- **The connection itself seemed to fail or time out.** The tenant-marker write
  is best-effort; a failure there doesn't fail the command, but the companion app
  may not be able to upload until it's retried. If `/league attach_ea` returned
  an outright error rather than a success reply, nothing was connected — retry
  the command.
- **A game or score seems to be missing or stale.** Ball Boy skips objects that
  look like a torn read (the export bytes and its metadata don't yet agree on
  size) rather than processing a half-written upload — this resolves itself on
  the next tick once the upload finishes. Repeated uploads of identical data are
  deduped and never double-apply.

Related: {{< relref "/docs/commands/league" >}} `/league attach_ea`;
{{< relref "/docs/concepts/ea-vs-manual" >}}.
