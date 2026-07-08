---
title: "Adding Ball Boy"
summary: "Invite Ball Boy and run the guided setup flow."
weight: 11
---

# Adding Ball Boy

## What Ball Boy is

Ball Boy is a Discord bot for running EA *College Football* and *Madden* dynasty
leagues from inside your Discord server. It manages schedules and game threads,
records results, keeps a live roster board of who owns which team, mirrors
ownership with Discord roles, supports streaming announcements, and can run a
team draft — all through slash commands and a Discord Activity.

## Inviting the bot

A server admin adds Ball Boy to a server using its Discord OAuth invite link.

<!-- TODO(owner): canonical invite URL + required OAuth scopes -->

## The guild-join setup flow

As soon as Ball Boy joins a server, it walks the admin through a short, guided
setup rather than guessing where it's allowed to post:

1. **Prompt.** Ball Boy posts a welcome message with a **"Set up Ball Boy"**
   button, in a channel it can already write to.
2. **Channel picker.** Clicking the button opens an ephemeral (only-you-can-see-it)
   channel picker, listing only the channels Ball Boy can actually post in.
3. **Setup message.** Picking a channel makes Ball Boy post its full setup message
   there, including a permission check of everything it needs.

This flow is **setup-only** — it doesn't change any of your league configuration.
It just gets Ball Boy's setup message and permission check in front of you. You
wire up specific channels (announcements, game threads, roster board, and so on)
afterward with `/admin channels`, covered in the next page.

## Next steps

- {{< relref "/docs/getting-started/permissions-setup" >}} — check and fix Discord
  permissions before you start creating leagues.
- {{< relref "/docs/getting-started/first-league" >}} — create your first league,
  season, and team claim.
