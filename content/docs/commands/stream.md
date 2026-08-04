---
title: "/stream — stream announcements"
summary: "Announce a stream for a friendly or unscheduled game."
weight: 110
---

`/stream` is a single top-level command — not a subcommand group. It posts a 🔴
"going live" announcement for a friendly or unscheduled game — the manual
counterpart to the in-game-thread **Go Live** button.

## `/stream`

**Syntax:** `/stream [league] [opponent] [message] [profile] [voice_channel] [url] [notify] [role]`

| Option | Required | Description |
|---|---|---|
| `league` | no | The league (autocompleted). If your server has exactly one league, it's picked automatically; with more than one, Ball Boy asks you to pick. |
| `opponent` | no | An opponent to name and ping. |
| `message` | no | A free-text matchup/note, e.g. "Texas vs Oklahoma (friendly)". |
| `profile` | no | Which saved stream profile to link — `Twitch`, `YouTube`, or `Custom URL`. Omit to use your saved default, or your first linked account. |
| `voice_channel` | no | A voice or stage channel picker, for streaming inside Discord. |
| `url` | no | An explicit stream URL override — wins over `profile`/your saved links. |
| `notify` | no | Who to ping — `Everyone` or `Stream role` (the league's configured stream-notify role). Omit to ping the league's configured stream role. |
| `role` | no | An explicit role to ping — wins over `notify`. |

**Who can run it:** Any member of the league's Discord server.

**What it does:** Posts a 🔴 stream announcement to the league's configured
`streams` channel (or the current channel if none is configured), naming the
streamer and, if given, the opponent and/or matchup note, with the stream URL
and/or the voice channel. If you have an unplayed game in the current week, it
also posts a copy into that game thread and pins it there. Acknowledges the
runner with an ephemeral confirmation after the public announcement is posted.

**Notes:** You only ever get **one** stream link, never a list of every account
you've connected. Resolution order: an explicit `url` always wins; then an
explicit `profile` choice; then your saved default, if that platform is actually
linked; then whichever you have linked, preferring Twitch, then YouTube, then a
custom link. Choosing a `voice_channel` without a `profile` suppresses the link
entirely, since the voice channel is the destination. Ping resolution order: an
explicit `role` wins over `notify`, and omitting both pings the league's
configured stream role; if no stream role is configured the announcement still
posts, with a note pointing at `/admin roles`. This
reuses the same announcement plumbing as the **🔴 Go Live** button posted in each
game thread — see {{< relref "/docs/commands/game" >}} for game-thread actions,
and {{< relref "/docs/commands/admin" >}} `/admin channels` /
`/admin roles` for configuring the `streams` channel and stream role.
