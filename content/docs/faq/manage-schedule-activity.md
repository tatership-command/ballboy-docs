---
title: "Can I build my schedule without uploading a CSV?"
summary: "Yes — the Manage Schedule tile in the Activity hub builds regular season, conference championships, and bowls/CFP."
weight: 125
---

Yes. Commissioners of a manual-mode league can open Ball Boy's Activity and tap
the **Manage Schedule** tile on the hub screen (only commissioners see it) to
build the schedule interactively instead of formatting a CSV. It has three
modes:

- **Regular Season** — auto-populates a card per owned team so you can pick
  each week's opponent and home/away.
- **Conference Championships** — one title-game row per eligible conference.
- **Bowl Weeks & CFP** — the non-playoff bowl slate plus the 12-team playoff
  bracket, seeded from your First Round pairings. Each bowl you add has its own
  **Bowl Week 1 / Bowl Week 2** picker, so you can split the slate across both
  weeks. Weeks 3 and 4 aren't offered — they belong to the semifinals and the
  championship, which Ball Boy builds for you. Quarterfinal host bowls are
  always Bowl Week 2 and aren't yours to move.

Each mode has its own Apply step that writes straight to the season — no CSV
needed. You can still use `/season schedule` to upload a CSV for a bulk
import; both write to the same schedule, so you can mix and match. Not
available for EA-mode leagues, which get their schedule from the companion
export.
