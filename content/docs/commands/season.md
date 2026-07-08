---
title: "/season — season lifecycle"
summary: "Create, advance, import, inspect, and delete seasons."
weight: 20
---

`/season` is a subcommand group (`/season <sub>`). It covers the lifecycle of a
season within a league: creation, weekly advancement, schedule import, results,
status, rollback, roster reconciliation, and deletion. Every season-scoped
subcommand defaults its optional `season` option to the league's active season, so
you only need to pass it explicitly when targeting a non-active season.

## `/season create`

**Syntax:** `/season create <league> <year> [name]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to create a season for (autocompleted). |
| `year` | yes | Season year (integer). |
| `name` | no | Optional display name for the season. |

**Who can run it:** Commissioner.

**What it does:** Creates a season and sets it as the league's active season. In
**manual mode**, this also seeds all 143 template teams (138 FBS programs plus 5
generic FCS placeholders) as CPU-owned teams ready to be claimed. **EA-mode**
leagues skip this seeding step — their teams arrive from the companion export
instead. The new season starts **active**, at Preseason / Week 0.

**Notes:** Because seeding can take a moment, this command replies immediately with
a short "creating…" acknowledgment, then posts the real result once it finishes. See
{{< relref "/docs/commands/team" >}} `/team claim` for how members take ownership of
seeded teams.

## `/season status`

**Syntax:** `/season status <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Viewer.

**What it does:** Shows the season's phase, activity, and current week. For a
manual-mode season whose next phase requires an imported schedule, it also shows an
import-gate hint pointing at `/season schedule`.

## `/season result`

**Syntax:** `/season result <league> <game> <home_score> <away_score> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `game` | yes | The game to record a result for (autocompleted). |
| `home_score` | yes | Home team's final score (integer). |
| `away_score` | yes | Away team's final score (integer). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Member.

**What it does:** Manually settles a game result. This is the **manual-mode** path
— in EA mode, results arrive automatically from the companion export instead.

**Notes:** Blocked once the season is completed, and blocked for a CFP bracket game
that would end in a tie (a decisive score is required).

## `/season advance`

**Syntax:** `/season advance <league> [season] [deadline]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |
| `deadline` | no | Deadline for the next week/phase. |

**Who can run it:** Commissioner.

**What it does:** Advances the season to the next week/phase. **Branches by mode**:
EA-mode seasons advance from the companion export's week index; manual-mode seasons
advance through a fixed phase calendar (regular weeks, conference championship,
bowl weeks, offseason) and are blocked from advancing into a phase whose games
haven't been imported yet (see `/season schedule` below). A completed manual season
rolls over into a brand-new season in one step.

**Notes:** Uses the immediate-ack handoff pattern — it replies right away and posts
progress/completion as follow-up messages rather than making you wait on a spinner.
This same advance logic is also triggered by an `@everyone`/announce-role ping in
the configured auto-advance channel; see {{< relref "/docs/commands/admin" >}}
`/admin auto_advance`.

## `/season prepare_week`

**Syntax:** `/season prepare_week <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Provisions the current week's game threads and posts the weekly
digest/announcement.

## `/season schedule`

**Syntax:** `/season schedule <league> <file> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `file` | yes | A CSV attachment with the schedule to import. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Imports a schedule CSV. **Manual mode only** — EA-mode leagues
get their schedule from the companion export and cannot use this command.

**Notes:** Also uses the immediate-ack handoff pattern: it acknowledges immediately,
then posts a "Schedule Import Results" embed once the import finishes (games
written, any skipped rows with reasons). Blocked on a completed season.

## `/season rollback`

**Syntax:** `/season rollback <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Server admin and Commissioner (both gates apply — a Discord
Administrator who is not also the league's Commissioner is still denied).

**What it does:** Rolls the season back one week/phase. Blocked on a completed
season — the only ways out of a completed season are advancing (which triggers
rollover into a new season) or deleting it.

## `/season sync_teams`

**Syntax:** `/season sync_teams <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Add-absent-only reconcile: seeds any template teams missing from
the season's roster (for example, teams added by a mid-season realignment update).
It never overwrites an existing team — claimed teams and their records are always
preserved.

## `/season delete`

**Syntax:** `/season delete <league> <season>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | **yes — no default** | The season to delete; unlike other season subcommands, this does **not** default to the active season. |

**Who can run it:** Server admin and Commissioner (both gates apply).

**What it does:** Shows a danger-confirm button; on confirmation, cascade-deletes
the entire season — teams, weeks, games, players, stats. This is destructive and
cannot be undone.
