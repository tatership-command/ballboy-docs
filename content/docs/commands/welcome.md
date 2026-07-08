---
title: "/welcome — how-to-claim help"
summary: "Post claim instructions in the current channel."
weight: 100
---

`/welcome` is a single top-level command — not a subcommand group. It posts a
public how-to-claim-a-team help embed in the current channel, optionally pinging a
specific member.

## `/welcome`

**Syntax:** `/welcome [user]`

| Option | Required | Description |
|---|---|---|
| `user` | no | A member to ping in the welcome message. |

**Who can run it:** Server admin (Discord **Administrator**) or Bot owner —
**there is no Commissioner path**. This command checks the raw Discord
Administrator permission bit and the global bot-owner bypass directly; it does not
go through the league's Commissioner gate the way most `/league`/`/season`/`/team`
subcommands do. A league commissioner who is not also a server admin cannot run
this command, even though the command's own rejection message reads "Only server
admins or commissioners can run `/welcome`" — that wording is inaccurate; the
actual gate is Server admin or Bot owner only.

**What it does:** Posts a how-to-claim help embed publicly in the current channel,
covering both the `/team claim` slash path and the Discord Activity claim path.

**Notes:** This is the manual/on-demand counterpart to Ball Boy's automatic
new-member welcome flow, configured via {{< relref "/docs/commands/admin" >}}
`/admin welcome`, which can post claim guidance automatically when a member joins
or gains a configured role/channel (using its own, slightly different welcome
embed — the two are related but not byte-identical).
