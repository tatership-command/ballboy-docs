---
title: "How do I get Ball Boy to ping people when I go live?"
summary: "Go Live and /stream share one announcement — a single link, pinned, with role/@everyone pings."
weight: 80
---
<!-- Grounding: CLAUDE.md (ADR 0017 unified stream announcement — single link,
     voice-channel detection, pinning in the game thread; /stream defaults +
     missing-role notice; notify role via /admin roles). -->

The 🔴 **Go Live** button in a game thread and the `/stream` command now share
one announcement, so they behave identically. Each posts a single stream link —
your most recently linked account, or your saved default — to the game thread
and, if a commissioner has configured one, the `streams` announcement channel.
The announcement is pinned in the game thread so nobody has to scroll to find it.

To ping people, pass `notify: Everyone` for `@everyone`, or `notify: Stream role`
(or an explicit `role:`) for the league's configured stream-notify role. A
commissioner sets that role with `/admin roles` and the `streams` channel with
`/admin channels`; until a stream role exists there's nothing for `Stream role`
to ping, so the announcement posts without a group tag. Your opponent in a game
is always pinged by name regardless.

If you're screen-sharing inside a Discord voice channel, Go Live detects it and
calls out the voice channel instead of a Twitch/YouTube link. See
{{< relref "/docs/flows/streaming" >}}.
