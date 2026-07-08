---
title: "/waitlist — the league waitlist"
summary: "Add, remove, promote, and list waitlisted members."
weight: 90
---

`/waitlist` is a subcommand group (`/waitlist <sub>`) for managing the league's
waitlist — an ordered list of members waiting for a team to open up.

## `/waitlist add`

**Syntax:** `/waitlist add <league> <user>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `user` | yes | The member to add (user picker). |

**Who can run it:** Commissioner.

**What it does:** Adds a member to the back of the waitlist.

## `/waitlist remove`

**Syntax:** `/waitlist remove <league> <user>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `user` | yes | The member to remove (user picker). |

**Who can run it:** Commissioner.

**What it does:** Removes a member from the waitlist.

## `/waitlist promote`

**Syntax:** `/waitlist promote <league> <user>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |
| `user` | yes | The member to promote (user picker). |

**Who can run it:** Commissioner.

**What it does:** Moves a member to the front of the waitlist.

## `/waitlist list`

**Syntax:** `/waitlist list <league>`

| Option | Required | Description |
|---|---|---|
| `league` | yes | The league (autocompleted). |

**Who can run it:** Viewer.

**What it does:** Shows the current waitlist order, as an ephemeral reply.
