---
title: "Running a draft"
summary: "A full draft from setup through join, start, the pick clock, queues, autopick, and the board."
weight: 30
---
<!-- Grounding: CLAUDE.md (Draft mode — spec 23 / ADR 0006, all slices 1-7
     complete); spec 23-draft-mode.md. -->

Ball Boy can run a full snake-style team draft in Discord: a commissioner
configures it, members join a pool, and each on-clock participant picks a team in
turn — with a timer, personal queues, auto-pick, and a live board tracking
progress.

## Prerequisites

- A league with an active season and claimable teams — see
  {{< relref "/docs/concepts/team-ownership" >}} for how claiming works, since a
  draft pick *is* a claim under the hood.
- A commissioner to configure and run the draft (`setup`, `start`, `skip`,
  `pause`, `resume`, `end`, `remove`, `replace`).
- Optionally, a channel configured for the persistent draft board and/or draft
  play-by-play — see {{< relref "/docs/commands/admin" >}} `/admin channels`
  (`draft_board`, `draft_updates`).

## Step by step

1. **A commissioner configures the draft.** {{< relref "/docs/commands/draft" >}}
   `/draft setup` opens an ephemeral panel to set the pick timer, what happens on
   timeout (autopick, skip, or pause), the skip destination (back of line, swap
   with next, or removed), the personal-queue size cap, the autopick strategy, and
   **how the pick order is decided** — either **manual** (the order you picked the
   participants in) or **🎲 race for order** (decided by a live race, see step 2b).
   This creates the draft in `pending` status — nothing else can happen until it
   starts.
2. **Members join the pool.** Any server member runs `/draft join` to enter the
   draft order. `/draft leave` removes yourself from the un-picked portion of the
   pool. A commissioner can also `/draft remove` a participant or `/draft replace`
   one participant with another, keeping their slot.

   **2b. (Race-order drafts only) The order is decided by a live race.** If the
   draft was set up with **🎲 race for order**, the pick order isn't set yet.
   `/draft race` posts a nudge telling participants to open the Ball Boy Activity.
   There, a commissioner presses **▶ Start Race** to run an animated race —
   everyone watching sees the same result, each manager in their own lane (with
   their Discord picture and name), and the order fills in live as racers finish.
   Nothing is saved until the commissioner presses **✅ Set Draft Order** (they can
   press **🎲 Race Again** to re-roll, or **↻ Rewatch**, first). Setting the order
   is what saves it and posts the draft board. The race is fair — every manager has
   an equal chance at any position.
3. **The commissioner starts the draft.** `/draft start` transitions it from
   `pending` to `in_progress` and starts the pick clock for the first participant
   in the order.
4. **The on-clock participant picks.** `/draft pick <team>` drafts a team — the
   `team` option only autocompletes undrafted, playable teams. This is the exact
   same claim operation as `/team claim`, so it respects the same non-playable
   guard. A successful pick advances the on-clock pointer to the next participant
   and, in timed drafts, restamps the deadline for their turn.
5. **On timeout, the configured on-timeout behavior kicks in.** If the on-clock
   participant doesn't pick before the deadline: `autopick` drafts for them (see
   the fallback chain below), `skip` moves them per the skip destination without
   recording a pick, or `pause` stops the clock entirely (moving the draft to
   `paused`, resumable with `/draft resume`).
6. **Participants can queue picks ahead of time.** `/draft queue_add <team>` adds
   a team to your own personal queue (subject to the configured size cap),
   `/draft queue_view` shows it, `/draft queue_remove` removes one entry, and
   `/draft queue_clear` empties it. `/draft auto on` turns on auto-pick for
   yourself — when it's your turn, Ball Boy drafts from your queue first (in
   order, skipping anything already drafted), falling back to the configured
   autopick strategy if your queue is empty or exhausted. Turning auto on while
   you're already on the clock drafts for you immediately.
7. **The draft ends.** It completes naturally once every participant has picked,
   or a commissioner can `/draft end` it early.

## What each participant sees

- **The commissioner** configures the draft, manages the pool, and can
  pause/resume/skip/end it at any point. They do **not** get a bypass to pick on
  someone else's behalf — see Troubleshooting.
- **The on-clock participant** sees the pick clock counting down (in timed
  drafts) and can pick, queue ahead, or turn on auto-pick.
- **Waiting participants** can still manage their own queue and auto-pick setting
  at any time, regardless of whose turn it is.
- **Everyone** can check {{< relref "/docs/commands/draft" >}} `/draft board` (or
  the persistent board, if a `draft_board` channel is configured) to see picks
  made so far, who's on the clock with a live countdown, and the remaining order.

## Troubleshooting

- **"It's not your turn" when trying to `/draft pick`.** This is the intended
  gate, not a bug: `/draft pick` can **only** be run by the current on-clock
  participant — there is no commissioner or bot-owner bypass. If a draft is stuck
  because someone can't pick (away, unresponsive), a commissioner should use
  `/draft skip` (moves them per the skip destination) or `/draft end` (ends the
  draft early), not try to pick on their behalf.
  {{< relref "/docs/commands/draft" >}} covers each subcommand's exact gate.
- **A pick timer that should have fired seems to do nothing.** Ball Boy's pick
  clock guards against acting on a stale timer — if the draft's state or deadline
  has already moved on by the time a scheduled timeout fires (for example,
  someone picked in the meantime), that timer silently self-cancels instead of
  double-processing.
- **Autopick picked a team you didn't expect.** The fallback order is: first
  available team in your own queue (skipping anything already drafted), then the
  draft's configured strategy — either a best-by-overall-rating pick among
  available playable teams, or a random pick. Check `/draft queue_view` to see
  what was actually queued.
- **A queue add is rejected.** The draft's configured `queue_size` cap has been
  reached; clear an entry with `/draft queue_remove` or `/draft queue_clear`
  first.

Related: {{< relref "/docs/commands/draft" >}} (all subcommands),
{{< relref "/docs/commands/admin" >}} `/admin channels`
(`draft_board`/`draft_updates`), concept
{{< relref "/docs/concepts/team-ownership" >}}.
