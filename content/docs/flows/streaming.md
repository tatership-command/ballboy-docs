---
title: "Streaming & Go Live"
summary: "How stream announcements work — Twitch/YouTube auto-detect, screen-share detection, the Go Live button, and /stream."
weight: 50
---
<!-- Grounding: CLAUDE.md (Stream auto-detect (webhook-based; Discord-presence
     detection RETIRED); YouTube stream auto-detection (WebSub); In-Discord
     voice-channel screen-share auto-detection; Go Live click handler;
     "/stream" ad-hoc stream announcement; Unified stream announcement +
     single-link default (ADR 0017); The Go Live button deliberately does NOT
     dedup); src/discord/handler.rs (go_live_guard_game_already_played,
     go_live_guard_non_owner_rejected). -->

Ball Boy has three ways to let your league know you're streaming a game: it can
detect the stream automatically, you can click a Go Live button right in the
game thread, or you can post an announcement manually with `/stream` for a
friendly or unscheduled game.

**Ball Boy no longer uses your Discord "Streaming" status.** Detection used to
read your Discord presence; it now uses Twitch's and YouTube's own notifications
instead, which are more reliable and don't depend on Discord noticing a status
change. If you relied on the old behavior, link your channel in the claim window
(below) to get automatic announcements back.

## The three automatic paths

Automatic detection covers three different situations:

- **Twitch** — you link your Twitch channel, and Twitch tells Ball Boy when you
  go live.
- **YouTube** — the same, for YouTube. Ball Boy confirms the video is actually
  live before announcing, so a scheduled-but-not-started broadcast doesn't fire
  a false alert.
- **In-Discord screen share** — you start a Discord screen share in a voice
  channel, and Ball Boy calls out the voice channel so people can just join you.

## Prerequisites

- **For Twitch/YouTube auto-detect:** link that channel to your profile in the
  claim window (see {{< relref "/docs/flows/claim-and-connect" >}}). Ball Boy
  only announces for a platform you've linked yourself, so nothing is
  broadcast on your behalf without you opting in. A commissioner also needs at
  least one match signal enabled via {{< relref "/docs/commands/admin" >}}
  `/admin stream`, and a `streams` channel configured.
- **For screen-share detection:** a `streams` channel configured. There's no
  title on a screen share, so there's nothing to match against and no
  `/admin stream` setup needed.
- **For the Go Live button:** an unplayed, provisioned game thread, and you need
  to be one of the two teams' owners in that game.
- **For any of them to reach an audience:** a `streams` channel and/or a
  stream-notify role configured via {{< relref "/docs/commands/admin" >}}
  `/admin channels` / `/admin roles`. Without a `streams` channel,
  announcements post in the current channel instead.

## Step by step

**Twitch / YouTube auto-detect:**

1. You link your Twitch and/or YouTube channel once, in the claim window.
2. You start streaming. The platform notifies Ball Boy directly.
3. Ball Boy checks your stream title against every **enabled** match signal in
   `/admin stream` (title keywords, game category, team names, week, league
   name). All enabled signals have to match, so streaming something else never
   trips an announcement.
4. Ball Boy checks whether you own a team with an unplayed game in the season's
   current week.
5. If both hold, the announcement posts automatically. No action needed from
   you.

**In-Discord screen share:**

1. You start a screen share in a voice channel.
2. Ball Boy checks whether you own a team with an unplayed game in the current
   week.
3. If so, it announces and points people at the voice channel you're in, rather
   than at a Twitch or YouTube link.

**The Go Live button:**

1. In an unplayed game thread, either team owner clicks the **🔴 Go Live**
   button.
2. Ball Boy posts the announcement to the thread (and to the `streams` channel,
   if configured), pinging the opponent, and pins it in the thread so nobody has
   to scroll to find it.
3. If you're screen-sharing in a voice channel at the time, the announcement
   calls out that voice channel instead of a saved stream link.
