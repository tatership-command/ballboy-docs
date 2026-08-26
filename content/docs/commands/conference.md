---
title: "/conference — realignment"
summary: "Move a team into a different conference, one at a time or in bulk."
weight: 130
---

<!-- Grounding: verified against production commit 5ed70abd (v1.0.64,
     ballboy-00195-t6j). `/conference assign`: src/discord/gateway.rs
     (conference_assign, ConferenceChoice) and src/discord/commands.rs
     (conference_assign — league_id is Option<String>, guild-admin +
     Commissioner both gated). `/conference manage`: src/discord/gateway.rs
     (conference_manage — zero-option LaunchActivity, byte-for-byte the
     shape of team_claim) and .docs/spec/42-conference-management-activity.md
     (Approved; bulk grid Activity screen, landed — build_conference_grid_groups
     in src/data/services.rs, routes in src/web.rs) plus
     .docs/spec/30-conference-reassignment.md ("/conference assign (per-team)
     is unaffected throughout" by spec 42). Automatic role reconcile on
     Save: reconcile_conference_roles_for_league in src/discord/handler.rs,
     wired at the apply route in src/web.rs. -->

`/conference` is a subcommand group (`/conference <sub>`) for moving an
already-seeded team into a different one of Ball Boy's canonical conferences —
useful when the underlying game's realignment doesn't match your league, or
changes mid-cycle. FCS is never a valid destination for either subcommand.

## `/conference assign`

**Syntax:** `/conference assign <league> <team> <target_conference> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | no | The league (autocompleted). Omit it if this server only has one league — Ball Boy resolves it automatically and only asks you to specify if the server has zero or more than one. |
| `team` | yes | The team to move (autocompleted). |
| `target_conference` | yes | The conference to move it into: ACC, Big 12, Big Ten, Conference USA, Independent, MAC, Mountain West, Pac-12, SEC, Sun Belt, or The American. FCS is not selectable. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Both a Discord server administrator **and** the league's
Commissioner — the command checks both gates, so a server admin who isn't also
that league's Commissioner is still denied.

**What it does:** Moves one team into the chosen conference. The move updates the
live season right away and is saved as a per-league override, so it survives
future seasons and {{< relref "/docs/commands/admin" >}} `/admin reload_teams`.

**Notes:** This doesn't touch existing Discord roles on its own — run
{{< relref "/docs/commands/admin" >}} `/admin roles_sync_all` afterward to move
the affected owner to their new conference role.

## `/conference manage`

**Syntax:** `/conference manage`

This command takes **no options**. Running it launches the Ball Boy Activity
directly — the same "launch an in-app screen" pattern as
{{< relref "/docs/commands/team" >}} `/team claim`. League selection happens
inside the Activity, not as a slash-command option.

**Who can run it:** Available to anyone who can launch the Activity; the
conference-management screen itself is only shown to Commissioners (gated
server-side when the screen loads, not merely hidden in the UI).

**What it does:** Opens a bulk conference-management screen showing every
conference and every team at once. Tap team chips to select them (selection
can span multiple conferences at the same time), then tap a conference's
"Move here" button to stage those teams into it — the screen shows a live
"Pending changes" list of every staged move before you commit anything.
One **Save** applies every staged move in a single batch. FCS, and any
teams Ball Boy couldn't resolve to one of its 12 conferences, are shown as
source-only groups with no "Move here" button.

**Notes:** Saving a batch through this screen has one behavior `/conference
assign` doesn't: if the league has a real, non-completed active season, Ball
Boy automatically reconciles Discord conference roles for the whole league as
part of the same Save — you do **not** need to run `/admin roles_sync_all`
afterward for moves made here. (`/conference assign`'s per-team move is
unaffected by this and still requires the manual `/admin roles_sync_all`
step described above.) A move made on a completed season is still saved as
the per-league override but is not applied to that season's live team data,
and existing conference win/loss totals for already-played games are never
recomputed — re-import the schedule to re-stamp future games if needed.
