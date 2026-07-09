---
title: "Claiming a team & connecting accounts"
summary: "The end-to-end team-claim flow: /team claim launches the Activity claim wizard, plus /team connect."
weight: 10
---
<!-- Grounding: CLAUDE.md (Activity claim integration — spec 22 Slices 4a + 4b;
     ClaimIntentDoc + launch handoff — spec 22 Slices 5+6; Team-claim
     announcement; Team logos in the claim picker; Commissioner force-assign /
     force-release); spec 22-*; src/web.rs. -->

Claiming a team is the one moment every member has to go through before they can
play. Ball Boy claims entirely through a guided in-Discord Activity — you open it
with `/team claim` (or the app launcher), and the wizard itself handles picking
your league and team, linking accounts, and confirming. This flow covers the
wizard end to end, plus linking your game and stream accounts to a team you
already own.

## Prerequisites

- A league with an active season and teams seeded (see
  {{< relref "/docs/getting-started/first-league" >}}). Manual-mode leagues seed
  all 143 template teams on `/season create`; EA-mode leagues get their teams from
  the companion export instead (see
  {{< relref "/docs/concepts/ea-vs-manual" >}}).
- You need to be a member of the Discord server the league lives in — claiming
  itself is self-service and needs no special role.
- Ball Boy's Discord Activity needs to be enabled for the server for `/team
  claim` to open. If it isn't, ask a commissioner — a slash-command-only claim
  path no longer exists.

## Step by step

1. **Open the claim Activity.** Run {{< relref "/docs/commands/team" >}} `/team
   claim` — it takes no options. This opens Ball Boy's claim Activity right
   inside Discord (you can also reach the same Activity from Discord's app
   launcher). If you already own a team in the season, opening it here starts you
   from the same wizard rather than a separate "connect" view.
2. **Pick your league and team in the wizard.** The Activity's picker only
   offers teams that are actually claimable — already-owned teams and the five
   non-playable FCS placeholder teams never appear.
3. **Link accounts in the Activity.** The wizard walks you through your identity
   source (Xbox, PlayStation, Steam, or a manually-entered EA username) and any
   stream links (Twitch, YouTube, or a custom URL) you want attached to your
   profile, then a review step before you confirm. Xbox, PlayStation, and Steam
   identities are read from **your Discord account's linked connections** (the
   same connections you manage under Discord's own User Settings →
   Connections) via OAuth — Ball Boy never asks for a platform password. If you
   haven't linked one of those platforms to your Discord account, the Activity
   falls back to a manually-entered EA username instead.
4. **Confirm.** The Activity's confirm step is the single underlying claim write
   used by every claim-shaped action in Ball Boy. If you already own the team
   (the common case when you're just here to update accounts), this step updates
   your linked accounts rather than re-claiming. Claiming a new team while
   already owning one releases your prior team back to CPU control as part of
   the same operation (you're never left ownerless mid-claim).
5. **Already claimed, just need to connect accounts?** Run
   {{< relref "/docs/commands/team" >}} `/team connect <league>` instead. It
   requires you already own a team in the season, and launches the same Activity
   pre-filled to the "finish linking" view rather than the new claim picker.

## What each participant sees

- **The claiming member** sees the Activity's picker → review → confirm steps
  (or the finish-linking view, for `/team connect`) open right inside Discord.
- **The commissioner** doesn't need to be involved for a normal self-service claim
  at all. If a member can't run the command themselves, the commissioner can force
  it with {{< relref "/docs/commands/team" >}} `/team assign` — this bypasses the
  self-service claimable-only restriction (while still rejecting the five
  non-playable teams), and uses the same claim-first-then-release ordering as a
  normal switch.
- **Other league members** see a celebratory "Team Claimed!" (or "Team Assigned!")
  embed posted to the league's configured `team_updates` channel, if one is set —
  this is best-effort and silently skipped if the channel isn't configured.

## Troubleshooting

- **`/team claim` doesn't open anything.** The server's Activity launch URL
  isn't configured, so there's currently no way to claim on this server. Ask a
  commissioner to enable Ball Boy's Activity, or to force-assign your team with
  `/team assign` in the meantime.
- **`/team connect` opens the new-claim picker instead of the finish-linking
  view, or falls back gracefully with no pre-fill.** The launch intent behind
  the pre-fill is advisory and expires 15 minutes after it's written. Past that
  window (or if the intent can't be resolved for any other reason), the Activity
  falls back to the normal team picker — this is a graceful degrade, not an
  error, and you can still pick your team manually.
- **`?league=` in the Activity URL returns "You do not have access to that
  league."** This 403 only ever fires when a league is explicitly named in the
  URL and you aren't a member of it. Opening the Activity without an explicit
  `?league=` parameter never 403s — it just falls back to the picker.
- **The Activity says there's no active season.** This is a graceful message, not
  an error — the league exists but hasn't had a season created yet (or its active
  season pointer isn't set). Ask a commissioner to run
  {{< relref "/docs/commands/season" >}} `/season create`.
- **A commissioner tries to force-assign a member who has DMs closed and nothing
  seems to happen.** Any DM-based prompts Ball Boy sends are best-effort — a
  closed-DMs error is swallowed silently rather than surfaced back to the
  commissioner. The assign itself still succeeds regardless.

See {{< relref "/docs/concepts/team-ownership" >}} for the ownership model this
flow is built on.
