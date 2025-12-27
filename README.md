# practice_codes

This repo contains daily algorithm / Python practice.

## Daily workflow (commit + push)

### 1) Check what changed

```bash
git status
```

### 2) Stage files

Stage everything:

```bash
git add .
```

Or stage specific files/folders:

```bash
git add dicionary/
git add Prefix_sums/
```

### 3) Commit

```bash
git commit -m "Your message here"
```

Examples:

```bash
git commit -m "Add prefix-sum practice"
git commit -m "Update two_sum and max_freq"
```

### 4) Push to GitHub

```bash
git push
```

That’s it. If you’ve already pushed once, `git push` will use the upstream branch automatically.

## One-time setup (only if needed)

### A) Initialize git (if `.git/` doesn’t exist)

```bash
git init
```

### B) Set the remote (connect to your GitHub repo)

This repo should point to:

- `https://github.com/dkouskoulas/practice_codes.git`

Commands:

```bash
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/dkouskoulas/practice_codes.git
```

Verify:

```bash
git remote -v
```

### C) Make sure you’re on `main` and push the first time

```bash
git branch -M main
git push -u origin main
```

## Helpful tips

- Don’t paste lines starting with `#` into your terminal; that’s a comment in many docs, but zsh will try to run it and show `command not found: #`.
- If `git status` says `nothing to commit, working tree clean`, you’re already committed locally. To publish to GitHub, run `git push`.
