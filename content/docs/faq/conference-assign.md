---
title: "How do I move a team to a different conference?"
summary: "/conference assign moves one team; /conference manage moves a batch with a paginated picker."
weight: 136
---

Run `/conference assign <league> <team> <target_conference>` — realignment can
happen mid-cycle in the underlying game, so this lets a commissioner move an
already-seeded team into any of Ball Boy's canonical conferences (FCS isn't a
valid target). To move several teams at once, `/conference manage [league]`
opens a paginated picker in Discord: pick a conference to move teams out of,
check the ones you want, choose the destination, and apply.

Either way the move updates the live season right away and is saved so it
survives future seasons and `/admin reload_teams`, but it doesn't touch
existing Discord roles on its own — run `/admin roles_sync_all` afterward to
move the affected owners to their new conference role.
