---
title: "Permissions & Setup"
summary: "Check and fix Ball Boy's Discord permissions before you start."
weight: 12
---

# Permissions & Setup

## Why permissions matter

Ball Boy posts embeds, creates and manages threads, and — for team and conference
role features — creates and orders Discord roles. Each of those needs a specific
Discord permission. If Ball Boy is missing one, the feature that depends on it will
silently fail or come back as a "command denied" error.

## The `/admin roles setup` preflight

Run `/admin roles setup` first, and again any time something isn't working. It is
a **read-only** command that checks every permission Ball Boy actually uses and
reports, for each one:

- a ✅ or ❌ line,
- an impact line explaining what breaks if it's missing, and
- a "how to fix" pointer (Server Settings → Integrations → Ball Boy) when something
  is missing.

Re-run it after changing Ball Boy's role or server permissions to confirm the fix
took.

## The permissions Ball Boy uses

- View Channel
- Send Messages
- Embed Links
- Attach Files
- Read Message History
- Mention Everyone / All Roles
- Manage Messages
- Create Public Threads
- Send Messages in Threads
- Manage Threads
- Manage Roles

Granting the **Administrator** permission satisfies all of these checks at once,
if you'd rather not grant them individually.

## Role position for role management

For team and conference roles (roles that mirror who owns which team), Ball Boy's
own role has to sit **above** the roles it creates and manages — Discord won't let
a bot assign or reorder a role that outranks it.

`/admin roles setup` checks that Ball Boy has a role at all. The deeper check —
that Ball Boy's role sits above every team and conference role it manages — is
enforced when you run `/admin roles sync_all`: if a managed role currently
outranks Ball Boy, sync_all aborts with a clear message telling you to move Ball
Boy's role up, rather than failing partway through.

## "Command denied" troubleshooting

Most Ball Boy commands are gated by an access level: Viewer, Member, Commissioner,
or server (guild) admin — plus a bot-owner superuser used for maintenance. If a
command comes back denied, the caller doesn't have the access level that command
requires. Each command's specific gate is covered on its own reference page in
{{< relref "/docs/commands" >}}.

## Next steps

- {{< relref "/docs/getting-started/first-league" >}} — create your first league,
  season, and team claim.
