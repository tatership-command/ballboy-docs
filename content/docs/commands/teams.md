---
title: "/teams — roster board"
summary: "Show the league roster board as a card-stack embed."
weight: 40
---

`/teams` is a single top-level command — not a subcommand group. It renders the
league's roster board as a public "card stack" message: one card per conference
(claimed teams grouped and ranked), plus a header card and, if any members are
waitlisted, a waitlist card.

## `/teams`

**Syntax:** `/teams <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to show (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Viewer (any member with read access to the league).

**What it does:** Posts the roster board publicly in the current channel — a
multi-embed card stack showing every conference's claimed teams (with owner
mentions and, where linked, in-game profile handles), plus a waitlist card when the
waitlist is non-empty. This is an **on-demand** render; it is separate from the
league's optional **persistent** roster board (configured via
{{< relref "/docs/commands/admin" >}} `/admin channels roster_board`), which
auto-refreshes on ownership changes instead of requiring a manual `/teams` call
each time.

**Notes:** See {{< relref "/docs/commands/team" >}} for how members claim teams
shown on this board, and {{< relref "/docs/commands/waitlist" >}} for waitlist
management.
