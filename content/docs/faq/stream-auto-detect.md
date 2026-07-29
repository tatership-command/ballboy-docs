---
title: "Does Ball Boy announce automatically when I go live on Twitch?"
summary: "Yes, once a commissioner turns it on with /admin stream — no button or command needed."
weight: 85
---
<!-- Grounding: CLAUDE.md (Twitch EventSub webhook receiver, spec 37; AND-of-
     enabled-signals stream match model, stream-match-signals slice, v1.0.45/46
     changelog); src/discord/commands.rs stream_title_matches. -->

It can. A commissioner turns on Twitch auto-detection with `/admin stream` and
picks which signals have to match before Ball Boy posts an announcement — your
stream title mentioning the league's name, one of the two team names playing,
the current week, and/or a custom keyword. League name and team names are on
by default. Every signal that's turned on has to match, so streaming something
else — a different league, a different week — never trips a false alert.

Once it's on, going live on Twitch during your dynasty week gets you announced
in your game thread automatically within seconds — using the stream link from
your linked Twitch account (set in the Activity's claim wizard) — and, if a
commissioner has configured one with `/admin channels`, to the `streams`
channel too.

This is separate from the manual
{{< relref "/docs/faq/stream-notifications" >}} `/stream` command and the 🔴
Go Live button, but all three post through the same announcement — auto-detect
just means you don't have to run either yourself.
