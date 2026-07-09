---
title: "Schedule CSV formats"
summary: "The four CSV formats /season schedule auto-detects, their exact column headers, and how skipped rows are reported."
weight: 25
---
<!-- Grounding: CLAUDE.md (Schedule import dispatch); src/data/services.rs
     (detect_schedule_format, import_legacy_flat_schedule,
     import_matrix_schedule, import_conf_champ_schedule,
     import_bowl_cfp_schedule). -->

`/season schedule` imports a season's games from a CSV file. It's **manual-mode
only** — EA-mode leagues get their schedule automatically from the companion
export and can't use this command (see
{{< relref "/docs/concepts/ea-vs-manual" >}}). Ball Boy supports four different CSV
shapes and auto-detects which one you've uploaded from its first line.

## What it is

`/season schedule` reads the uploaded file's first non-empty line (after stripping
a leading UTF-8 byte-order mark, if your spreadsheet app added one) and inspects
its column shape to decide which of four formats you're using: **legacy-flat**,
**matrix**, **conference-championship**, or **bowl/CFP**. You don't choose the
format explicitly — the header shape picks it for you.

## The four formats

### Legacy-flat

No header row — every line is a data row.

```
week_key,home_team_key,away_team_key
```

Three columns per line: the week key exactly as you want it stored (any string of
letters, numbers, underscores, or hyphens — not zero-padded automatically), the
home team's key, and the away team's key. Both team keys must already exist on the
season's roster — this format does a **strict exists-check**: an unresolved team
key fails the whole import rather than being skipped.

```
week_01,texas,oklahoma
week_01,ohio_state,michigan
```

### Matrix

One row per team, one column per week.

```
team,1,2,3,...,16
```

The header's first cell is literally `team`; every remaining header cell must be a
week number (1 through 16). Each data row starts with a team name (resolved
against the season roster by display name/alias, not raw team key) and then one
cell per week: blank means a bye, a plain opponent name means that team is
**home**, and an opponent name prefixed with `@` means that team is **away** (the
opponent is home). Week keys are written zero-padded (`week_01` … `week_16`).
Unresolved team or opponent names are **skipped with a reported reason** rather
than failing the whole import — the summary lists exactly which cells were
skipped and why.

```
team,1,2,3
Texas,@Oklahoma,Baylor,
Oklahoma,Texas,,@Kansas
```

### Conference championship

```
home_team,away_team,conference
```

Exactly three columns, this exact header. Every row — regardless of what's in the
`conference` column, which is read but ignored — is imported into `week_18`. Team
names are resolved against the season roster the same way as the matrix format,
with the same skip-and-report behavior for unresolved names. These games never
count toward conference win/loss records (postseason).

### Bowl / CFP

```
bowl_name,home_team,away_team,bowl_week,cfp_round,home_seed,away_seed
```

Seven columns, this exact header (case-insensitive, but the columns must appear in
this order). `bowl_week` is 1–4, mapping to `week_19` through `week_22`.
`cfp_round` is optional and, if present, must be one of `first_round`,
`quarterfinal`, `semifinal`, or `championship` — anything else fails the import.
`home_seed`/`away_seed` are optional integers 1–12.

A blank (or literal `TBD`) `home_team`/`away_team` cell has two meanings depending
on the row: on a `first_round` row with only one real team, it's a **bye** for a
top-4 seed (no game is created, just a skip note); on a `quarterfinal` row with a
known seed for the blank side, it's recorded as a `tbd_qf_{seed}` **sentinel** —
a placeholder that Ball Boy fills in automatically with the real first-round
winner once that round completes (see
{{< relref "/docs/concepts/seasons-and-phases" >}} for the auto-progressing CFP
bracket). A row where **both** teams are blank/TBD is skipped entirely with a
reported reason.

Each import of this format clears any non-completed game already in weeks 19–22
before writing the new rows — but it **preserves** semifinal and championship
games Ball Boy auto-generated from a completed bracket round, so re-uploading your
first-round/quarterfinal CSV mid-bracket doesn't wipe out games the bot already
built.

```
bowl_name,home_team,away_team,bowl_week,cfp_round,home_seed,away_seed
Rose Bowl,Oregon,Alabama,1,quarterfinal,1,8
Sugar Bowl,,Texas,1,quarterfinal,,5
```

## Skipped rows and re-imports

Every format except legacy-flat reports skipped rows rather than failing the whole
import when it hits an unresolvable name or an ambiguous cell — `/season schedule`
shows the count of games written plus the first several skip reasons, so you can
fix your source data and re-upload. Re-importing is safe: a completed game is
never silently overwritten by a conflicting row from a later upload (Ball Boy
checks for that before writing), so a partial or repeated import doesn't lose
already-recorded results.

## Related commands

- {{< relref "/docs/commands/season" >}} — `/season schedule` (the import command
  itself, using the immediate-ack handoff pattern), `/season status` (shows an
  import-gate hint when the next phase needs a schedule import).
- {{< relref "/docs/concepts/seasons-and-phases" >}} — the phase calendar, import
  gates, and the auto-progressing CFP bracket that fills in `tbd_qf_*` sentinels.
- {{< relref "/docs/concepts/ea-vs-manual" >}} — why this command is manual-mode
  only.
