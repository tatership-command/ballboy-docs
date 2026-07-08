---
title: "Adding Ball Boy"
summary: "Join the Ball Boy Discord to get the invite link, then run the guided setup flow."
weight: 11
---

# Adding Ball Boy

## What Ball Boy is

Ball Boy is a Discord bot for running EA *College Football* and *Madden* dynasty
leagues from inside your Discord server. It manages schedules and game threads,
records results, keeps a live roster board of who owns which team, mirrors
ownership with Discord roles, supports streaming announcements, and can run a
team draft — all through slash commands and a Discord Activity.

## Getting the invite link

Ball Boy is **not** publicly listed and has no public self-serve invite link. To
add it to your own server, you first need to be a member of the **Ball Boy
Discord server**:

<https://discord.gg/REVjfCRpw>

Access to Ball Boy requires membership in that server. Once you've joined, obtain
the **Server Owner** role there — the link to add Ball Boy to your own league
server is shared in a channel that's only visible to members with that role. A
commissioner who wants Ball Boy in their server: joins the Ball Boy Discord,
obtains the Server Owner role, and uses the invite link shared in that gated
channel to add the bot.

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
