---
title: "/admin — league configuration"
summary: "Configure channels, roles, auto-advance, welcome, streaming, board, and templates."
weight: 80
---

`/admin` is a subcommand group (`/admin <sub>`) for server-owner configuration of a
league: channel routing, role routing, auto-advance, stream detection, welcome
messages, roster-board appearance, Activity launch-card behavior, bulk role
provisioning, a permission preflight check, and two bot-owner-only maintenance
commands. The whole group carries `default_member_permissions = "ADMINISTRATOR"`,
so Discord hides it from non-admin members in the slash-command picker; unless
noted otherwise, every subcommand below additionally requires the **Server admin**
(Discord **Administrator**) gate at runtime. Channel and role options are native
Discord pickers. Most subcommands also expose a `clear` choice enum to unset a
previously-configured field — the clear choice is applied last, so it always wins
over any concurrently-supplied picker value.

## `/admin channels`

**Syntax:** `/admin channels <league> [...channel pickers] [clear]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `announcements` | no | Weekly advance/announcement channel. |
| `game_thread` | no | Channel used to create game threads (text or **forum** channel — pointing this at a forum channel opts the league into forum-post game threads). |
| `general` | no | General channel. |
| `game_results` | no | Game-results posting channel. |
| `league_updates` | no | League-updates channel. |
| `team_updates` | no | Team-claim celebration announcements channel. |
| `admin_logs` | no | Admin log channel. |
| `bot_status` | no | Bot-online status announcement channel. |
| `member_updates` | no | Member-update announcement channel. |
| `roster_board` | no | Channel that hosts the persistent roster board. |
| `streams` | no | Stream announcement channel (used by `/stream` and the Go Live button). |
| `draft_board` | no | Channel that hosts the persistent, board-only draft board. |
| `draft_updates` | no | Channel for draft play-by-play announcements (on-clock pings, picks, skips); falls back to `draft_board` when unset. |
| `clear` | no | Choice of which field to clear. |

**Who can run it:** Server admin.

**What it does:** Configures the league's channel routing. All channel fields are
optional and independent — set as many or as few as you like in one call.

## `/admin roles`

**Syntax:** `/admin roles <league> [role pickers] [stream_notify] [clear]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `admin` | no | Admin role. |
| `commissioner` | no | Commissioner role. |
| `lurker` | no | Lurker (auto-follow) role. |
| `announce` | no | Announce-ping role (used instead of `@everyone` for weekly advance pings). |
| `stream` | no | Stream-notify role. |
| `stream_notify` | no | Choice: `everyone` — sets the stream ping to `@everyone` instead of a specific role. |
| `clear` | no | Choice of which field to clear. |

**Who can run it:** Server admin.

**What it does:** Configures the league's role routing.

**Notes:** See {{< relref "/docs/commands/admin" >}} `/admin roles_sync_all` below
for bulk team/conference role provisioning — a separate operation from this
command, which only sets the fixed admin/commissioner/lurker/announce/stream roles.

## `/admin auto_advance`

**Syntax:** `/admin auto_advance <league> [enabled] [cooldown_minutes] [required_role_id] [trigger_channel_id] [messaging_channel_id] [clear]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `enabled` | no | Boolean — turn @everyone-triggered auto-advance on/off. |
| `cooldown_minutes` | no | Minimum minutes between auto-advance triggers. |
| `required_role_id` | no | Role that must be pinged (or the pinger must hold) to trigger advance. |
| `trigger_channel_id` | no | Channel where a matching ping triggers the advance confirmation. |
| `messaging_channel_id` | no | Channel where the advance confirm/progress/complete messages post; falls back to the trigger channel when unset. |
| `clear` | no | Choice of which field to clear. |

**Who can run it:** Server admin.

**What it does:** Configures @everyone- (or announce-role-) triggered auto-advance:
a matching ping in the trigger channel, combined with advance-intent keywords in
the message, opens a public confirm thread with Advance/Cancel buttons. Only the
bot owner, a server admin, or the commissioner can click Advance.

**Notes:** See {{< relref "/docs/commands/season" >}} `/season advance` for the
underlying advance logic this triggers.

## `/admin stream`

**Syntax:** `/admin stream <league> [keywords] [category]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `keywords` | no | Comma-separated keywords to match in a member's stream title. |
| `category` | no | Exact game/category name to match. |

**Who can run it:** Server admin.

**What it does:** Configures automatic stream-presence detection — Ball Boy watches
member Discord presences for a matching stream and posts an announcement.

