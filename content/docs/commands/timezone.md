---
title: "/timezone — set your time zone"
summary: "Set the time zone Ball Boy uses for you, everywhere. Usually detected automatically."
weight: 75
---
<!-- Grounding: .docs/spec/41-game-availability-and-user-timezone.md (Part A,
     §A6 autocomplete; D8 global-per-user scope). Verified against ballboy-prod
     @ v1.0.68: src/discord/gateway.rs `timezone` (slash_command, NOT
     guild_only, single required `zone` option with autocomplete_timezone);
     src/discord/handler.rs set_user_timezone (writes UserProfileDoc.timezone,
     ephemeral ack / unrecognized-zone message verbatim);
     src/discord/user_timezone.rs TZ_VARIANTS pinned at 597 and
     timezone_label's two output shapes. -->

`/timezone` is a single top-level command — not a subcommand group. It records
which time zone you're in so Ball Boy can show times in your local time and work
out when you and an opponent are both free.

**You usually don't need to run it.** Your zone is detected automatically the
first time you open the Ball Boy Activity. Use this command to set it before
you've ever opened the Activity, or to correct it if you've moved.

## `/timezone`

**Syntax:** `/timezone <zone>`

| Option | Required | Description |
|---|---|---|
| `zone` | yes | Your IANA time zone, e.g. `America/New_York`. Autocompleted over all 597 zones; you can also type a full name directly. |

**Who can run it:** anyone. There is no league, member, or commissioner gate.

**What it does:** Saves the zone to your personal Ball Boy profile and replies
privately with the zone it understood, for example:

> ✅ Time zone set to **New York · EDT (-04:00)**.

Zones without a lettered abbreviation render without one — *Buenos Aires
(-03:00)*, *Kathmandu (+05:45)* — and `UTC` renders as bare **UTC**. The
abbreviation and offset reflect the zone *today*, so a zone that observes
daylight saving displays differently in January than in July. That's expected;
the stored value is the zone itself, not a fixed offset.

If the zone isn't recognized you'll get a private message saying so, and nothing
is saved:

> Unrecognized time zone `EST5EDT_typo`. Pick a suggestion from the list, or
> type a full IANA name like `America/New_York`.

**Scope:** the setting is **global to you**, not per-league and not per-server.
Set it once and it applies in every league and every server you share with
Ball Boy. The command works outside a server for the same reason.

## What your time zone is used for

- **Availability.** The **Add Availability** button parses the windows you type
  in your own zone. Without a stored zone, Ball Boy has nothing to interpret
  them against and the modal won't open — so this is the one place a missing
  zone actively blocks you.
- **Your game threads.** Your zone is shown under your team in every new game
  thread, so an opponent can see where you are without asking.
- **Every displayed time.** Kickoffs, deadlines, and availability windows render
  through Discord's dynamic timestamps, so each person sees them in their *own*
  local time regardless of what you set here.

Related: {{< relref "/docs/faq/availability-and-timezones" >}},
{{< relref "/docs/commands/game" >}} `/game schedule_time`.
