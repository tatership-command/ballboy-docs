# Ball Boy Docs

User and reference documentation for the [Ball Boy](https://github.com/tatership-command/ballboy)
Discord bot, built with [Hugo](https://gohugo.io/) and the
[Hugo Book](https://github.com/alex-shpak/hugo-book) theme (via Hugo Modules).

Deploys automatically to [docs.ball-boy.app](https://docs.ball-boy.app/) via the
`Deploy docs to GitHub Pages` GitHub Actions workflow on every push to `main`.

## Local development

Requires [Hugo extended](https://gohugo.io/installation/) (>= 0.158) and Go (for
Hugo Modules).

```
hugo mod get -u
hugo server
```

Then open `http://localhost:1313/`.

## Build

```
hugo --gc --minify
```

Output goes to `public/` (git-ignored, build artifact only).
