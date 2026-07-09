---
title: "/team — team ownership"
summary: "Claim, switch, leave, connect, and (for commissioners) assign or release teams."
weight: 30
---

`/team` is a subcommand group (`/team <sub>`). It covers team ownership: claiming a
team, switching or leaving one, connecting linked accounts to a team you already
own, and (for commissioners) force-assigning or force-releasing a team. Every
subcommand defaults its optional `season` option to the league's active season
unless noted otherwise.

## `/team claim`

**Syntax:** `/team claim`

Takes no options — it's a pure Activity launcher, not an inline claim.

**Who can run it:** Any server member.

**What it does:** Opens Ball Boy's claim Activity right inside Discord. The
wizard walks you through picking your league and team, linking your game and
stream accounts, and a review step before you confirm — the confirm step inside
the Activity is where the actual claim write happens (the same single ownership
primitive used by every other claim-shaped action, including `/team switch` and
a commissioner's `/team assign`).

**Notes:** Claiming a new team while already owning one still releases the prior
team(s) back to CPU as part of the same operation (claim-first ordering, so
you're never left ownerless mid-claim) — that logic runs inside the Activity's
confirm step now. The 5 generic FCS placeholder teams are non-playable and never
offered as a choice. See {{< relref "/docs/concepts" >}} for the ownership
model, and {{< relref "/docs/flows" >}} for the Activity claim walkthrough.

## `/team connect`

**Syntax:** `/team connect <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Member.

**What it does:** Launches the Claim Activity to link game and stream accounts for
a team you already own. Requires you to already own a team in the season.

## `/team leave`

**Syntax:** `/team leave <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to leave — autocompletes across the **full roster**. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any server member.

**What it does:** Releases your team back to CPU control.

## `/team switch`

**Syntax:** `/team switch <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The new team to claim (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any server member.

**What it does:** Claims a new team and releases your prior team(s), using the same
claim-first ordering as `/team claim`.

## `/team info`

**Syntax:** `/team info <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to inspect (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Viewer.

**What it does:** Shows an ephemeral summary of the team — its logo (when
resolved) and display name, current owner (a member mention, or "CPU" if
unowned), overall win-loss-tie record, conference record, and its next unplayed
game (week and matchup, or "None" if the schedule has no upcoming game for this
team).

## `/team assign`

**Syntax:** `/team assign <league> <season> <team> <member>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | **yes — required** | Does not default to the active season for this subcommand. |
| `team` | yes | The team to assign (autocompleted). |
| `member` | yes | The Discord member to assign it to (user picker). |

**Who can run it:** Commissioner.

**What it does:** Force-assigns a team to a member, bypassing the normal
self-service claim flow. Non-playable FCS generics are rejected, same as
`/team claim`.

## `/team release`

**Syntax:** `/team release <league> <season> <team>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | **yes — required** | Does not default to the active season for this subcommand. |
| `team` | yes | The team to release (autocompleted). |

**Who can run it:** Commissioner.

**What it does:** Force-releases a team back to CPU control. If the team is
already CPU-controlled, this is a graceful no-op.
