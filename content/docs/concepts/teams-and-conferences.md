---
title: "Teams & conferences"
summary: "The default 143-team dataset, the 12 conferences and their role abbreviations, and the non-playable FCS placeholders."
weight: 35
---
<!-- Grounding: CLAUDE.md (Default FBS team dataset; Non-playable team guard;
     Role management — conf_abbrev_for_role / conference_rank table; Manual-season
     auto-seed); src/data/team_dataset.rs; src/discord/role_management.rs;
     src/discord/roster_board.rs. -->

Every manual-mode season is seeded from the same bundled team dataset: a fixed set
of programs grouped into a fixed set of conferences. This page covers what's in
that dataset and how conferences map to Discord roles and board ordering.

## What it is

The dataset ships with Ball Boy (embedded at build time) and is loaded into
Firestore once, then read from there at runtime. It has **143 teams total: 138
real FBS programs plus 5 generic FCS placeholder teams**, reflecting the 2026
conference realignment. `/season create` seeds all 143 as CPU-owned teams for a
manual-mode season in one step; EA-mode leagues skip this entirely and get their
teams from the companion export instead (see
{{< relref "/docs/concepts/ea-vs-manual" >}}).

## Key ideas

- **12 conferences, each with a short Discord role abbreviation.** Conference roles
  (see {{< relref "/docs/concepts/roles-and-conferences" >}}) use these
  abbreviations rather than full names:

  | Conference key | Full name | Role abbreviation |
  |---|---|---|
  | `acc` | ACC | ACC |
  | `big_ten` | Big Ten | B1G |
  | `big_12` | Big 12 | B12 |
  | `sec` | SEC | SEC |
  | `pac_12` | Pac-12 | PAC |
  | `the_american` | American Athletic Conference | AAC |
  | `conference_usa` | Conference USA | CUSA |
  | `mac` | Mid-American Conference | MAC |
  | `mountain_west` | Mountain West | MWC |
  | `sun_belt` | Sun Belt | SBC |
  | `independent` | Independent | Ind |
  | `fcs` | FCS (generic placeholders) | FCS |

- **Conferences render in a fixed order, not alphabetically** — the roster board
  and standings both group by conference in the order shown above (ACC first,
  FCS last), so the board reads the same every league.
- **Five teams are generic FCS placeholders, not real programs**: `fcs_west`,
  `fcs_east`, `fcs_midwest`, `fcs_northwest`, and `fcs_southeast`. They exist so a
  schedule can include an FCS opponent without needing a full FCS dataset.
- **The FCS placeholders can never be claimed, assigned, or switched to.** They're
  marked non-playable, and every ownership path — self-service claim, switch, and
  a commissioner's force-assign — rejects them before any write happens. See
  {{< relref "/docs/concepts/team-ownership" >}} for the ownership rules this
  guard is part of.
- **Team data drives more than the roster.** Each team's logo, primary color, and
  (for the 138 FBS programs) a launch-ratings overall rating are seeded from the
  same templates. Logos back the roster board and schedule/standings views, colors
  back team role coloring, and the overall rating backs a draft's "best available"
  autopick strategy.

## How it behaves

Seeding is create-absent-only: `/season create` writes all 143 teams once, and a
later `/season sync_teams` can back-fill any that are missing (for example after a
realignment update) without touching teams that are already claimed or already
CPU-owned. An owner-level refresh of the underlying templates themselves (not a
season's teams) is a separate, bot-owner-only maintenance step and doesn't affect
seasons that already exist.

## Related pages

- {{< relref "/docs/concepts/roster-board" >}} — how conference grouping and team
  logos show up on the board.
- {{< relref "/docs/concepts/team-ownership" >}} — the ownership rules, including
  the non-playable guard.
- {{< relref "/docs/concepts/roles-and-conferences" >}} — how conference roles are
  created and ordered in Discord.
- {{< relref "/docs/concepts/ea-vs-manual" >}} — why EA-mode leagues don't use this
  seeding step.
