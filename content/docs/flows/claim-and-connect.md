---
title: "Claiming a team & connecting accounts"
summary: "The end-to-end team-claim flow: the slash claim, the Activity claim wizard, and /team connect."
weight: 10
---
<!-- Grounding: CLAUDE.md (Activity claim integration — spec 22 Slices 4a + 4b;
     ClaimIntentDoc + launch handoff — spec 22 Slices 5+6; Team-claim
     announcement; Team logos in the claim picker; Commissioner force-assign /
     force-release); spec 22-*; src/web.rs. -->

Claiming a team is the one moment every member has to go through before they can
play — and Ball Boy gives you two doors into the same underlying claim: a single
slash command, or a guided Activity wizard launched right after it. This flow
covers both, plus linking your game and stream accounts to a team you already own.

## Prerequisites

- A league with an active season and teams seeded (see
  {{< relref "/docs/getting-started/first-league" >}}). Manual-mode leagues seed
  all 143 template teams on `/season create`; EA-mode leagues get their teams from
  the companion export instead (see
  {{< relref "/docs/concepts/ea-vs-manual" >}}).
- You need to be a member of the Discord server the league lives in — claiming
  itself is self-service and needs no special role.
- The Activity steps require Ball Boy's Discord Activity to be enabled for the
  server (`BALLBOY_ACTIVITY_LAUNCH_URL` configured); if it isn't, the launch link
  is silently omitted and the slash-command claim still works on its own.

## Step by step

1. **Claim a team.** Run {{< relref "/docs/commands/team" >}} `/team claim
   <league> <team>`. The `team` option only autocompletes teams that are actually
   claimable — already-owned teams and the five non-playable FCS placeholder teams
   never appear. If you already own a different team in the season, claiming a new
   one releases your prior team back to CPU control as part of the same operation
   (you're never left ownerless mid-claim).
2. **Follow the launch link.** A successful claim's ephemeral confirmation
   includes a link button to open the Claim Activity. Clicking it launches the
   Activity already scoped to your league, season, and the team you just claimed —
   you don't have to re-pick anything.
3. **Finish linking accounts in the Activity.** The Activity walks you through
   your identity source (Xbox, PlayStation, Steam, or a manually-entered EA
   username) and any stream links (Twitch, YouTube, or a custom URL) you want
   attached to your profile, then a review step before you confirm.
4. **Confirm.** The Activity's confirm step writes through the same underlying
   claim used by `/team claim` — it isn't a separate write path. If you already
   own the team (the common case, arriving from the launch link), this step
   updates your linked accounts rather than re-claiming.
5. **Already claimed, just need to connect accounts?** Run
   {{< relref "/docs/commands/team" >}} `/team connect <league>` instead of
   claiming again. It requires you already own a team in the season, and launches
   the same Activity pre-filled to the "finish linking" view rather than the new
   claim picker.

## What each participant sees

- **The claiming member** sees an ephemeral claim confirmation with the launch
  link, then the Activity's picker → review → confirm steps (or the finish-linking
  view, for `/team connect`).
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

- **The Activity link is missing from the claim confirmation.** The server's
  Activity launch URL isn't configured. The slash-command claim itself still
  succeeded; you're just missing the guided account-linking step. Try
  `/team connect` again later once the Activity is enabled, or link accounts
  manually with a commissioner's help.
- **The Activity opens to the team picker instead of your claimed team, or falls
  back gracefully with no pre-fill.** The launch intent behind the pre-fill is
  advisory and expires 15 minutes after it's written. Past that window (or if the
  intent can't be resolved for any other reason), the Activity falls back to the
  normal team picker — this is a graceful degrade, not an error, and you can still
  pick your team manually.
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
