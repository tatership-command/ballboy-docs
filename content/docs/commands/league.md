---
title: "/league — league management"
summary: "Create, connect, inspect, configure, and delete a Ball Boy league."
weight: 10
---

`/league` is a subcommand group (`/league <sub>`). It covers the lifecycle of a
league itself — creating it, connecting it to the EA companion app, inspecting it,
tuning its settings, and deleting it. Every subcommand is `guild_only`; `create` and
`delete` also carry `default_member_permissions = "ADMINISTRATOR"`, so Discord hides
them from non-admin members in the slash-command picker.

## `/league create`

**Syntax:** `/league create <name> <game>`

| Option | Required | Description |
|---|---|---|
| `name` | yes | League display name; the league id/slug is derived from it. |
| `game` | yes | Release game: `cfb`/`madden` or the release-tagged forms `cfb27`/`madden27`. |

**Who can run it:** Server admins (Discord **Administrator**).

**What it does:** Creates a new league in **manual mode**. A symbol-only `name`
(one that normalizes to no usable slug) is rejected, as is a `name` that duplicates
an existing league in the same server.

**Notes:** A league enters **EA (companion) mode** only via `/league attach_ea` (see
below) — there is no `game` value or flag on `create` that puts it in EA mode
directly. See {{< relref "/docs/concepts" >}} for the EA-vs-manual model. Once
created, use {{< relref "/docs/commands/season" >}} `/season create` to add a
season.

## `/league attach_ea`

**Syntax:** `/league attach_ea <league> <platform> <ea_league_id> [ea_league_name] [game]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to connect (autocompleted). |
| `platform` | yes | The EA companion platform. |
| `ea_league_id` | yes | The EA companion league id. |
| `ea_league_name` | no | A friendly label for the EA league. |
| `game` | no | Release game override. |

**Who can run it:** Commissioner.

**What it does:** Connects the league to the EA companion export. This is **the
only way a league enters EA mode** — it writes a GCS tenant marker plus the EA
connection record. Because this does external I/O, the command defers before
replying.

**Notes:** After attaching, EA-mode data (teams, schedules, results) arrives
automatically from the companion export rather than through manual commands like
`/season schedule` or `/season result`. See {{< relref "/docs/concepts" >}} for the
full EA-vs-manual comparison.

## `/league info`

**Syntax:** `/league info <league>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to show (autocompleted). |

**Who can run it:** Viewer.

**What it does:** Shows league details.

## `/league list`

**Syntax:** `/league list`

No options.

**Who can run it:** Any server member.

**What it does:** Replies with an ephemeral list of leagues configured in this
server.

## `/league settings`

**Syntax:** `/league settings <league> [deadlines] [announcement_style] [lurker_role_id]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to update (autocompleted). |
| `deadlines` | no | Deadline configuration. |
| `announcement_style` | no | Announcement style configuration. |
| `lurker_role_id` | no | Lurker (auto-follow) role. |

**Who can run it:** Commissioner.

**What it does:** Updates miscellaneous league settings.

<!-- VERIFY: exact accepted shapes/values for `deadlines` and `announcement_style` were not re-grepped for this page; treat as free-text/config fields until confirmed against `gateway.rs`/`commands.rs`. -->

## `/league delete`

**Syntax:** `/league delete <league>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league to delete (autocompleted). |

**Who can run it:** Server admin.

**What it does:** Shows a danger-confirm button; on confirmation, cascade-deletes
the entire league — every season, team, game, and related record. This is
destructive and cannot be undone.
