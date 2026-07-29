---
title: "How do I make someone a commissioner or admin?"
summary: "/admin access grants/revokes the Activity-recognized commissioner/admin tier, and syncs the matching Discord role."
weight: 112
---

Run `/admin access <user> <role> <action> [league]` (`role` is `commissioner`
or `admin`; `action` is `grant` or `revoke`; requires a Discord server admin).
This writes the flag Ball Boy's Activity actually checks for access — someone
with only a Discord role but no matching flag on their member record could
pass in Discord commands but still get treated as a regular member inside the
Activity. `/admin access` closes that gap directly, then best-effort syncs the
matching Discord role afterward. A revoke that fails to remove the Discord
role is reported back to you so you can retry — access isn't fully gone until
the role is too, since either one still grants it.

If your server only has one league, you can leave `league` out. See
{{< relref "/docs/getting-started/permissions-setup" >}}.
