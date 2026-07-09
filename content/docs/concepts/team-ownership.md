---
title: "Team ownership"
summary: "How claiming a team works — the single ownership primitive, CPU vs owned teams, and the waitlist."
weight: 30
---
<!-- Grounding: CLAUDE.md (Activity claim integration — claim_team_core is the
     single ownership primitive; Non-playable team guard; Default FBS team
     dataset; Waitlist spec 19 Slice 3; Commissioner force-assign /
     force-release); spec 22-*. -->

Every team in a season is either **CPU-controlled** (unowned, the default when
seeded) or **owned** by a Discord member. Claiming, switching, leaving, connecting,
and a commissioner's force-assign or force-release all funnel through the same
underlying ownership write.

## What it is

Ball Boy has exactly one place that changes who owns a team. Whether you get there
through `/team claim`, `/team switch`, the Discord Activity's claim confirm step,
or a commissioner running `/team assign`, the result is the same single write to
the team's owner.

## Key ideas

- **One ownership primitive.** Every claim-shaped action — self-service claim,
  switch, the Activity wizard, and commissioner assign — routes through the same
  claim logic, so the rules (see below) are consistent no matter which door you
  came in.
- **CPU vs owned.** A season starts with every seeded team CPU-controlled. A member
  claims a CPU team to become its owner; releasing it (`/team leave`, or a
  commissioner's `/team release`) returns it to CPU control.
- **Claim-first ordering.** If you already own a team and claim (or are assigned) a
  new one, the new team is claimed *first* and your prior team(s) are released to
  CPU afterward — never the other way around. A failure partway through this
  sequence never leaves you owning nothing.
- **Five teams are never claimable.** The five generic FCS placeholder teams are
  marked non-playable and are rejected by every ownership path — claim, switch, and
  assign — before any write happens.
- **The waitlist is a separate, ordered queue**, not a claim itself. A commissioner
  adds, removes, or promotes members on it; being on the waitlist doesn't
  automatically grant a team when one opens up.

## How it behaves

Self-service claiming — `/team claim`, which opens Ball Boy's Activity claim
wizard — only offers teams that are actually claimable in its picker; non-playable
and already-owned teams don't appear. A commissioner's `/team assign` and `/team
release` bypass that self-service restriction (while still respecting the
non-playable guard), which is useful for onboarding a member who can't run the
command themselves, or reclaiming an inactive member's team. Releasing an
already-CPU team is a graceful no-op — a commissioner can run `/team release`
without checking state first.

## Related commands

- {{< relref "/docs/commands/team" >}} — claim, switch, leave, connect, assign,
  release.
- {{< relref "/docs/commands/waitlist" >}} — the separate ordered waiting list.
- See {{< relref "/docs/flows" >}} for the Activity claim walkthrough and the
  draft's pick-as-claim behavior.
