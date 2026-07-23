---
title: "How do I schedule a game time?"
summary: "Use /game schedule_time or the 📅 Schedule button — pick a date, time, and timezone."
weight: 100
---
<!-- Grounding: CLAUDE.md (ADR 0019 timezone-aware schedule-time input + dynamic
     <t:UNIX> display; schedule-time-5 public game-thread announcement; schedule-time
     slice 1 past-time "now"-parsing fix). -->

Use `/game schedule_time` or the 📅 **Schedule** button on a game thread. Either
way you pick a **date** (`YYYY/MM/DD` or `YYYY-MM-DD`), a **time** in 24-hour
`HH:MM`, and your **timezone** from a dropdown — Ball Boy handles the conversion,
so there's no UTC math to do yourself.

The scheduled kickoff then shows in each person's own local timezone
automatically (Discord's dynamic timestamps), and a public note is posted in the
game thread so everyone sees the time — not just whoever scheduled it. You can't
schedule a game in the past. See {{< relref "/docs/commands/game" >}}.
