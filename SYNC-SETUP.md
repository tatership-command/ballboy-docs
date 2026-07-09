# Release -> docs Auto-PR sync

This repo (`ballboy-docs`) auto-syncs two things whenever the `ballboy` bot
ships a `v*` release: a new **changelog page** and a **command-manifest drift
check**. The sync always opens a pull request for human review — it never
commits to `main` directly.

## End-to-end flow

1. `ballboy` cuts a `v*` tag and deploys to prod (see `ballboy`'s
   `.docs/RELEASING.md`).
2. The `ballboy` deploy workflow sends a `repository_dispatch` to this repo
   (`tatership-command/ballboy-docs`) with `event_type: bot-release` and a
   `client_payload` containing the release version, the base64-encoded
   release-note file, and the base64-encoded command manifest. (The sender
   side lives in the `ballboy` repo and is built/maintained separately from
   this repo.)
3. This repo's `.github/workflows/sync-release.yml` receives the dispatch,
   decodes the payload, writes `content/docs/changelog/{version}.md` via
   `scripts/release_to_changelog.py`, and diffs the incoming manifest against
   `data/command-manifest.txt` via `scripts/check_manifest_drift.py`.
4. It opens a PR (branch `sync/release-{version}`) containing the new
   changelog page, the refreshed `data/command-manifest.txt` baseline, and a
   PR body with the changelog summary plus a drift checklist (or "No command
   drift." when the manifest is unchanged). If the changelog page already
   exists for that version AND there is no manifest drift, it skips opening a
   PR entirely (no-op — nothing new to sync).
5. You review and merge the PR like any other change.
6. Merging to `main` triggers the existing `pages.yml` workflow, which
   rebuilds and redeploys the Hugo site.

## One-time setup required in the `ballboy` repo (owner action)

The sender lives in `ballboy`, not here. It authenticates as a **GitHub App**
rather than a personal access token, so the credential never expires and
never needs annual rotation:

1. Create a GitHub App under the `tatership-command` org (Settings →
   Developer settings → GitHub Apps → New GitHub App). Give it
   **Repository permissions → Contents: Read and write** (the minimum scope
   that allows sending a `repository_dispatch` event to this repo). No other
   permissions are needed.
2. Install the App on the **`ballboy-docs`** repository only.
3. From the App's settings page, copy its **App ID** and generate a
   **private key** (downloads a `.pem` file).
4. In the **`ballboy`** repo's Actions settings, save two secrets:
   - **`DOCS_SYNC_APP_ID`** — the App ID from step 3.
   - **`DOCS_SYNC_APP_PRIVATE_KEY`** — the full contents of the downloaded
     `.pem` private-key file.

The `notify-docs.yml` workflow in `ballboy` mints a short-lived installation
token from these two secrets at runtime (via `actions/create-github-app-token`)
and uses it to send the `repository_dispatch`. Unlike a fine-grained PAT,
**the App's private key does not expire** — there is no annual rotation to
remember. This repo itself needs no read token — `sync-release.yml` uses the
default `GITHUB_TOKEN` to open its PR, since it only ever operates on its own
repo.

Nothing needs to be configured in `ballboy-docs` for the receiver to work —
`sync-release.yml` is self-contained and uses the default `GITHUB_TOKEN`
(`permissions: contents: write, pull-requests: write`, already declared in
the workflow).

## Manual / testing trigger

`sync-release.yml` also accepts `workflow_dispatch` with a `version` input
and an optional `note` textarea (paste a full release-note file — frontmatter
+ body — to test the changelog transform end-to-end). Manual runs do not
exercise the manifest-drift check (there's no manifest input on
`workflow_dispatch`) — use the manual fallback below to test that path.

## Manual fallback (if the automation is broken or you're backfilling)

Run the same two scripts locally and commit by hand:

```sh
cd ballboy-docs
python3 scripts/release_to_changelog.py ../ballboy/.docs/releases/vX.Y.Z.md
python3 scripts/check_manifest_drift.py ../ballboy/tests/fixtures/command-manifest.txt
# review the printed drift report; if there's drift, update the relevant
# content/docs/commands/*.md pages by hand, then:
cp ../ballboy/tests/fixtures/command-manifest.txt data/command-manifest.txt
git add content/docs/changelog data/command-manifest.txt
git commit -m "docs: sync vX.Y.Z release"
```

That's it — same transform, same drift check, just run by hand instead of
via the workflow.

## See also

- `CHANGELOG-SYNC.md` — the exact, deterministic transform spec that
  `scripts/release_to_changelog.py` implements.
