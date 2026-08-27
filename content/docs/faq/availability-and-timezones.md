---
title: "How do we find a time to play when we're in different timezones?"
summary: "Post the windows you're free, let Ball Boy find the overlap with your opponent, then propose and confirm a kickoff."
weight: 105
---
<!-- Grounding: .docs/ADR/0025-game-thread-availability-and-user-timezone.md;
     .docs/spec/41-game-availability-and-user-timezone.md (Part A timezone,
     Part B availability); .docs/releases/v1.0.61.md, v1.0.62.md. Verified
     against ballboy-prod @ v1.0.68: src/discord/side_effects.rs button
     labels "Add Availability", "Clear mine", "Confirm", "Decline";
     src/discord/availability.rs format_propose_button_label ("Propose Thu
     8:00 PM") and the "✅ Both free" embed field;
     src/discord/user_timezone.rs TZ_VARIANTS pinned at 597. -->

Every game thread has an **Add Availability** button. Press it and enter the
windows you're free over the next few days — in your own timezone, which
Ball Boy already knows. Your opponent does the same.

Ball Boy then works out where the two of you overlap and keeps a pinned message
in the thread up to date, with a **✅ Both free** section showing the times you
can actually play. Windows you're currently inside still count, so a window that
started an hour ago doesn't vanish from the overlap.

## Proposing and confirming

Each shared window gets a button labelled with the time itself — *Propose Thu
8:00 PM*. Either of you presses one, and the other gets **Confirm** or
**Decline**. On confirm, the game is scheduled — no commissioner in the middle
tagging people to broker it.

**Clear mine** removes just your own windows if your week changes. It doesn't
touch your opponent's.

## Timezones

Your timezone is detected automatically the first time you open the Ball Boy
Activity, so there's usually nothing to set up. It's shown under your team in
every new game thread, so your opponent can see where you are without asking.

To set or correct it, run `/timezone` — it autocompletes over all 597 IANA
zones, so start typing a city or region and pick yours from the list.

Everything Ball Boy displays is rendered with Discord's dynamic timestamps,
which means each person sees every kickoff, deadline, and window in **their own**
local time. Nobody converts anything by hand.

## When you already know the time

Availability is for finding a slot. If you and your opponent have already agreed
on one, skip it and go straight to `/game schedule_time` or the **Schedule Game**
button in the thread.

Related: {{< relref "/docs/faq/schedule-a-game-time" >}},
{{< relref "/docs/commands/game" >}}.
