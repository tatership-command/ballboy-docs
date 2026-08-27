---
title: "Does Ball Boy announce automatically when I go live?"
summary: "Yes — on Twitch, on YouTube, or screen-sharing in a Discord voice channel."
weight: 85
---
<!-- Grounding: CLAUDE.md (Twitch EventSub webhook receiver, spec 37 phase 1;
     YouTube stream auto-detection (WebSub), spec 37 phase 2; In-Discord
     voice-channel screen-share auto-detection, phase 3; AND-of-enabled-signals
     stream match model, stream-match-signals slice; v1.0.45/46/48/49
     changelog); src/discord/commands.rs stream_title_matches; verified
     against ballboy-prod @ v1.0.64: src/discord/handler.rs
     resolve_stream_online_context (Twitch/YouTube path) and
     run_voice_stream_pipeline (voice path) both gate on a non-blank
     channel_ids["streams"] BEFORE any eligibility/game lookup — an
     unconfigured streams channel means the whole match returns
     None/continues, so nothing posts anywhere, not even the game thread. -->

It can, in three different ways — but all three need a `streams` channel set
with `/admin channels` first. That channel isn't just a bonus posting
destination; it's the switch that turns auto-detect on at all. With no
`streams` channel configured, Ball Boy doesn't announce anywhere — not even
in your game thread — it just checks and gives up silently. (This
requirement is specific to auto-detect. The manual `/stream` command and the
🔴 Go Live button always post to your game thread regardless.)

**Twitch and YouTube.** Link that channel to your profile in the Activity's
claim wizard. Ball Boy only announces for a platform you've linked yourself, so
nothing goes out on your behalf without you opting in. A commissioner turns on
detection with `/admin stream` and picks which signals have to match before an
announcement posts — your stream title mentioning the league's name, one of the
two team names playing, the current week, and/or a custom keyword. League name
and team names are on by default. Every signal that's turned on has to match, so
streaming something else, a different league or a different week, never trips a
false alert.

Once it's on, going live during your dynasty week gets you announced in both
your game thread and the `streams` channel, automatically, within seconds.

**Screen-sharing in Discord.** Start a screen share in a voice channel and Ball
Boy announces that instead, pointing people at the voice channel so they can
just join you. There's no title on a screen share, so none of `/admin
stream`'s signal matching applies to it — only the `streams` channel
requirement above does.

Ball Boy no longer uses your Discord "Streaming" status for any of this. It used
to; it now uses Twitch's and YouTube's own notifications, which don't depend on
Discord noticing a status change. If you relied on the old behavior, link your
channel to get automatic announcements back.

This is separate from the manual
{{< relref "/docs/faq/stream-notifications" >}} `/stream` command and the 🔴
Go Live button, but all of them post through the same announcement — auto-detect
just means you don't have to run either yourself.
