---
title: "Ball Boy"
summary: "Ball Boy is a Discord bot that runs online EA College Football and Madden dynasty/franchise leagues end-to-end — seasons, schedules, game threads, results, standings, rosters, roles, drafts, and streaming — inside your league's own Discord server."
---

# Ball Boy

**Ball Boy runs your online dynasty league from inside Discord.** Seasons,
schedules, game threads, results, standings, rosters, roles, drafts, streaming —
one bot, one server, no spreadsheets.

## What is Ball Boy?

Ball Boy is a Discord bot built for commissioners running online **EA College
Football** and **Madden** dynasty/franchise leagues. It manages a season's entire
lifecycle in Discord: it advances the calendar week to week, creates a thread for
every matchup, records results, keeps live standings and a persistent roster
board, mirrors team ownership with Discord roles, and can run a full snake draft.

Every league runs in one of two modes — see
{{< relref "/docs/concepts/ea-vs-manual" >}} for the details:

- **EA companion mode** — connect a league to the EA companion app
  (`/league attach_ea`) and Ball Boy ingests teams, schedules, and results
  automatically as they're uploaded. No manual data entry.
- **Manual mode** — the commissioner imports the schedule (CSV) and reports
  results, and the league starts pre-seeded with the full ~143-team default College
  Football dataset (138 FBS programs plus 5 FCS placeholders), ready to claim.

## Why commissioners use it

Running a league by hand means the commissioner becomes the league's
infrastructure: manually tracking who's playing whom each week, chasing down
results, updating a standings spreadsheet, spinning up a thread for every
matchup, remembering who owns which team, and keeping members engaged between
game nights. Ball Boy takes that work off your plate:

- **No more manual standings or schedule tracking.** Standings, schedule, and
  the roster board are always live and one command away.
- **No more spinning up threads by hand.** Every game gets its own thread (or
  forum post), automatically, with result-reporting buttons built in.
- **No more chasing ownership by memory.** Team, conference, and league roles
  are created and kept in sync automatically as members claim, switch, or
  release teams.
- **The season keeps moving.** Advance the week with one command — or just ping
  the league in Discord and confirm — instead of manually opening the next
  round of threads yourself.

## What it does

- **Seasons & the phase calendar** — a season moves through a fixed calendar
  from Preseason through the regular season, conference championships, and bowl
  weeks, into the offseason, then rolls straight into next year automatically.
  See {{< relref "/docs/concepts/seasons-and-phases" >}}.
- **Game threads & results** — every matchup gets an auto-created thread with
  buttons to report the result, force a win, or run a fair sim; results update
  standings and post a recap automatically. See
  {{< relref "/docs/commands/game" >}} and {{< relref "/docs/commands/season" >}}.
- **Standings, schedule & scoreboard** — `/standings` and `/schedule` render a
  live, in-Discord view of the season at any point. See
  {{< relref "/docs/commands/standings" >}} and
  {{< relref "/docs/commands/schedule" >}}.
- **The persistent roster board** — a self-updating, per-conference card stack
  showing who owns which team, with team logos and linked game profiles. See
  {{< relref "/docs/concepts/roster-board" >}}.
- **Team claiming** — claim a team with a single slash command or through a
  guided Discord Activity wizard, with a commissioner-managed waitlist for
  when there's more members than open teams. See
  {{< relref "/docs/concepts/team-ownership" >}} and
  {{< relref "/docs/flows/claim-and-connect" >}}.
- **Automatic roles** — team, conference, and league roles (admin,
  commissioner, lurker, announce, stream) are created, colored, and kept in
  sync with ownership — no manual role management. See
  {{< relref "/docs/concepts/roles-and-conferences" >}}.
- **Streaming & Go Live** — announce a stream automatically via Discord
  presence detection, with a one-click Go Live button in the game thread, or
  manually with `/stream`. See {{< relref "/docs/flows/streaming" >}}.
- **New-member welcome** — greet new members automatically with claim
  instructions the moment they join, gain a role, or gain channel access. See
  {{< relref "/docs/flows/welcome-flow" >}}.
- **Draft mode** — run a full snake-style draft with a pick timer, personal
  pick queues, auto-pick, and a live draft board. See
  {{< relref "/docs/commands/draft" >}} and
  {{< relref "/docs/flows/draft-walkthrough" >}}.
- **12-team CFP bracket auto-progression** — import the first round and
  quarterfinals; Ball Boy fills in the semifinals and championship from the
  results automatically. See {{< relref "/docs/concepts/seasons-and-phases" >}}.
- **CSV schedule import** — bring your own regular-season, conference
  championship, or bowl/CFP schedule into a manual-mode league.

## For members

Join your league's Discord server, claim your team with `/team claim` (or the
guided Activity), and you're in. Ball Boy creates a thread for each of your
games, so you report results and go live right there — see
{{< relref "/docs/flows/claim-and-connect" >}} to get started.

## Get started

- {{< relref "/docs/getting-started" >}} — add Ball Boy to your server, check
  permissions, and create your first league and season.
- {{< relref "/docs/commands" >}} — the full command reference.
- {{< relref "/docs/changelog" >}} — release notes for every shipped version.
- **Join the Ball Boy Discord** to get access:
  <https://discord.gg/REVjfCRpw> — see
  {{< relref "/docs/getting-started/adding-ball-boy" >}} for how membership
  turns into an invite for your own server.
