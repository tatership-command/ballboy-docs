---
title: "How do I set up roles, and why can't Ball Boy create team/conference roles?"
summary: "Run /admin roles_setup to check permissions, then /admin roles_sync_all to provision them."
weight: 120
---
<!-- Grounding: CLAUDE.md (role_management.rs comprehensive preflight incl.
     Pin Messages; /admin roles type-to-create/adopt via classify_role_slot_value). -->

Run `/admin roles_setup` first — it's a read-only permission check that reports
exactly which Discord permission is missing (including **Pin Messages**, which
Discord split out of Manage Messages, so an existing bot role may need it
granted separately) and how to fix it, plus Ball Boy's own role position (it
has to sit above the roles it creates and manages).

Once permissions check out, `/admin roles_sync_all` bulk-provisions and orders
every team and conference role for the league — and you don't have to create
the roles yourself first. On `/admin roles`, typing a role name that doesn't
exist yet creates it (behind a one-click confirm); typing the name of a role
that already exists adopts it instead. See
{{< relref "/docs/getting-started/permissions-setup" >}} and
{{< relref "/docs/concepts/roles-and-conferences" >}}.
