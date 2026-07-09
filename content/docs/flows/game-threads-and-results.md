---
title: "Game threads & results"
summary: "How a game thread is built, what the action buttons do, and what happens when a result is recorded."
weight: 15
---
<!-- Grounding: CLAUDE.md (Game-thread starter message; Game-thread title
     naming; Component translation; Result side-effect sink; Default embed
     color; Delivery-layer embed wrapping; Forum-channel game mode; Go Live
     click handler); src/discord/commands.rs (can_report_result). -->

Every matchup in a manual-mode season (and CPU-vs-CPU postseason games in EA mode)
gets its own Discord thread, with a starter message that shows both teams and a row
of buttons for reporting the result. This is the surface most members interact with
week to week.

## Prerequisites

- A week has to be provisioned — either automatically as the season advances (see
  {{< relref "/docs/flows/auto-advance" >}}) or via
  {{< relref "/docs/commands/season" >}} `/season prepare_week`.
- The channel `/admin channels game_thread` points at determines the thread style:
  a normal text channel gets one **thread per game**; a **forum** channel gets one
  **forum post** per game instead (see Forum-channel mode below).

## The thread itself

**Title.** A freshly created thread is titled `"Week {N}: {Home} vs {Away}"`, or
`"{Bowl Name}: {Home} vs {Away}"` for a bowl/CFP game — always home team first,
always the literal word "vs".

**Starter message.** The starter shows a Home Team field and an Away Team field.
An owned team shows its logo, display name, and record, with the owner mentioned
on its own line; a CPU-controlled team shows `(CPU)` before its record instead of
an owner mention. A bowl game also shows a Bowl Game field, and if a deadline is
set, a Game Deadline field. Team logos render when Ball Boy has a resolvable emoji
for that team.

## The action buttons

Six buttons sit under the starter message, plus a seventh in its own row:

- **✅ Game Played** — opens a modal to enter the final score and settle the
  result normally.
- **🏠 FW Home** / **✈️ FW Away** — force-win the game for the home or away team
  (1–0), for when a game can't be played out but a winner needs to be recorded.
- **🤖 Fair Sim** — settles the game via a simulated result rather than a
  human-reported score.
- **📅 Schedule Game** — opens a modal to set (or update) the game's scheduled
  kickoff time. Same action as {{< relref "/docs/commands/game" >}}
  `/game schedule_time`.
- **🗑️ Delete Thread** — deletes the Discord thread. Commissioner only; this
  removes the thread, not the underlying game record or any result already
  recorded. Same action as `/game delete_thread`.
- **🔴 Go Live** (its own row) — announces that one of the two team owners is
  streaming this game. See {{< relref "/docs/flows/streaming" >}} for the full
  Go Live behavior.

**Who can use which button:** Game Played, both force-win buttons, Fair Sim, and
Schedule Game are all gated the same way — either team's actual owner in that
specific game, or anyone with Commissioner access in the league. A member who
doesn't own either team and isn't a commissioner gets an ephemeral denial. Delete
Thread requires Commissioner. Go Live requires being one of the two team owners
(commissioners who don't own either team can't click it).

## What happens when a result is recorded

Whichever path settles the game — the Game Played modal, a force-win button, Fair
Sim, or the equivalent slash command
({{< relref "/docs/commands/season" >}} `/season result`) — the same things
happen:

1. **Team records update** — wins, losses, and (for conference games) conference
   wins/losses, for both teams.
2. **The thread title gets a completion marker** prefixed to the same
   `{Home} vs {Away}` base, with `🏆` in front of the winner's name: `✅` for a
   normal reported result, `🤖` for Fair Sim, `✅ 🏠` for a home force-win, `✅ ✈️`
   for an away force-win. A tie gets no trophy.
3. **A green result recap posts in the thread** — final score, updated records,
   and a link back to the game thread if it's being cross-posted.
4. **The thread archives and locks.**
5. **A copy posts to the configured results channel**, if
   {{< relref "/docs/commands/admin" >}} `/admin channels game_results` is set.

## Forum-channel mode

If `/admin channels game_thread` is pointed at a **forum channel** instead of a
text channel, each game becomes a forum **post** instead of a thread. The starter
content is plain stacked markdown (no embed — forum previews render the starter
message's text, not an embed) with the same button grid underneath. Lifecycle
(rename on result, archive+lock, re-provision) works the same either way; members
who follow the league's lurker role are added as post followers rather than pinged
inline.

## Related commands

- {{< relref "/docs/commands/game" >}} — `/game schedule_time`, `/game
  delete_thread`, the slash equivalents of two of the buttons.
- {{< relref "/docs/commands/season" >}} — `/season result`, the slash equivalent
  of Game Played/force-win/Fair Sim.
- {{< relref "/docs/concepts/seasons-and-phases" >}} — how weeks get provisioned in
  the first place.
