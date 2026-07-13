---
title: "FAQ & Troubleshooting"
summary: "Answers to common permission, setup, and troubleshooting questions."
weight: 50
bookCollapseSection: true
---

# FAQ & Troubleshooting

## Getting started

**How do I add Ball Boy to my server?**
Ball Boy isn't publicly listed. You need to join the Ball Boy Discord server
first, get the Server Owner role there, and use the gated invite link shared in
that role's channel. See
{{< relref "/docs/getting-started/adding-ball-boy" >}} for the full flow,
including the guided setup message Ball Boy posts as soon as it joins.

**Can I run more than one league in a server?**
Yes. A Discord server is just a container — it can hold any number of
independent Ball Boy leagues, and every league-scoped command takes an explicit
`league` option so there's never any ambiguity about which one you mean. See
{{< relref "/docs/concepts/multiple-leagues" >}}.

**What's the difference between EA mode and manual mode?**
Manual mode is where you enter schedules and results yourself; EA mode pulls
teams, schedules, and results automatically from the EA companion app once a
commissioner runs `/league attach_ea`. See
{{< relref "/docs/concepts/ea-vs-manual" >}} for the comparison, and
{{< relref "/docs/flows/ea-connect" >}} for the step-by-step connect flow.

**How do I import my schedule?**
`/season schedule` (manual-mode leagues only) uploads a CSV and auto-detects
which of four supported formats you're using from its header shape. See
{{< relref "/docs/concepts/schedule-csv-formats" >}} for the exact column
layouts.

## For members

**How do I claim a team?**
Run `/team claim` — it opens the claim window (Ball Boy's Discord Activity) with
no options to fill in. Pick your team and confirm in the wizard. If every team
is already claimed, ask a commissioner to add you to the waitlist with
`/waitlist add`. See {{< relref "/docs/flows/claim-and-connect" >}} for the full
walkthrough.

**I own a team, but Ball Boy says I don't have access to a command.**
This was a real bug, fixed in v1.0.24: claiming a team didn't used to register
you as a league member on its own, so plain team owners could be denied commands
like `/standings`, `/schedule`, or `/teams`. As of that update, claiming,
switching, or being assigned a team grants you member access automatically (and
it's revoked when you leave or are released from all your teams), and everyone
who already owned a team at the time was backfilled with member access
automatically — no re-claiming needed. See
{{< relref "/docs/concepts/team-ownership" >}}.

**Why did the bot delete the little "used Launch" card after I opened the
Activity?**
That's expected — Ball Boy auto-deletes the Discord-generated "used Launch" card
by default to keep channels focused on the game itself. If you'd rather keep
those cards, a commissioner can run `/admin launch_cards <league> keep`
(`/admin launch_cards <league> suppress` turns auto-delete back on).

**How do I get Ball Boy to ping people when I go live?**
Both `/stream` and the in-thread **🔴 Go Live** button can notify the server when
a stream starts. Pass `notify: Everyone` to ping `@everyone`, or
`notify: Stream role` (or an explicit `role:`) to ping the league's configured
stream-notify role. A commissioner sets that role with `/admin roles` and the
`streams` announcement channel with `/admin channels` — until a stream role is
set, there's nothing for `Stream role` to ping, so the announcement posts without
a group tag. The opponent in a game is always pinged by name regardless. See
{{< relref "/docs/flows/streaming" >}}.

**How do I get notified when it's time to play my games?**
On each weekly advance announcement, click the 🔔 buttons to opt into game
notifications — one for **all games**, one for only **user-vs-user games** (both
teams owned by people). Your commissioner chooses with `/admin notify_mode`
whether opting in sends you a quiet role ping next to each game thread, or adds
you to the thread as a follower.

## For commissioners

**How does the season advance from week to week?**
Either directly with `/season advance`, or conversationally — someone pings the
league with advance-intent wording, and an authorized confirmer (bot owner,
server admin, or commissioner) clicks Advance on the confirm prompt that opens.
Both paths run the exact same advance logic. See
{{< relref "/docs/flows/auto-advance" >}}.

**How do I set up roles, and why can't Ball Boy create team/conference roles?**
Run `/admin roles setup` first — it's a read-only permission check that reports
exactly which Discord permission is missing and how to fix it, including
Ball Boy's own role position (it has to sit above the roles it creates and
manages). Once permissions check out, `/admin roles sync_all` bulk-provisions
and orders every team and conference role for the league. See
{{< relref "/docs/getting-started/permissions-setup" >}} and
{{< relref "/docs/concepts/roles-and-conferences" >}}.

**Should game threads be a text channel or a forum channel?**
Either works — point `/admin channels game_thread` at whichever kind of channel
you prefer. A normal text channel gets one public thread per game; a forum
channel gets one forum post per game instead, with the same starter content and
action buttons. See {{< relref "/docs/flows/game-threads-and-results" >}}.

**How do I decide the draft pick order — can I race for it?**
Yes. When you run `/draft setup`, the panel asks how the pick order is decided:
**manual** (the order you selected the participants) or **🎲 race for order**. If
you pick race, `/draft race` posts a nudge for everyone to open the Ball Boy
Activity, where a commissioner presses **▶ Start Race** to run a live, animated
race — each manager in their own lane with their Discord picture and name.
Nothing is locked until you press **✅ Set Draft Order** (re-roll with **🎲 Race
Again**, or **↻ Rewatch**, as much as you like first); that's the moment the order
saves and the draft board posts. The race gives every manager an equal chance at
any position. See {{< relref "/docs/flows/draft-walkthrough" >}}.

## Troubleshooting

**Why is my command denied?**
See {{< relref "/docs/getting-started/permissions-setup" >}} for how Ball Boy's
access levels (Viewer, Member, Commissioner, server admin) work and how to check
what a specific command requires.

**How do I get Ball Boy working in a new server?**
Start at {{< relref "/docs/getting-started" >}}.

---

More answers get added here as real questions come up in the community — if
something you needed isn't covered yet, ask in the Ball Boy Discord.
