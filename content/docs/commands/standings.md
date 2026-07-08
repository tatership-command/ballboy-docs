---
title: "/standings — standings view"
summary: "Show conference standings in Discord."
weight: 50
---

`/standings` is a single top-level command — not a subcommand group. It renders
conference standings (teams grouped by conference, ranked by record) as a public
embed.

## `/standings`

**Syntax:** `/standings <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to show (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Viewer (any member with read access to the league).

**What it does:** Posts the current standings publicly in the current channel:
each conference's teams ranked by wins/losses (and win percentage), with team logos
where resolvable. Non-playable placeholder teams are excluded.

**Notes:** See {{< relref "/docs/commands/season" >}} `/season status` for the
season's current phase and week, and {{< relref "/docs/commands/schedule" >}} for a
single week's games.
