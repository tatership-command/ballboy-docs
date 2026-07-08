---
title: "Roles & conferences"
summary: "How Ball Boy's team, conference, and league roles mirror ownership and how the hierarchy is ordered."
weight: 40
---
<!-- Grounding: CLAUDE.md (Role management, spec 21, all slices complete;
     /admin roles setup — comprehensive read-only preflight); spec
     21-role-management.md. -->

Ball Boy can manage three kinds of Discord role for a league: a **team role** per
claimed team, a **conference role** per conference with at least one claim, and a
small set of fixed **league roles** (admin, commissioner, lurker, announce,
stream). Team and conference roles are created and assigned automatically as
ownership changes; league roles are configured once.

## What it is

Team and conference roles exist to mirror team ownership in Discord — so a claimed
team's owner (and everyone in that conference) can be pinged or grouped by role,
without a commissioner hand-managing role assignments.

## Key ideas

- **Roles track ownership, lazily.** A team role and its conference role are
  created (or adopted, if a same-named role already exists) the first time that
  team is claimed — not up front for the whole league. Claiming, switching, or
  releasing a team grants or removes the relevant role membership as part of that
  same operation.
- **Conference roles use short abbreviations**, not full names — for example "SEC"
  or "B1G" rather than "Southeastern Conference" — so they read well in a member
  list. If Ball Boy adopts a pre-existing role that has the full name, it renames
  it to the abbreviation.
- **Bulk provisioning is a separate operation.** `/admin roles_sync_all`
  re-provisions every owned team's roles at once, removes stale role holders whose
  team ownership has since changed, and reorders the whole managed-role hierarchy —
  useful after a realignment, a bulk import, or just to clean up drift.
- **Ball Boy's own role must sit above every role it manages.** Discord only lets a
  bot assign or reorder roles below its own highest role. If a team or conference
  role Ball Boy manages ends up above Ball Boy's role (for example, after a manual
  server reorg), bulk sync refuses to run rather than silently failing partway
  through.

## How it behaves

`/admin roles_setup` is a safe, read-only permission preflight — it reports every
Discord permission Ball Boy needs (including the role-position requirement above)
with a pass/fail per item and fix hints, and it makes no changes. Run it any time
you're unsure whether Ball Boy is correctly configured, and especially before your
first `/admin roles_sync_all`.

## Related commands

- {{< relref "/docs/commands/admin" >}} — `/admin roles` (the fixed
  admin/commissioner/lurker/announce/stream roles), `/admin roles_sync_all` (bulk
  provisioning), `/admin roles_setup` (the preflight).
- See {{< relref "/docs/concepts/team-ownership" >}} for the ownership changes that
  drive role assignment.
- See {{< relref "/docs/getting-started/permissions-setup" >}} for the initial
  server permission setup.
