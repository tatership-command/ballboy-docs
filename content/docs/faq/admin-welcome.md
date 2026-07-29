---
title: "Can Ball Boy automatically welcome new members?"
summary: "Yes — /admin welcome posts a claim how-to when someone joins, gets a role, or gains channel access."
weight: 138
---

Yes. `/admin welcome <league> [options]` configures an automatic welcome
message: a commissioner turns it on and picks a post channel, then any
combination of triggers — a plain server join, being granted a specific role,
or gaining view access to a specific channel. The message covers how to claim
a team and, if you set them, your dynasty's in-game league name and join
password.

You can also post the same "how to claim" message manually at any time with
`/welcome [user]`. See {{< relref "/docs/commands/admin" >}} and
{{< relref "/docs/flows/welcome-flow" >}}.
