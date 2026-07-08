---
title: "The roster board"
summary: "The persistent card-stack roster board — conferences, the waitlist, header image, and board color."
weight: 50
---
<!-- Grounding: CLAUDE.md (Roster board, spec 19, slices 1-4 complete +
     visual-overhaul + multi-embed card stack + letterbox header; /admin
     board_image; /admin board_color); spec 19 (roster board). -->

The roster board is Ball Boy's visual summary of who owns what: one Discord message
built from several embeds stacked together — a header card, one card per conference
with at least one claimed team, and (if anyone's waitlisted) a waitlist card at the
end. Render it on demand with `/teams`, or configure a persistent copy that keeps
itself up to date automatically.

## What it is

Rather than one large embed, the roster board is a "card stack" — multiple embeds
in a single message. This keeps each conference readable on its own and lets the
board grow or shrink with the league without hitting Discord's per-embed size
limits.

## Key ideas

- **It's a card stack, not one big embed.** The header card names the league and
  season and carries the header image; each conference with at least one claimed
  team gets its own embed (title = conference name, a small conference-logo
  thumbnail when a matching logo is resolved, and one row per claimed team); a
  waitlist card lists waitlisted members in order when the waitlist is non-empty.
- **Conferences are grouped and ranked** in a fixed conference order, not
  alphabetically, so the board reads the same every time.
- **Team rows show ownership and in-game identity.** Each claimed team's row names
  the owner (as a mention) and, when the member has linked a game profile
  (Xbox/PSN/Steam/etc.), a second line with that handle — so at a glance you can
  see who to add for the game itself.
- **The header image and embed color are configurable and independent** of each
  other: `/admin board_image` sets an uploaded image or an external URL (falling
  back to the server's icon if neither is set); `/admin board_color` sets the embed
  color used across the board and several other embeds bot-wide.
- **On-demand vs persistent.** `/teams` always renders a fresh copy in the current
  channel. A league can additionally configure a persistent board (via
  `/admin channels roster_board`) that Ball Boy keeps posted and up to date
  automatically, instead of requiring someone to run `/teams` again each time.

## How it behaves

Every ownership change (claim, switch, leave, assign, release) that touches a
league with a persistent board triggers an automatic refresh of that board — so the
persistent board never goes stale after a claim. Team and conference logos come
from Ball Boy's own Discord application emoji, refreshed periodically and on
demand with `/admin reload_emoji`.

## Related commands

- {{< relref "/docs/commands/teams" >}} — `/teams`, the on-demand render.
- {{< relref "/docs/commands/admin" >}} — `/admin board_color`, `/admin
  board_image`, and `/admin channels` (`roster_board`).
- {{< relref "/docs/commands/standings" >}} — a related but distinct read view
  (win/loss standings rather than ownership).
- See {{< relref "/docs/concepts/roles-and-conferences" >}} for how conference
  grouping relates to conference roles.
