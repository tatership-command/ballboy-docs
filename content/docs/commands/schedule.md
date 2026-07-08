---
title: "/schedule — schedule view"
summary: "Show a single week's schedule in Discord."
weight: 60
---

`/schedule` is a single top-level command — not a subcommand group. It renders one
week's games (completed with scores, scheduled with kickoff time, or unscheduled)
as a public embed.

## `/schedule`

**Syntax:** `/schedule <league> [season] [week]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to show (autocompleted). |
| `season` | no | Defaults to the league's active season. |
| `week` | no | A week key, e.g. `week_05` or `postseason`. Defaults to the season's current week. |

**Who can run it:** Viewer (any member with read access to the league).

**What it does:** Posts that week's schedule publicly in the current channel.
Completed games show the final score (home team first); scheduled games show the
kickoff time; unscheduled games show as unscheduled. Team logos are shown where
resolvable.

**Notes:** Members can set a specific game's kickoff time with
{{< relref "/docs/commands/game" >}} `/game schedule_time`. See
{{< relref "/docs/commands/season" >}} `/season prepare_week` for how game threads
for a week are created in the first place.
