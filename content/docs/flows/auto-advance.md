---
title: "Season advance & auto-advance"
summary: "How weekly advance works, including the @everyone confirm flow and import gates."
weight: 40
---
<!-- Grounding: CLAUDE.md (Message-triggered auto-advance — all slices complete;
     "/season advance" slash command uses the same handoff path; Slice 2 —
     Import gates; S4 — @everyone suppression); spec 20-season-phase-calendar.md;
     src/discord/handler.rs. -->

Advancing a season to the next week or phase can be run directly with a slash
command, or triggered conversationally by pinging the league in Discord once
everyone's ready. Both paths run the exact same advance logic underneath.

## Prerequisites

- A commissioner (or, for the direct command, anyone with the Commissioner gate)
  to actually confirm an advance.
- For the ping-triggered path: a configured trigger — see
  {{< relref "/docs/commands/admin" >}} `/admin auto_advance`, which sets the
  required role/`@everyone`, the trigger channel, an optional cooldown, and where
  the confirm/progress messages post.
- For manual-mode seasons, understand the phase calendar and its import gates —
  see {{< relref "/docs/concepts/seasons-and-phases" >}}.

## Step by step

1. **Someone pings the league in the trigger channel.** A matching ping is either
   `@everyone` or the league's configured announce/required role. A ping alone
   isn't enough — the message also needs advance-intent wording (things like
   "advance," "next week," or "week" plus a completion word like "done"/"ready").
   A ping without that wording — an unrelated `@everyone` announcement, for
   example — is silently ignored. Bots and webhooks (including Ball Boy's own
   weekly announcement) never trigger this.
2. **Ball Boy checks who sent it.** Only the bot owner, a server admin, or the
   league's commissioner can trigger the confirm prompt this way — a regular team
   owner pinging the channel does not trigger anything, even with the right
   wording.
3. **A public confirm thread opens off the trigger message**, with Advance and
   Cancel buttons. If Discord won't let Ball Boy create a thread there for some
   reason, it falls back to posting the confirm prompt directly in the channel
   instead.
4. **A confirmer clicks Advance.** The buttons retire immediately (so a second
   click can't start a second advance), Ball Boy posts a progress message, and the
   actual advance runs in the background.
5. **Alternatively, skip the ping entirely and run
   {{< relref "/docs/commands/season" >}} `/season advance` directly.** It uses
   the identical advance logic and immediate-ack handoff — it just skips the
   ping-and-confirm step.
6. **The advance completes, or is blocked.** A successful advance posts a green
   "Season Advance Complete" summary (previous phase, new phase, game threads
   provisioned) and archives+locks the confirm thread. A manual-mode season
   whose next phase needs games that haven't been imported yet instead gets a red
   "Import Required" message with a Retry button — the thread stays open so you
   can import the schedule and retry without starting over. See
   {{< relref "/docs/concepts/seasons-and-phases" >}} for exactly which
   transitions are gated.
7. **A completed manual season rolls straight into next year.** Advancing past
   the terminal offseason phase (or advancing an already-completed manual season)
   both finishes the old season and creates the new one in a single step, posting
   a "Season Complete — New Season Started" summary instead of the normal
   complete message.

## What each participant sees

- **The person who pings the channel** doesn't need any special permission to
  send the ping itself — the authorization check happens before the confirm
  prompt is posted, so an unauthorized ping simply produces no visible response
  at all.
- **The confirming commissioner (or admin/bot owner)** sees the public confirm
  thread with League/Requested-by/Source/Cooldown details and the Advance/Cancel
  buttons, then the progress and completion messages as they post.
- **Everyone else in the server** sees the public thread and its outcome, since
  it's not ephemeral — that's intentional, so the whole league can see an advance
  in progress.

## Troubleshooting

- **Nothing happens after pinging `@everyone` with clear advance intent.** Check,
  in order: is auto-advance actually enabled for the league
  (`/admin auto_advance`), is this the configured trigger channel, does the ping
  match the configured role (or is it a genuine `@everyone`), and is the sender
  the bot owner, a server admin, or the commissioner. A cooldown between
  triggers may also be in effect.
- **The advance is "blocked" rather than "import required."** These are two
  different states: import-required means the next phase specifically needs a
  schedule import (the message names what to import and the thread stays open
  to retry); a generic block (for example, an unresolvable playoff bracket state)
  reports the same way but has no retry button — resolve the underlying issue
  and re-trigger.
- **Two confirm prompts seem to appear for the same ping.** Ball Boy has a
  built-in guard against this: if a thread already exists for the trigger
  message, the duplicate attempt is silently skipped rather than falling back to
  an in-channel post — you should only ever see one prompt per genuine trigger.
- **The weekly advance announcement doesn't ping `@everyone` even though it used
  to.** When auto-advance is configured and enabled for a league, the weekly
  advance announcement's own ping is suppressed to avoid double-pinging on top of
  the trigger/confirm flow.

Related: {{< relref "/docs/commands/season" >}} `/season advance`,
`/season schedule`, `/season status`; {{< relref "/docs/commands/admin" >}}
`/admin auto_advance`; concept {{< relref "/docs/concepts/seasons-and-phases" >}}.
