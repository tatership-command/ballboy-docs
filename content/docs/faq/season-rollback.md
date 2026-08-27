---
title: "What happens when I roll back a week?"
summary: "It restores the season's position, but deliberately keeps the results you already reported."
weight: 111
---
<!-- Grounding: CLAUDE.md (Rollback reversal contract — ADR 0021 / spec 38,
     Seams A/C/D); .docs/ADR/0021-season-rollback-reversal-contract.md;
     .docs/spec/38-season-rollback-reversal.md; src/data/services.rs
     handle_cfp_advancement (verified against ballboy-prod @ v1.0.64: all
     three transitions recompute from current results on every
     /season advance; cfp_downstream_conflict_message refuses when a
     downstream game is already played; unassignable rows are skipped with
     only a server-side tracing::warn!). -->

`/season rollback` moves the season back one week or phase and **restores its
position**. It deletes the game threads and the weekly announcement for the week
you're leaving, then reopens (unarchives and unlocks) the threads for the week
you're returning to.

What it does not do is rewrite the record. Results you already reported, and the
team win-loss records they produced, survive a rollback untouched. That's
deliberate: a rollback is for putting the season back where it was, not for
undoing what happened. To correct a wrong score you don't need to roll back at
all, just re-report it with `/season result`.

Running it takes both server admin and commissioner. A Discord Administrator who
isn't a commissioner is still denied. It's also blocked on a completed season;
from there your only options are advancing (which rolls over into a new season)
or deleting it.

One thing worth knowing: CFP bracket rounds *do* re-derive. On every
`/season advance` that crosses into the next round, Ball Boy rebuilds the
Quarterfinals from First Round results, the Semifinals from Quarterfinal
results, and the Championship from Semifinal results. Catch a wrong score
before you advance past that round and the next advance builds it correctly
on its own. If you've already moved on, roll back to the round in question
and advance again to rebuild what follows it from the corrected score.

The one thing Ball Boy won't do is overwrite a game that's already been
played. There's no command to un-play a game, so if a correction would
change who's playing in an already-completed downstream game, `/season
advance` refuses outright and names the game(s) you need to fix by hand
first. There's also a rarer, silent case: a hand-imported bracket row with a
blank seed cell that Ball Boy can't match to a bracket slot gets skipped
with no message you'll see — it's only logged server-side, so a bracket
round that looks incomplete is worth double-checking your import for.

Related: {{< relref "/docs/commands/season" >}} `/season rollback`,
`/season result`.
