---
title: "What happens when I roll back a week?"
summary: "It restores the season's position, but deliberately keeps the results you already reported."
weight: 111
---
<!-- Grounding: CLAUDE.md (Rollback reversal contract — ADR 0021 / spec 38,
     Seams A/C/D; CFP bracket-correction warning, W1); .docs/ADR/
     0021-season-rollback-reversal-contract.md; .docs/spec/
     38-season-rollback-reversal.md. -->

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

One caveat worth knowing: CFP bracket rounds don't re-derive. If you fix a First
Round, Quarterfinal, or Semifinal score after Ball Boy already built the next
round from it, that round won't update, even after a rollback and re-advance.
Ball Boy warns you when you roll back out of a CFP bowl week so you know to
check it rather than assuming it sorted itself out.

Related: {{< relref "/docs/commands/season" >}} `/season rollback`,
`/season result`.
