---
title: "The new-member welcome flow"
summary: "How new-member welcome messages are configured, triggered, and what a new member sees."
weight: 20
---
<!-- Grounding: CLAUDE.md (New-member welcome flow — Slices A-C;
     src/discord/welcome_message.rs); src/discord/handler.rs
     (should_welcome, welcome_dedup_insert, WelcomeEventKind). -->

Ball Boy can greet new members automatically — posting a claim-instructions
message the moment someone joins your server, gains a specific role, or gains
visibility into a specific channel. This flow covers configuring it and what a new
member actually sees.

## Prerequisites

- A commissioner or server admin needs to configure the flow first with
  {{< relref "/docs/commands/admin" >}} `/admin welcome` — it does nothing until a
  channel is set and it's enabled. This command is Server admin-gated.
- Ball Boy needs the `GUILD_MEMBERS` privileged gateway intent, which is already
  required for the bot to function and needs no extra toggle for this flow
  specifically.
- A league with an active season (so the welcome message's claim instructions make
  sense) — see {{< relref "/docs/getting-started/first-league" >}}.

## Step by step

1. **A server admin runs `/admin welcome`.** This sets the auto-welcome channel
   (`channel`), turns the flow on (`enabled`), and picks one or more triggers:
   `role` (welcome when a member gains this role), `watch_channel` (welcome when a
   member gains visibility into this channel), and/or `on_join` (welcome on a
   plain server join). It can also carry your in-game league name and password,
   which get shown in the welcome message. Any field can be cleared independently.
2. **A member triggers one of the configured events.** Discord notifies Ball Boy
   when a member joins the server, or when their roles or channel visibility
   change.
3. **Ball Boy checks whether this trigger actually matches.** A plain join only
   welcomes if `on_join` is on; a role-grant or channel-visibility change only
   welcomes if that specific role or channel is the one configured. Bots are
   always skipped.
4. **A per-member, per-server dedup guard fires once.** Ball Boy tracks which
   `(server, member)` pairs it has already welcomed for the life of the running
   process, so re-triggering the same event again (e.g. losing and regaining the
   watched role) doesn't post a duplicate welcome.
5. **The welcome message posts.** Ball Boy pings the new member and posts a public
   embed in the configured channel with condensed claim instructions —
   `/team claim`, which opens Ball Boy's claim Activity — plus your in-game
   league name and password if configured (shown as "none required" if no
   password is set).
6. **The new member claims a team.** They run `/team claim` from the message —
   see {{< relref "/docs/flows/claim-and-connect" >}} for the full claim
   walkthrough.

This flow has a single primary actor configuring it (the admin) and a second actor
receiving it (the new member) — there's no multi-party coordination beyond that.

## Troubleshooting

- **Nothing posts when a member joins.** Check three things in order: is
  `enabled` actually true, is a `channel` actually set, and is `on_join` (or the
  matching role/channel trigger) turned on. `/admin welcome` with no options
  replies with the current configuration so you can check all four at once.
- **A member was welcomed once but not again after a config change.** The dedup
  guard is per-process and doesn't distinguish which trigger fired — once a member
  has been welcomed in this server, they won't be welcomed again until the bot
  process restarts, even if you change the trigger afterward.
- **The role-grant or channel-visibility trigger doesn't fire.** Double check the
  role or channel picker actually matches what changed — a role-grant trigger only
  matches its own specific role, and a channel-visibility trigger only matches
  visibility into its own specific channel, not any role/channel change.
- **You want to re-send welcome instructions on demand instead of waiting for an
  auto-trigger.** Use {{< relref "/docs/commands/welcome" >}} `/welcome [user]` —
  a separate, manually-triggered command that posts the same kind of
  how-to-claim help publicly in the current channel. Note its gate is narrower
  than `/admin welcome`'s: **Server admin or Bot owner only** — there is no
  Commissioner path, even though its own rejection message mentions
  commissioners.

Related: {{< relref "/docs/commands/admin" >}} `/admin welcome`,
{{< relref "/docs/commands/welcome" >}} `/welcome`,
{{< relref "/docs/commands/team" >}} `/team claim`.
