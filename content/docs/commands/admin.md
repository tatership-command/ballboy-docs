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
(Discord **Administrator**) gate at runtime. Channel options are native Discord
pickers; role options are free text with autocomplete (see `/admin roles` below).
Most subcommands also expose a `clear` choice enum to unset a previously-configured
field — the clear choice is applied last, so it always wins over any
concurrently-supplied value.

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

**Syntax:** `/admin roles <league> [role fields] [stream_notify] [clear]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `admin` | no | Admin role. |
| `commissioner` | no | Commissioner role. |
| `lurker` | no | Lurker (notify for all games) role. |
| `lurker_uvu` | no | User-games-only notify role — notified only for games where both teams are owned by a member. |
| `announce` | no | Announce-ping role (used instead of `@everyone` for weekly advance pings). |
| `stream` | no | Stream-notify role. |
| `stream_notify` | no | Choice: `everyone` — sets the stream ping to `@everyone` instead of a specific role (wins over a typed `stream` value). |
| `clear` | no | Choice of which field to clear. |

**Who can run it:** Server admin.

**What it does:** Configures the league's role routing.

**Notes:** Each role field is **free text with autocomplete**, not a Discord role
picker. Typing (or picking a suggested) existing role name **adopts** that role
(renaming it to Ball Boy's convention if needed); typing a name that doesn't match
any existing role **creates** a new one; pasting a role ID directly targets that
role by ID, but only if it matches a role that already exists in this server — an
unrecognized ID is rejected with no changes made. If your input would create or
adopt a role, Ball Boy asks you to confirm before making the change. See
{{< relref "/docs/commands/admin" >}} `/admin roles_sync_all` below for bulk
team/conference role provisioning — a separate operation from this command, which
only sets the fixed admin/commissioner/lurker/user-games/announce/stream roles.

## `/admin access`

**Syntax:** `/admin access <user> <role> <action> [league]`

| Option | Required | Description |
|---|---|---|
| `user` | yes | The member to grant/revoke staff access for (user picker). |
| `role` | yes | Which staff tier: `commissioner` or `admin`. |
| `action` | yes | `grant` or `revoke`. |
| `league` | no | The league (autocompleted). Omit if this server only has one league. |

**Who can run it:** Server admin, and additionally gated to Commissioner at the
league level.

**What it does:** Grants or revokes the commissioner/admin access flag that Ball
Boy's Activity (and every other permission check) actually reads. A Discord role
alone isn't enough — someone with only the Discord role but no matching flag on
their member record would pass Discord-side commands but still be treated as a
regular member inside the Activity. `/admin access` writes that flag directly,
then best-effort syncs the matching Discord role (`admin` or `commissioner` from
{{< relref "/docs/commands/admin" >}} `/admin roles`) to match. A revoke whose
Discord role removal fails is reported back to you so you can re-run it — access
isn't fully gone until the role is too, since either one still grants it.

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

**Syntax:** `/admin stream <league> [keywords] [category] [match_team_names] [match_week] [match_league_name]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `keywords` | no | Comma-separated keywords to match in a member's stream title (empty clears). |
| `category` | no | Exact game/category name to match (empty clears). |
| `match_team_names` | no | Boolean — match when the title names one of the two teams in the streamer's current game. Default **on**. |
| `match_week` | no | Boolean — match when the title contains the current week number (e.g. "week 5", "wk 5"). Default **off**. |
| `match_league_name` | no | Boolean — match when the title contains the league's name. Default **on**. |

**Who can run it:** Server admin.

**What it does:** Configures Ball Boy's stream auto-detection matching
criteria — Ball Boy watches for the streamer going live on Twitch or YouTube and
posts a "going live" announcement once every **enabled** signal matches (AND, not
OR), so streaming something else — a different league, a different week — never
trips a false alert. Requires a `streams` channel or a game thread to post the
announcement to; set the streams channel with {{< relref "/docs/commands/admin"
>}} `/admin channels`, not here.

**Notes:** The poise function backing this subcommand is internally named
`admin_stream_detect`, but the **user-facing command name is `/admin stream`**
(`rename = "stream"`). All five signals feed the Twitch EventSub and YouTube
WebSub webhook receivers, which are how detection works; the older
Discord-presence path has been removed, so no privileged gateway intent is
involved. These settings do **not** apply to in-Discord voice screen-share
detection — a screen share has no title to match against, so it only needs a
`streams` channel. Auto-detection is a separate feature from the manual
{{< relref "/docs/commands/stream" >}} `/stream` command and the game-thread Go
Live button.

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

## `/admin role_color`

**Syntax:** `/admin role_color <league> <team> <source> [brighten] [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team whose Discord role color to set (autocompleted). |
| `source` | yes | `primary`, `secondary`, or `clear`. Picks which of the team's stored brand colors to paint its role, or clears a previous override. |
| `brighten` | no | Lighten the color by N percentage points of HSL lightness (0–40) so dark brand colors stay readable on Discord's dark theme. |
| `season` | no | Season (defaults to the current one). |

**Who can run it:** Commissioner.

**What it does:** Sets a team's Discord role color from its stored primary or
secondary brand color, with an optional brighten bump. `clear` removes the
override and reverts the role to the team's default color. The live Discord role
is recolored immediately.

## `/admin notify_mode`

**Syntax:** `/admin notify_mode <league> <mode>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `mode` | yes | `ping` (default) or `thread`. |

**Who can run it:** Server admin.

**What it does:** Chooses how members who opt into game-thread notifications get
notified each week. `ping` posts a quiet role mention alongside the game thread
(no "added to thread" system message); `thread` adds opted-in members to each
game thread as followers. Members opt in with the 🔔 buttons on the weekly
advance announcement.

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
Attach Files, Read Message History, Mention Everyone/All Roles, Pin Messages,
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
