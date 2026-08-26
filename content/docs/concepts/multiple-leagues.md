---
title: "Multiple leagues in one server"
summary: "One Discord server can host any number of independent Ball Boy leagues, side by side."
weight: 5
---
<!-- Grounding: verified against production commit 5ed70abd (v1.0.64,
     ballboy-00195-t6j), src/discord/commands.rs (autocomplete_leagues —
     "Non-owners see all active leagues in their guild — no membership
     check. Guild-scoping (list_leagues_from_command) is the only filter for
     non-owners. Handlers gate their own actions; the league picker is not
     sensitive."; list_leagues_from_command has no status filter either) and
     src/discord/role_management.rs (scoped_role_name, guild_is_multi_league
     — team/conference Discord role names get an automatic " [League Name]"
     suffix once a guild hosts 2+ league docs). Also CLAUDE.md (autocomplete
     contract — autocomplete_leagues tiered scope; Bot-owner injection +
     global superuser; /league create game option; /league create slug
     guard; every league-scoped command's "league" option;
     Default-to-current-season; Multi-league role scoping). -->

A Discord server isn't a league in Ball Boy — it's a **container** that can hold
any number of independent leagues. Every league-scoped command takes an explicit
`league` option, so a server with two, three, or more leagues works exactly the
same as one with a single league.

## What it is

A league is created with `/league create <name> <game>`. Nothing about the server
itself limits you to one — running `/league create` again in the same server
creates a second, fully independent league. The two leagues share nothing but the
Discord server they live in.

## Key ideas

- **No "current league" for a channel or server.** Ball Boy never infers which
  league a command is about from where it's run. Every league-scoped command —
  `/season`, `/team`, `/game`, `/admin`, `/waitlist`, `/draft`, and so on — takes an
  explicit `league` option (autocompleted), so you always pick the target
  explicitly.
- **Leagues don't share data.** Each league has its own teams, seasons, rosters,
  schedules, results, channel routing, role routing, and settings (board color,
  board image, auto-advance configuration, welcome configuration, stream
  configuration, launch-card behavior). Configuring one league never touches
  another.
- **Leagues can share channels and roles, or not — your choice.** Because
  channel/role routing is per-league (see {{< relref "/docs/commands/admin" >}}
  `/admin channels` / `/admin roles`), you can point two leagues at the same
  `#announcements` channel if you want a combined feed, or give each its own set
  of channels and roles for a clean separation. Ball Boy doesn't assume either
  way.
- **Seasons nest inside a league, and "active season" is per-league.** Each
  league tracks its own active season independently — `/season create` in one
  league has no effect on another league's active season, even in the same
  server. See {{< relref "/docs/concepts/seasons-and-phases" >}}.
- **Team and conference Discord role names get automatically tagged once a
  server has 2+ leagues.** A single-league server's roles are plain (`Texas`,
  `SEC`). The moment a server has a second league configured, Ball Boy starts
  naming any team/conference role it creates or renames `{Team} [League Name]`
  (for example `Texas [Fall Dynasty]`) so two leagues that both have an "Air
  Force" or an "SEC" never collide on the same role. This means adding a second
  league to a server that already has one **will rename that first league's
  existing roles** the next time they're synced (for example, via
  {{< relref "/docs/commands/admin" >}} `/admin roles_sync_all`, or the moment a
  member claims a team) — don't be surprised to see `[League Name]` appended to
  roles that didn't have it before. If a league later goes back to being the
  only one in the server, its roles are renamed back to plain on the next sync.

## How it behaves

Regular members only ever see leagues from their **own server** in autocomplete —
that's the only filter applied. The league picker itself doesn't check whether you
have Viewer access (or any access) to a given league; it lists every league
configured in the current server, full stop. Access is enforced when you actually
run a command against a specific league, not at autocomplete time — so you may see
a league in the picker that a command then denies you for. The **bot owner is the
one exception on the other axis**: as a global maintenance superuser, the bot
owner's autocomplete shows every league across every server Ball Boy is in, not
just the current one. That's an intentional maintenance affordance, not a scoping
bug — regular commissioners and members never get that cross-server view.

Creating a second (or third, or tenth) league is just another `/league create` —
there's no special "multi-league mode" to turn on, and no migration step. Each new
league starts in manual mode and is connected to EA independently via its own
`/league attach_ea`, if you want that.

## Why you'd do this

- **Different games in one server** — a CFB dynasty and a Madden league for the
  same friend group, run side by side.
- **Multiple dynasties of the same game** — a competitive league and a casual
  league, or separate seasons run by different sub-groups, without the two
  affecting each other's rosters or standings.
- **A content-creator or network hub** — one server hosting several independent
  leagues for different creators or communities, each configured (and channeled)
  on its own terms.

## Related commands

- {{< relref "/docs/commands/league" >}} — `/league create`, `/league list`
  (lists every league configured in the current server), `/league info`.
- {{< relref "/docs/concepts/ea-vs-manual" >}} — mode is set per league, not per
  server.
- {{< relref "/docs/getting-started/first-league" >}} — creating your first
  league and season.
