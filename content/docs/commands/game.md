---
title: "/game — per-game actions"
summary: "Schedule a game time or delete a game thread."
weight: 70
---

`/game` is a small subcommand group (`/game <sub>`) for actions on an individual,
already-provisioned game. Both subcommands operate on a specific game within a
season; `season` defaults to the league's active season.

## `/game schedule_time`

**Syntax:** `/game schedule_time <league> <game> <scheduled_at> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `game` | yes | The game to schedule (autocompleted). |
| `scheduled_at` | yes | Kickoff time, UTC ISO-8601. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Member.

**What it does:** Sets (or updates) a game's scheduled kickoff time.

**Notes:** The same action is also available as a button on the game thread itself
(the "Schedule Game" button on the game-thread starter message).

## `/game delete_thread`

**Syntax:** `/game delete_thread <league> <game> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `game` | yes | The game whose thread to delete (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Deletes the game's Discord thread.

**Notes:** This deletes the thread only — it does not delete the underlying game
record or any recorded result. See {{< relref "/docs/commands/season" >}}
`/season result` for recording results.
