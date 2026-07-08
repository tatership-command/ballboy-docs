---
title: "/stream — stream announcements"
summary: "Announce a stream for a friendly or unscheduled game."
weight: 110
---

`/stream` is a single top-level command — not a subcommand group. It posts a 🔴
"going live" announcement for a friendly or unscheduled game — the manual
counterpart to the in-game-thread **Go Live** button.

## `/stream`

**Syntax:** `/stream <league> [opponent] [message] [profile] [voice_channel] [url] [notify] [role]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `opponent` | no | An opponent to name and ping. |
| `message` | no | A free-text matchup/note, e.g. "Texas vs Oklahoma (friendly)". |
| `profile` | no | Which saved stream profile to link — `Twitch`, `YouTube`, or `Custom URL`. Omit to include all your saved links. |
| `voice_channel` | no | A voice or stage channel picker, for streaming inside Discord. |
| `url` | no | An explicit stream URL override — wins over `profile`/your saved links. |
| `notify` | no | Who to ping — `Everyone` or `Stream role` (the league's configured stream-notify role). |
| `role` | no | An explicit role to ping — wins over `notify`. |

**Who can run it:** Viewer — any member of the league.

**What it does:** Posts a 🔴 stream announcement to the league's configured
`streams` channel (or the current channel if none is configured), naming the
streamer and, if given, the opponent and/or matchup note, with the stream URL(s)
and/or the voice channel. Acknowledges the runner with an ephemeral confirmation
after the public announcement is posted.

**Notes:** Stream URL resolution order: an explicit `url` always wins; otherwise
`profile` selects a single saved link, or all saved links are used when `profile`
is omitted. Ping resolution order: an explicit `role` wins over `notify`. This
reuses the same announcement plumbing as the **🔴 Go Live** button posted in each
game thread — see {{< relref "/docs/commands/game" >}} for game-thread actions,
and {{< relref "/docs/commands/admin" >}} `/admin channels` /
`/admin roles` for configuring the `streams` channel and stream role.
