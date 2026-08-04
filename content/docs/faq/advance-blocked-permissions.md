---
title: "Why was my advance blocked with a permissions message?"
summary: "Ball Boy checks it can post before it starts, so a missing permission stops you up front instead of halfway through."
weight: 155
---
<!-- Grounding: CLAUDE.md (Advance/prepare permission preflight — spec 39 A5,
     Seam I: required_channel_permissions, advance_preflight_blocked_message);
     .docs/releases/v1.0.49.md. -->

Before `/season advance` or `/season prepare_week` does anything, Ball Boy checks
that it can actually post in the channels it's about to need: your announcements
channel and your game-thread channel. **If something's missing it stops up
front** and names the exact permission and channel, rather than half-finishing
and leaving you with game threads created but no announcement.

In the announcements channel it needs View Channel, Send Messages, and Embed
Links. For a text game-thread channel, add Create Public Threads and Send
Messages in Threads. For a Forum game-thread channel it needs View Channel,
Create Posts, and Send Messages in Threads.

The check looks at **channel-level** permissions, not just Ball Boy's
server-wide role. That matters, because the usual cause is a channel-specific
override denying something the bot's role otherwise grants.

Fix it under Server Settings, then Integrations, then Ball Boy, or by editing
that channel's permission overwrites, then run the command again. A channel you
haven't configured at all is simply skipped, not treated as an error. For a full
checkup, `/admin roles setup` reports everything that's missing.

Related: {{< relref "/docs/faq/roles-setup" >}},
{{< relref "/docs/commands/season" >}} `/season advance`.
