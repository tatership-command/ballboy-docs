---
title: "How does the season advance from week to week?"
summary: "Run /season advance, or ping the league; /season prepare_week can build next week's threads early."
weight: 110
---
<!-- Grounding: CLAUDE.md (WeekProvisionMode Prepare/Advance — prepare-week
     silent "(Preparation)" announcement; Ready to Advance button on the
     weekly announcement). -->

Either directly with `/season advance`, or conversationally — someone pings the
league with advance-intent wording, and an authorized confirmer (bot owner,
server admin, or commissioner) clicks Advance on the confirm prompt that opens.
Both paths run the exact same advance logic. See
{{< relref "/docs/flows/auto-advance" >}}.

A commissioner can also get a head start with `/season prepare_week`: it builds
next week's game threads and posts the weekly announcement early, but doesn't
actually advance the season. That announcement posts silently (no ping) and is
labeled **(Preparation)** until a commissioner runs `/season advance`, which
replaces it with the real, pinging announcement.

Team owners can click the ✅ **Ready to Advance** button on the weekly
announcement once they're done with their game — it's a signal for the
commissioner, not something that triggers the advance on its own.