4. You get an ephemeral acknowledgment.

**Manual `/stream`:**

1. Run {{< relref "/docs/commands/stream" >}} `/stream` with any combination of
   an opponent to ping, a free-text matchup note, which saved stream link to use
   (or an explicit URL override), a voice channel you're streaming in, and who
   to notify. The `league` option is optional: if your server has exactly one
   league, Ball Boy picks it for you.
2. Ball Boy posts to the configured `streams` channel (or the current channel).
   If you have an unplayed game this week, it also posts a copy into that game
   thread and pins it there.

## What each participant sees

- **The streamer** either does nothing (auto-detect), clicks one button (Go
  Live), or runs one command with options (`/stream`). All of them post the same
  kind of public announcement.
- **The opponent** is pinged by name in the announcement (when there is one), so
  they know a stream is starting.
- **The audience** (the configured stream role, or `@everyone` if that's what's
  set) is notified in the `streams` channel per the announcement's ping
  settings.

## Troubleshooting

- **Auto-detect never fires.** Work through these in order: your Twitch or
  YouTube channel has to be linked to your profile in the claim window (Ball Boy
  will not announce for a platform you haven't linked); your stream title has to
  satisfy every enabled signal in `/admin stream` (run it with no options to see
  the current configuration); and you have to own a team with an unplayed game
  in the current week. Screen-share detection skips the title check entirely, so
  if Twitch/YouTube isn't working but a voice screen share is, the title is the
  thing to look at.
- **A YouTube stream announced late, or not at all.** Ball Boy confirms a video
  is genuinely live before announcing. A scheduled broadcast usually notifies
  once when you schedule it and again when you actually start, and only the
  second one announces. If you're testing, make sure you've pressed **Go Live**
  in YouTube Studio; an encoder connection on its own leaves the broadcast in
  the "upcoming" state.
- **The Go Live button doesn't post a stream URL.** It uses whatever's saved on
  your profile (Twitch/YouTube/custom link, set via the claim Activity's
  account-linking step). If nothing's saved, the announcement still posts, just
  without a URL, and the ephemeral acknowledgment hints at setting your links in
  the claim/connect Activity. If Ball Boy detected you screen-sharing in a voice
  channel, it deliberately points at the voice channel instead of your saved
  link.
- **The Go Live button is rejected.** Two guards: it only works on a game that
  hasn't been completed yet, and only the two teams' actual owners in that game
  can click it. Anyone else, including a commissioner who doesn't own either
  team, gets an ephemeral denial.
- **I got announced twice.** Auto-detect fires at most once per stream, but the
  **🔴 Go Live** button doesn't suppress itself. That's on purpose: it's the way
  to re-announce if you stop and restart, which auto-detect won't do for you a
  second time. If you don't want the second post, just don't click the button
  after an automatic announcement.
- **`/stream` posted a different link than expected.** You only ever get one
  link, never a list of every account you've connected. Resolution order: an
  explicit `url` option always wins; then an explicit `profile` choice (Twitch,
  YouTube, or Custom); then your saved default, if that platform is actually
  linked; then whichever you have linked, preferring Twitch, then YouTube, then
  a custom link. Picking a voice channel and no `profile` suppresses the link
  entirely, since the voice channel is where people should go.
- **The announcement posted with no group ping.** If no stream-notify role is
  configured, there's nothing for Ball Boy to ping, so it posts anyway and adds
  a note in that channel pointing at `/admin roles`. Your opponent is still
  pinged by name.

Related: {{< relref "/docs/commands/stream" >}} `/stream`,
{{< relref "/docs/commands/admin" >}} `/admin stream`, `/admin channels`
(`streams`), `/admin roles` (`stream`); {{< relref "/docs/flows/claim-and-connect" >}}
for linking your Twitch/YouTube channel; concept
{{< relref "/docs/concepts/team-ownership" >}} for the owner-gate context behind
the Go Live button.
