---
title: "How do I move a team to a different conference?"
summary: "/conference assign moves one team; /conference manage opens an Activity screen for moving a batch at once."
weight: 136
---
<!-- Grounding: .docs/spec/42-conference-management-activity.md,
     .docs/ADR/0026-conference-management-activity.md; verified against
     ballboy-prod @ v1.0.64: src/discord/gateway.rs conference_manage (bare
     LaunchActivity, zero options); src/discord/commands.rs
     apply_conference_to_live_team call site in conference_assign (skips the
     live-season write when the active season is completed, saving only the
     durable override); src/web.rs conference_grid_apply. -->

Run `/conference assign <league> <team> <target_conference>` — realignment can
happen mid-cycle in the underlying game, so this lets a commissioner move an
already-seeded team into any of Ball Boy's canonical conferences (FCS isn't a
valid target).

To move several teams at once, `/conference manage` opens the Activity
instead of a Discord picker — every conference and every team laid out as a
grid. Tap teams to select them (selection can span more than one conference
at a time), tap the destination conference to move everything you've
selected, and hit Save once to apply the whole batch.

Either way the move is saved as a league-level override, so it survives
future seasons and `/admin reload_teams`. Whether it *also* updates the
current season's live team right away depends on that season's state: if
it's still active, yes, immediately; if it's already completed, only the
saved override is written and the live (completed) season is left alone —
the move takes effect starting with the next season you create. Neither
path touches existing Discord roles on its own — run
`/admin roles_sync_all` afterward to move the affected owners to their new
conference role.
