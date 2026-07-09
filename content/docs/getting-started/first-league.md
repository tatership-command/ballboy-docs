---
title: "Your First League"
summary: "Create a league and season, then claim your first team."
weight: 13
---

# Your First League

## Create a league

`/league create <name> <game>` creates a new league. `game` accepts `cfb` or
`madden` (or the release-tagged forms `cfb27` / `madden27`). Ball Boy derives the
league's internal id from `name`; a symbol-only name, or a name that duplicates an
existing league in the same server, is rejected.

## EA vs. manual — which am I?

A newly created league starts in **manual mode**. It only becomes an **EA
(companion) mode** league once you run `/league attach_ea` to connect it to the EA
companion export. A quick way to tell which you are: if you've connected the
companion app, you're EA mode; otherwise, you're manual.

See {{< relref "/docs/concepts" >}} for the full comparison between the two modes.

## Create a season

`/season create <league> <year> [name]` creates a season for the league and sets it
as the league's active season. In **manual mode**, this also seeds all 143 template
teams (138 FBS programs plus 5 generic FCS placeholders) as CPU-owned teams ready
to be claimed. **EA-mode** leagues skip this seeding step — their teams arrive from
the companion export instead. Either way, the new season starts **active**, at
Preseason / Week 0.

Because seeding can take a moment, `/season create` replies immediately with a
short "creating…" acknowledgment, then posts the real result once it finishes.

## Claim a team

`/team claim` takes no options — it opens Ball Boy's **Discord Activity** claim
wizard right inside Discord (you can also reach it from Discord's app launcher).
Pick your league and team, link accounts, and confirm inside the wizard; the
confirm step is the single ownership primitive in Ball Boy, and the same write
every other claim-shaped action funnels through. See {{< relref "/docs/flows" >}}
for the full walkthrough.

## Where to go next

- {{< relref "/docs/commands" >}} — the full command reference.
- {{< relref "/docs/concepts" >}} — how leagues, seasons, ownership, and roles fit
  together.
