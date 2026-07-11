---
title: "/draft — draft mode"
summary: "Run a full team draft: setup, join, queue, start, pick, and board."
weight: 120
---

`/draft` is a subcommand group (`/draft <sub>`) that runs a full draft: configuring
it, building the participant pool, running the on-clock pick timer, personal pick
queues, auto-pick, and a persistent draft board. A pick is Ball Boy's normal
team-claim primitive under the hood — drafting a team **is** claiming it. Unlike
`/team` and `/season`, several `/draft` subcommand names are user-facing as **flat**
names rather than a nested group — `queue_view`, `queue_add`, `queue_remove`,
`queue_clear`, and `board` are top-level `/draft` subcommands, not a nested
`/draft queue` group. Every subcommand's `season` option defaults to the league's
active season unless noted. Every subcommand's permission below was independently
re-grepped against its `commands.rs` handler (not carried from CLAUDE.md prose) —
see the `/draft pick` note for the one case where that check surfaced a correction.

## `/draft setup`

**Syntax:** `/draft setup <league> [season] [skip_destination] [queue_size] [autopick]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |
| `skip_destination` | no | Choice — where a skipped on-clock participant goes: back of line, swap with next, or removed. |
| `queue_size` | no | Choice — personal queue size cap (e.g. 5 or 10). |
| `autopick` | no | Choice — the auto-pick strategy used on timeout or when a participant enables auto (e.g. best-by-rating, random). |

**Who can run it:** Commissioner.

**What it does:** Opens an ephemeral configuration panel — participants, pick
timer, on-timeout behavior, and **how the pick order is decided** — with a Create
Draft button that finalizes the draft in `pending` status. The order-method choice
has two settings:

- **Set order manually** — the pick order is simply the order you selected the
  participants in. The draft board posts right away.
- **🎲 Race for order** — the pick order is decided by a live, animated race you
  run inside the Ball Boy Activity (see `/draft race` below). No board is posted
  until you lock the result in.

## `/draft join`

**Syntax:** `/draft join <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any server member (self-service).

**What it does:** Joins the draft pool.

## `/draft leave`

**Syntax:** `/draft leave <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any server member (self-service).

**What it does:** Leaves the un-picked portion of the draft pool.

## `/draft remove`

**Syntax:** `/draft remove <league> <user> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `user` | yes | The participant to remove (user picker). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Removes a participant from the draft.

## `/draft replace`

**Syntax:** `/draft replace <league> <old_user> <new_user> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `old_user` | yes | The participant to replace (user picker). |
| `new_user` | yes | The replacement (user picker). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Replaces an un-picked participant with someone else, keeping
their slot in the order.

## `/draft start`

**Syntax:** `/draft start <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Transitions the draft from `pending` to `in_progress`, starting
the pick clock.

## `/draft race`

**Syntax:** `/draft race <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Only meaningful for a draft created with the **🎲 Race for
order** method (see `/draft setup`). It posts a public nudge telling participants
to open the Ball Boy Activity to watch the order get decided. It does **not**
compute or save an order itself — the race is run interactively in the Activity.

**How the race works (in the Activity):**

1. Any participant can open the Activity to watch; a **commissioner** presses
   **▶ Start Race** to run the animated race. Everyone watching sees the same
   race — each manager runs in their own lane (shown with their Discord picture
   and name), and the pick order fills in live as each racer crosses the finish
   line.
2. Nothing is saved yet. The commissioner can press **🎲 Race Again** to re-roll
   as many times as they like, or **↻ Rewatch** to replay the current race.
3. When happy, the commissioner presses **✅ Set Draft Order** — *this* is the
   moment the pick order is saved and the draft board is posted. After that, run
   `/draft start` to begin picking.

The race is fair (every manager has an equal shot at any position) and the same
roll always animates identically for everyone.

## `/draft pick`

**Syntax:** `/draft pick <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to draft — autocompletes to **undrafted, playable** teams only. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Only the current on-clock participant — there is **no**
Commissioner or bot-owner bypass. A commissioner who needs to force a stuck draft
forward uses `/draft skip` or `/draft end` instead.

**What it does:** Drafts a team — a pick is the same underlying claim operation as
`/team claim`. Advances the on-clock pointer to the next participant.

## `/draft end`

**Syntax:** `/draft end <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Ends the draft early.

## `/draft pause`

**Syntax:** `/draft pause <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Pauses the pick clock, moving the draft to `paused` status.

## `/draft resume`

**Syntax:** `/draft resume <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Resumes a paused draft, restarting the pick clock.

## `/draft skip`

**Syntax:** `/draft skip <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Commissioner.

**What it does:** Skips the current on-clock participant, per the draft's
configured `skip_destination` (back of line, swap with next, or removed). This does
not record a pick.

## `/draft queue_view`

**Syntax:** `/draft queue_view <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any draft participant.

**What it does:** Shows your personal pick queue.

## `/draft queue_add`

**Syntax:** `/draft queue_add <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to add to your queue (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any draft participant.

**What it does:** Adds a team to your personal pick queue, subject to the draft's
configured `queue_size` cap.

## `/draft queue_remove`

**Syntax:** `/draft queue_remove <league> <team> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `team` | yes | The team to remove — autocompletes to teams **currently in your own queue**. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any draft participant.

**What it does:** Removes a team from your personal pick queue.

## `/draft queue_clear`

**Syntax:** `/draft queue_clear <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any draft participant.

**What it does:** Clears your entire personal pick queue.

## `/draft auto`

**Syntax:** `/draft auto <league> <enabled> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `enabled` | yes | `on` or `off`. |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Any draft participant.

**What it does:** Toggles auto-pick for yourself. When it's your turn and auto-pick
is on, Ball Boy drafts for you automatically — first from your personal queue (in
order, skipping already-drafted teams), then by the draft's configured auto-pick
strategy.

**Notes:** If you enable auto-pick while you're already on the clock, Ball Boy
immediately drafts for you.

## `/draft board`

**Syntax:** `/draft board <league> [season]`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `season` | no | Defaults to the league's active season. |

**Who can run it:** Viewer.

**What it does:** Posts (or refreshes) the persistent draft board — a live view of
picks made, who's on the clock with a countdown, and upcoming order — in the
league's configured draft-board channel.