**Notes:** The poise function backing this subcommand is internally named
`admin_stream_detect`, but the **user-facing command name is `/admin stream`**
(`rename = "stream"`). Requires the Presence privileged Discord gateway intent to
be enabled for the bot. Automatic presence-based detection is a separate feature
from the manual {{< relref "/docs/commands/stream" >}} `/stream` command and the
game-thread Go Live button.

## `/admin welcome`

**Syntax:** `/admin welcome <league> [enabled] [channel] [role] [watch_channel] [on_join] [ingame_name] [ingame_password] [clear]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `enabled` | no | Boolean — turn the welcome flow on/off. |
| `channel` | no | Channel where the auto-welcome message posts. |
| `role` | no | Role that triggers a welcome when granted. |
| `watch_channel` | no | Channel whose visibility grant triggers a welcome. |
| `on_join` | no | Boolean — welcome on plain server join. |
| `ingame_name` | no | In-game league name shown in the welcome message. |
| `ingame_password` | no | In-game league password shown in the welcome message (or "none required" if absent). |
| `clear` | no | Choice of which field to clear. |

**Who can run it:** Server admin.

**What it does:** Configures the new-member welcome flow: when a member joins,
gains the configured role, or gains visibility into the watch channel, Ball Boy
posts a welcome + how-to-claim message in the configured channel.

**Notes:** See {{< relref "/docs/commands/welcome" >}} `/welcome` for the
manually-triggered equivalent message.

## `/admin board_color`

**Syntax:** `/admin board_color <league> [color]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `color` | no | Hex color (`#RRGGBB` or `RRGGBB`). Blank resets to the default. |

**Who can run it:** Server admin.

**What it does:** Sets the roster-board embed color. Also used as the default
color for several other embeds across the bot when no more specific color applies.

## `/admin board_image`

**Syntax:** `/admin board_image <league> [image] [url]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `image` | no | PNG/JPEG attachment, up to 2 MB. |
| `url` | no | An `https://` image URL. |

**Who can run it:** Server admin.

**What it does:** Sets (or clears) the roster-board header image. If both `image`
and `url` are supplied, the uploaded `image` wins. If neither is supplied, the
header image is cleared.

## `/admin launch_cards`

**Syntax:** `/admin launch_cards <league> <mode>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `mode` | yes | Choice: `suppress` (default behavior) or `keep`. |

**Who can run it:** Server admin.

**What it does:** Controls whether Ball Boy deletes the Discord "used Launch" game
invitation card that Discord auto-posts when a member launches the Claim Activity.
`suppress` (the default) deletes it; `keep` leaves it in the channel.

## `/admin roles_sync_all`

**Syntax:** `/admin roles_sync_all <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Server admin and Commissioner.

**What it does:** Bulk-provisions team and conference roles for every owned team,
assigns the correct members, removes stale role holders, and reorders the role
hierarchy so Ball Boy's managed roles sit correctly relative to each other. With up
to ~150 roles to manage, this can take a while — it defers before replying.

**Notes:** Requires Ball Boy's own role to sit above the roles it manages (its
team and conference roles); run `/admin roles_setup` first if you're unsure whether
that's the case.

## `/admin roles_setup`

**Syntax:** `/admin roles_setup`

No options.

**Who can run it:** Server admin (gated at the group level; this subcommand itself
performs no additional access check).

**What it does:** A **read-only** permission preflight: reports ✅/❌ for every
Discord permission Ball Boy needs (View Channel, Send Messages, Embed Links,
Attach Files, Read Message History, Mention Everyone/All Roles, Manage Messages,
Create Public Threads, Send Messages in Threads, Manage Threads, Manage Roles) plus
whether Ball Boy's role sits above its managed roles, with fix hints for anything
missing. It makes **no mutations** — safe to run anytime.

## `/admin reload_emoji`

**Syntax:** `/admin reload_emoji`

No options.

**Who can run it:** **Bot owner only.**

**What it does:** Refreshes the Discord application-emoji cache (team/conference
logos) and re-renders every league's roster board with the refreshed logos.

## `/admin reload_teams`

**Syntax:** `/admin reload_teams`

No options.

**Who can run it:** **Bot owner only.**

**What it does:** Force-refreshes the team and conference template data from the
bot's embedded dataset and busts the in-process template cache, so a code/data
update (for example, a conference realignment) takes effect immediately without a
restart. This does not retroactively update teams already seeded into an existing
season — see {{< relref "/docs/commands/season" >}} `/season sync_teams` for
backfilling an already-created season.
