---
title: "Can I run more than one league in a server?"
summary: "Yes — most commands take a league option; a few auto-resolve it when there's only one."
weight: 20
---

Yes. A Discord server is just a container — it can hold any number of
independent Ball Boy leagues. Most league-scoped commands take a `league`
option so there's no ambiguity about which one you mean. A few commands —
`/stream` and `/admin access` — let you leave `league` out and resolve it
automatically when the server has exactly one league (they ask you to pick one
if there's more than one). `/team claim` and `/conference manage` need no
`league` option at all; both open an Activity where you choose the league
inside it. See
{{< relref "/docs/concepts/multiple-leagues" >}}.
