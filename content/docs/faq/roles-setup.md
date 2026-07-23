---
title: "How do I set up roles, and why can't Ball Boy create team/conference roles?"
summary: "Run /admin roles setup to check permissions, then /admin roles sync_all to provision them."
weight: 120
---

Run `/admin roles setup` first — it's a read-only permission check that reports
exactly which Discord permission is missing and how to fix it, including
Ball Boy's own role position (it has to sit above the roles it creates and
manages). Once permissions check out, `/admin roles sync_all` bulk-provisions
and orders every team and conference role for the league. See
{{< relref "/docs/getting-started/permissions-setup" >}} and
{{< relref "/docs/concepts/roles-and-conferences" >}}.
