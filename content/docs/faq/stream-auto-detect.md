---
title: "Does Ball Boy announce automatically when I go live?"
summary: "Yes — on Twitch, on YouTube, or screen-sharing in a Discord voice channel."
weight: 85
---
<!-- Grounding: CLAUDE.md (Twitch EventSub webhook receiver, spec 37 phase 1;
     YouTube stream auto-detection (WebSub), spec 37 phase 2; In-Discord
     voice-channel screen-share auto-detection, phase 3; AND-of-enabled-signals
     stream match model, stream-match-signals slice; v1.0.45/46/48/49
     changelog); src/discord/commands.rs stream_title_matches. -->

It can, in three different ways.

**Twitch and YouTube.** Link that channel to your profile in the Activity's
claim wizard. Ball Boy only announces for a platform you've linked yourself, so
nothing goes out on your behalf without you opting in. A commissioner turns on
detection with `/admin stream` and picks which signals have to match before an
announcement posts — your stream title mentioning the league's name, one of the
two team names playing, the current week, and/or a custom keyword. League name
and team names are on by default. Every signal that's turned on has to match, so
streaming something else, a different league or a different week, never trips a
false alert.

Once it's on, going live during your dynasty week gets you announced in your
game thread automatically within seconds, and in the `streams` channel too if a
commissioner has configured one with `/admin channels`.

**Screen-sharing in Discord.** Start a screen share in a voice channel and Ball
Boy announces that instead, pointing people at the voice channel so they can
just join you. There's no title on a screen share, so no `/admin stream` setup
applies to it — it only needs a `streams` channel.

Ball Boy no longer uses your Discord "Streaming" status for any of this. It used
to; it now uses Twitch's and YouTube's own notifications, which don't depend on
Discord noticing a status change. If you relied on the old behavior, link your
channel to get automatic announcements back.

This is separate from the manual
{{< relref "/docs/faq/stream-notifications" >}} `/stream` command and the 🔴
Go Live button, but all of them post through the same announcement — auto-detect
just means you don't have to run either yourself.
