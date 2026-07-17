---
title: "Your First League"
summary: "Create a league, set your staff and channels, create a season, and claim a team."
weight: 13
---

# Your First League

This page is the full "day one" checklist for a server owner: create the league,
give the right people staff access, route Ball Boy's channels, decide how game
threads should look, then create a season and claim a team.

If you haven't yet, run {{< relref "/docs/commands/admin" >}} `/admin roles_setup`
first — it's a read-only check that confirms Ball Boy has the Discord permissions
it needs. See {{< relref "/docs/getting-started/permissions-setup" >}}.

## 1. Create a league

`/league create <name> <game>` creates a new league. `game` accepts `cfb` or
`madden` (or the release-tagged forms `cfb27` / `madden27`). Ball Boy derives the
league's internal id from `name`; a symbol-only name, or a name that duplicates an
existing league in the same server, is rejected.

## 2. Set your staff — admins & commissioners

Out of the box, only Discord **server administrators** can run Ball Boy's admin
commands. To let other people help run the league, give them a role and tell Ball
Boy which role means what:

- **Commissioners** run day-to-day league operations — advancing the season,
  importing schedules, running the draft, and assigning or releasing teams.
- **Admins** additionally manage the league's Ball Boy configuration (the
  `/admin …` commands themselves).

Point Ball Boy at the Discord roles you use for each:

```text
/admin roles league:<league> commissioner:@Commissioners
/admin roles league:<league> admin:@League Admins
```

Anyone holding the matching Discord role is treated as that staff tier — you don't
have to add people one at a time. If a role doesn't exist yet, you can type a new
name and Ball Boy will offer to create it for you. To grant or revoke staff access
to a **single person** without using a shared role, use `/admin access <user>
<role> <action>`.

Once your team and conference roles start getting created (as members claim teams),
run `/admin roles_sync_all` to provision and order them all at once. See
{{< relref "/docs/concepts/roles-and-conferences" >}} for how Ball Boy's roles
work.

## 3. Route your channels

Ball Boy posts different kinds of message to different channels. Tell it where each
one should go with `/admin channels`:

```text
/admin channels league:<league> announcements:#announcements game_thread:#games roster_board:#roster-board
```

All channel options are independent — set as many or as few as you like, in one
call or across several. The ones most leagues set first:

| Channel | What lands there |
|---|---|
| `announcements` | The weekly advance announcement (matchups, byes, opt-in buttons). |
| `game_thread` | Where per-game threads (or forum posts) are created — see the next section. |
| `roster_board` | The always-up-to-date board of who owns which team. |
| `game_results` | Final scores as games are reported. |
| `team_updates` | "Team claimed!" celebration posts. |
| `streams` | Go-live announcements from `/stream` and the Go Live button. |

See {{< relref "/docs/commands/admin" >}} `/admin channels` for the complete list.

> **Heads up:** Ball Boy needs permission to post in whatever channel you point it
> at. When you set a channel it can't post in, `/admin channels` still saves your
> choice but warns you which permission is missing — grant it in the channel's
> settings (or Server Settings → Integrations → Ball Boy) and you're set. It never
> silently drops a channel.

## 4. Game threads: text channel or forum?

The `game_thread` channel decides how each game shows up. Ball Boy detects the
channel type automatically — you opt in to forum mode simply by pointing
`game_thread` at a forum channel:

- **Text channel** → one **public thread per game**, created off a starter message
  in the channel. Good if you want game chatter to live alongside the rest of your
  server's conversation.
- **Forum channel** → one **forum post per game** instead. Good if you want games
  to be a tidy, browsable gallery on their own, separate from general chat, with
  each matchup as its own post.

Both carry the same starter content and the same game-action buttons; the only
difference is presentation. You can switch later by pointing `game_thread` at a
different channel. See {{< relref "/docs/flows/game-threads-and-results" >}} for the
full game-thread lifecycle, and the {{< relref "/docs/faq" >}} for a quick
text-vs-forum rundown.

## EA vs. manual — which am I?

A newly created league starts in **manual mode**. It only becomes an **EA
(companion) mode** league once you run `/league attach_ea` to connect it to the EA
companion export. A quick way to tell which you are: if you've connected the
companion app, you're EA mode; otherwise, you're manual.

See {{< relref "/docs/concepts" >}} for the full comparison between the two modes.

## 5. Create a season

`/season create <league> <year> [name]` creates a season for the league and sets it
as the league's active season. In **manual mode**, this also seeds all 143 template
teams (138 FBS programs plus 5 generic FCS placeholders) as CPU-owned teams ready
to be claimed. **EA-mode** leagues skip this seeding step — their teams arrive from
the companion export instead. Either way, the new season starts **active**, at
Preseason / Week 0.

Because seeding can take a moment, `/season create` replies immediately with a
short "creating…" acknowledgment, then posts the real result once it finishes.

## 6. Claim a team

`/team claim` takes no options — it opens Ball Boy's **Discord Activity** claim
wizard right inside Discord (you can also reach it from Discord's app launcher).
Pick your league and team, link accounts, and confirm inside the wizard; the
confirm step is the single ownership primitive in Ball Boy, and the same write
every other claim-shaped action funnels through. See {{< relref "/docs/flows" >}}
for the full walkthrough.

## Where to go next

- {{< relref "/docs/commands" >}} — the full command reference.
- {{< relref "/docs/commands/admin" >}} — every `/admin` configuration subcommand.
- {{< relref "/docs/concepts" >}} — how leagues, seasons, ownership, and roles fit
  together.
