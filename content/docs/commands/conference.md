---
title: "/conference — realignment"
summary: "Move a team into a different conference, one at a time or in bulk."
weight: 130
---

`/conference` is a subcommand group (`/conference <sub>`) for moving an
already-seeded team into a different one of Ball Boy's canonical conferences —
useful when the underlying game's realignment doesn't match your league, or
changes mid-cycle. FCS is never a valid destination for either subcommand.

## `/conference assign`

**Syntax:** `/conference assign <league> <team> <target_conference> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to move (autocompleted). |
| `target_conference` | yes | The conference to move it into: ACC, Big 12, Big Ten, Conference USA, Independent, MAC, Mountain West, Pac-12, SEC, Sun Belt, or The American. FCS is not selectable. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Moves one team into the chosen conference. The move updates the
live season right away and is saved as a per-league override, so it survives
future seasons and {{< relref "/docs/commands/admin" >}} `/admin reload_teams`.

**Notes:** This doesn't touch existing Discord roles on its own — run
{{< relref "/docs/commands/admin" >}} `/admin roles_sync_all` afterward to move
the affected owner to their new conference role.

## `/conference manage`

**Syntax:** `/conference manage [league]`

| Option | Required | Description |
|---|---|---|
| `league` | no | The league (autocompleted). Omit if this server only has one league. |

**Who can run it:** Commissioner.

**What it does:** Opens a paginated, ephemeral picker in Discord for moving
several teams at once: pick a conference to move teams **out of**, check the
teams you want (selections carry across pages, up to 25 teams per page), choose
the destination conference, and apply. After applying, the picker resets so you
can immediately process another source conference in the same session.

**Notes:** Same underlying move as `/conference assign`, applied per team — the
same live-update, persistence, and "run `/admin roles_sync_all` afterward" notes
apply. The picker session expires after 10 minutes of inactivity.
