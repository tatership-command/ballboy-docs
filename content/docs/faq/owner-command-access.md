---
title: "I own a team, but Ball Boy says I don't have access to a command."
summary: "Fixed in v1.0.24 — claiming a team now grants league member access automatically."
weight: 60
---

This was a real bug, fixed in v1.0.24: claiming a team didn't used to register
you as a league member on its own, so plain team owners could be denied commands
like `/standings`, `/schedule`, or `/teams`. As of that update, claiming,
switching, or being assigned a team grants you member access automatically (and
it's revoked when you leave or are released from all your teams), and everyone
who already owned a team at the time was backfilled with member access
automatically — no re-claiming needed. See
{{< relref "/docs/concepts/team-ownership" >}}.
