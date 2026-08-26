---
title: "Seasons & the phase calendar"
summary: "How seasons progress through the fixed phase calendar from preseason to offseason."
weight: 20
---
<!-- Grounding: verified against production commit 5ed70abd (v1.0.64,
     ballboy-00195-t6j), src/discord/season_calendar.rs (the CALENDAR table,
     RegularSeasonLength/regular_season_length_from_setting,
     PhaseActor/phase_requires_league_user_action — ADR 0027 landed: every
     phase except the terminal, unreachable Completed is PhaseActor::
     LeagueUsers) and src/data/services.rs (the Ready-to-Advance embed gate
     at the "Games"/header-only announcement build site, ADR 0028's
     materialized week_pre sentinel). Also CLAUDE.md (Season phase calendar
     and mode-branched advance/rollback; Manual season rollover; One-step
     Offseason rollover; Slice 2 — Import gates; CFP 12-team bracket
     auto-progression; per-season Conference Championship week setting; Ready
     to Advance / ADR 0023 amendment); spec 20-season-phase-calendar.md. -->

A manual-mode season moves through a fixed sequence of phases — from Preseason,
through the regular season, conference championships, and bowl weeks, into a run of
offseason phases — before completing and rolling straight into next year's season.

## What it is

The phase calendar is the ordered list of stages every manual-mode season passes
through: Preseason → Week 0 through Week 15 (the regular season) → Conference
Championships → Bowl Week 1 through 4 → a sequence of offseason phases (season
recap, players leaving, offseason recruiting, national signing day, training
results, offseason) → Completed. This calendar is fixed by the bot, not derived
from whatever games happen to be imported. EA-mode seasons don't use it — they
advance by the companion export's own week index instead (see
{{< relref "/docs/concepts/ea-vs-manual" >}}).

## Key ideas

- **The calendar order is fixed by default, but the regular-season length is a
  per-season setting.** Every manual season follows the same sequence of phases in
  the same order — except that a season can be configured to run its regular
  season 15 weeks instead of the default 16, to match a game-specific quirk where
  Conference Championship week lands one week earlier than Ball Boy's default
  assumption. This is set from the Activity's schedule builder, not a slash-command
  option; the effect is that Conference Championships (and everything after it)
  shifts one week earlier for that season only.
- **A season completes only by advancing past the terminal Offseason phase.**
  Running out of imported weeks does not complete a season on its own — you keep
  advancing through the calendar until you pass the last offseason phase.
- **Import gates block advance, they don't skip it.** A few phase transitions
  require games to already be imported before you can move into them: entering
  Week 0 requires at least one regular-season game; entering Conference
  Championships requires a Week 18 game; entering Bowl Week 1 requires both a Week
  19 and a Week 20 game. Trying to advance without them returns a message telling
  you what to import with `/season schedule` — nothing is mutated.
- **Every phase — including Preseason — posts a public weekly announcement with a
  Ready to Advance button.** Team owners toggle themselves Ready/Not Ready on that
  button; it's informational for the Commissioner deciding when to advance, not a
  gate that blocks `/season advance` on its own. This applies to every phase in the
  calendar except the terminal Completed phase (which is never actually reached by
  a live season — advancing past Offseason triggers rollover into next year's
  season instead of landing on Completed).
- **Completing a season triggers rollover, not a dead end.** A single
  `/season advance` from the terminal Offseason phase (or on an
  already-completed, still-active manual season) both finishes the old season and
  creates next year's season in one step: the new season is seeded with all 143
  template teams, every human-owned team carries over to its equivalent team key
  with its record reset to 0-0, and the league's active season pointer moves to the
  new season.
- **The 12-team playoff bracket fills itself in.** For leagues using the postseason
  CFP bracket, Ball Boy auto-generates the quarterfinal, semifinal, and
  championship matchups from the prior round's results as you advance through the
  bowl weeks — you only import the first round and quarterfinal games; the
  semifinals and championship are built automatically. A round can't advance past a
  tied game — CFP games require a decisive score. The bracket's byes are fixed: the
  1-seed's bye slot is filled by the winner of the 8-vs-9 first-round game, the
  2-seed's by the winner of 7-vs-10, the 3-seed's by the winner of 6-vs-11, and the
  4-seed's by the winner of 5-vs-12. Once the quarterfinals are done, the two
  semifinal games are automatically named after New Year's Six bowls (Rose, Sugar,
  Orange, Cotton, Peach, Fiesta) that weren't already used as quarterfinal bowl
  names, in that order.

## Phase-to-week-key reference

Commands that take an explicit week — `/schedule week` and
{{< relref "/docs/commands/game" >}} `/game schedule_time` among them — use the
week key from this table, not the phase label:

| Phase | Week key(s) |
|---|---|
| Preseason | `week_pre` |
| Regular season (Weeks 0–15) | `week_00` through `week_15` |
| *(reserved gap — no phase)* | `week_16`, `week_17` |
| Conference Championships | `week_18` |
| Bowl Week 1 of 4 | `week_19` |
| Bowl Week 2 of 4 | `week_20` |
| Bowl Week 3 of 4 | `week_21` |
| Bowl Week 4 of 4 | `week_22` |
| Offseason phases (recap, players leaving, recruiting, signing day, training, offseason) | `week_23` through `week_31` |

`week_16` and `week_17` are intentionally unused — the calendar jumps straight
from `week_15` to Conference Championships (`week_18`), **unless** the season is
set to the 15-week regular-season length above, in which case the boundary is one
week earlier (`week_14` → Conference Championships).

## How it behaves

`/season advance` moves a manual-mode season exactly one step along the calendar
(unless it's the completion→rollover case above). `/season status` shows the
season's current phase (a friendly label, e.g. "Preseason"), an activity
description, and the current week — the **week** line shows the raw week key
verbatim (`week_pre`, `week_05`, and so on), not a friendly label, so don't be
surprised to see `week_pre` there during preseason. It also shows an import-gate
hint when the next phase needs a schedule import first. `/season rollback` moves
one step backward — but it's blocked once a season is completed; at that point
advancing (which triggers rollover) or deleting the season are the only ways
forward.

## Related commands

- {{< relref "/docs/commands/season" >}} — `advance`, `status`, `schedule`, and
  `rollback` all interact with phase state directly.
- See {{< relref "/docs/flows" >}} for the end-to-end auto-advance walkthrough.
- See {{< relref "/docs/concepts/ea-vs-manual" >}} for how EA mode differs.
