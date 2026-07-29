---
title: "/game — per-game actions"
summary: "Schedule a game time or delete a game thread."
weight: 70
---

`/game` is a small subcommand group (`/game <sub>`) for actions on an individual,
already-provisioned game. Both subcommands operate on a specific game within a
season; `season` defaults to the league's active season.

## `/game schedule_time`

**Syntax:** `/game schedule_time <league> <game> <date> <time> <timezone> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `game` | yes | The game to schedule (autocompleted). |
| `date` | yes | Game date, `YYYY/MM/DD` (also accepts `YYYY-MM-DD`). |
| `time` | yes | Kickoff time, 24-hour `HH:MM` (e.g. `20:00` for 8:00 PM). |
| `timezone` | yes | Choice — the game's local timezone, from a dropdown: Newfoundland (NT), Atlantic (AT), Eastern (ET), Central (CT), Mountain (MT), Arizona (MST, no DST), Pacific (PT), Alaska (AKT), Hawaii (HST, no DST), or UTC. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Member.

**What it does:** Sets (or updates) a game's scheduled kickoff time. You give the
date, time, and timezone as the people in your league would say them — Ball Boy
converts that to UTC itself, so there's no UTC math for you to do. You can't
schedule a game in the past.

**Notes:** The same action is also available as the 📅 **Schedule Game** button on
the game-thread starter message, which opens a modal with the same three fields
— but its timezone field is free text rather than a dropdown, since a Discord
modal can't show a select menu here; it accepts the zone name, its display label
(e.g. `Eastern (ET)`), or a common abbreviation (`ET`, `CT`, `MT`, `PT`, `AT`,
`NT`, `AKT`, `HST`, `MST`, `UTC`), case-insensitive. Daylight-saving edge cases
are handled deliberately: a time that's ambiguous because clocks are falling
back resolves to the earliest of the two possible UTC instants, while a time
that doesn't exist because clocks are springing forward is rejected with an
error naming the timezone rather than being silently shifted. The scheduled
kickoff is shown as a Discord dynamic timestamp, so everyone sees it converted
to their own local time automatically, and a public note is also posted in the
game thread so both teams see the scheduled time, not just whoever ran the
command.

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
