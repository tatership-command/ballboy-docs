---
title: "Streaming & Go Live"
summary: "How stream announcements work — presence auto-detect, the Go Live button, and /stream."
weight: 50
---
<!-- Grounding: CLAUDE.md (Stream auto-detect via Discord presence — Part B;
     Go Live click handler — Part A; "/stream" ad-hoc stream announcement —
     Part C; announce_stream_to_channels); src/discord/handler.rs
     (go_live_guard_game_already_played, go_live_guard_non_owner_rejected). -->

Ball Boy has three ways to let your league know you're streaming a game: it can
detect your Discord presence automatically, you can click a Go Live button right
in the game thread, or you can post an announcement manually with `/stream` for a
friendly or unscheduled game.

## Prerequisites

- For presence auto-detect: a server admin needs to configure
  {{< relref "/docs/commands/admin" >}} `/admin stream` (title keywords and/or an
  exact game-category match) and Ball Boy needs the **Presence** privileged
  Discord gateway intent enabled.
- For the Go Live button: an unplayed, provisioned game thread, and you need to
  be one of the two teams' owners in that game.
- For any of the three to reach an audience: a `streams` channel and/or a
  stream-notify role configured via {{< relref "/docs/commands/admin" >}}
  `/admin channels` / `/admin roles`. Without a `streams` channel, announcements
  post in the current channel instead.

## Step by step

**Presence auto-detect:**

1. A member starts streaming from their console or PC with Discord presence
   sharing on, and their stream title (and/or game category) matches the
   league's configured keywords/category.
2. Ball Boy checks whether that member owns a team with an unplayed game in the
   season's current week.
3. If so, and this is the first time this session for that member+game pairing,
   Ball Boy posts the announcement automatically — no action needed from the
   streamer.

**The Go Live button:**

1. In an unplayed game thread, either team owner clicks the **🔴 Go Live** button.
2. Ball Boy posts the announcement to the thread (and to the `streams` channel, if
   configured), pinging the opponent, using the stream URL saved on the clicker's
   profile if one is set.
3. The clicker gets an ephemeral acknowledgment.

**Manual `/stream`:**

1. Run {{< relref "/docs/commands/stream" >}} `/stream <league>` with any
   combination of an opponent to ping, a free-text matchup note, which saved
   stream link to use (or an explicit URL override), a voice channel you're
   streaming in, and who to notify.
2. Ball Boy posts the announcement to the configured `streams` channel (or the
   current channel), then acknowledges you ephemerally.

## What each participant sees

- **The streamer** either does nothing (presence auto-detect), clicks one button
  (Go Live), or runs one command with options (`/stream`) — all three post the
  same kind of public announcement.
- **The opponent** is pinged by name in the announcement (when there is one), so
  they know a stream is starting.
- **The audience** (the configured stream role, or `@everyone` if that's what's
  set) is notified in the `streams` channel per the announcement's ping settings.

## Troubleshooting

- **Presence auto-detect never fires.** Two independent things have to both be
  true: Ball Boy needs the Presence privileged intent actually enabled (a Discord
  Developer Portal setting, not a Ball Boy command), and your stream title or
  category has to match what `/admin stream` has configured — check
  `/admin stream` with no options to see the current keywords/category.
- **The Go Live button doesn't post a stream URL.** It uses whatever's saved on
  your profile (Twitch/YouTube/custom link, set via the claim Activity's
  account-linking step). If nothing's saved, the announcement still posts — just
  without a URL — and the ephemeral acknowledgment hints at setting your links in
  the claim/connect Activity.
- **The Go Live button is rejected.** Two guards: it only works on a game that
  hasn't been completed yet, and only the two teams' actual owners in that game
  can click it — anyone else (including a commissioner who doesn't own either
  team) gets an ephemeral denial.
- **`/stream` posts without the URL you expected.** Resolution order is: an
  explicit `url` option always wins; otherwise `profile` picks a single saved
  link (Twitch, YouTube, or Custom); if `profile` is omitted, all your saved
  links are used.

Related: {{< relref "/docs/commands/stream" >}} `/stream`,
{{< relref "/docs/commands/admin" >}} `/admin stream`, `/admin channels`
(`streams`), `/admin roles` (`stream`); concept
{{< relref "/docs/concepts/team-ownership" >}} for the owner-gate context behind
the Go Live button.
