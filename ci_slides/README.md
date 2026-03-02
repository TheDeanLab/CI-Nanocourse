# Slidev Setup (CI Nanocourse)

This document explains how the Slidev presentation environment was installed and how to reproduce it cleanly.

## Important: Avoid `sudo` with npm

Do **not** run:

```bash
sudo npm i -g pnpm
```

Using `sudo` here can cause permission mismatches in:

- `~/.npm`
- `/usr/local/lib/node_modules`

Common symptoms:

- `EACCES` permission errors
- broken installs
- `slidev: command not found`
- missing `node_modules`

If this has already happened, fix ownership:

```bash
sudo chown -R $(whoami) ~/.npm
sudo chown -R $(whoami) /usr/local/lib/node_modules
```

## Clean Install Instructions

### 1. Install pnpm (no sudo)

```bash
npm install -g pnpm
```

If this fails due to permissions, run the ownership fix above first.

### 2. Create the Slidev project

From inside the repository:

```bash
pnpm create slidev
```

Choose:

- **Project name:** `ci_slides`
- **Install and start now?:** `yes`
- **Package manager:** `npm` or `pnpm` (be consistent)

This scaffolds:

```text
ci_slides/
  package.json
  slides.md
  ...
```

### 3. If install fails (permission recovery)

If npm errors look like this:

```text
EACCES: permission denied, mkdir ~/.npm/_cacache/...
```

Run:

```bash
sudo chown -R $(whoami) ~/.npm
sudo chown -R $(whoami) /usr/local/lib/node_modules
```

Then reinstall dependencies:

```bash
cd ci_slides
rm -rf node_modules
rm -f package-lock.json pnpm-lock.yaml
pnpm install
```

### 4. Install dependencies

Inside the slides directory:

```bash
cd ci_slides
pnpm install
```

Expected dependencies include:

- `@slidev/cli`
- `@slidev/theme-default`
- `@slidev/theme-seriph`
- `vue`

Peer dependency warnings for `shiki` are usually harmless.

### 5. Start the dev server

```bash
npm run dev
```

Or:

```bash
pnpm dev
```

You should see:

```text
public slide show   > http://localhost:3030/
presenter mode      > http://localhost:3030/presenter/
```

## Project Structure

```text
CI-Nanocourse/
  ci_slides/
    slides.md
    package.json
    node_modules/
```

Slides are edited in:

```text
ci_slides/slides.md
```

## Reproducible Setup for Students (Recommended)

Install Node via `nvm`:

```bash
brew install nvm
nvm install --lts
nvm use --lts
npm install -g pnpm
```

This avoids global permission issues.

## Common Errors and Fixes

### `slidev: command not found`

- **Cause:** `node_modules` missing
- **Fix:** `pnpm install`

### `ERR_PNPM_NO_IMPORTER_MANIFEST_FOUND`

- **Cause:** running `pnpm` in the wrong directory
- **Fix:** `cd ci_slides`

## Build Script Warning

You may see:

```text
Ignored build scripts: esbuild
```

This is a pnpm security feature and does not prevent Slidev from running.

If needed:

```bash
pnpm approve-builds
```

## Version Snapshot (Record Yours)

Record versions with:

```bash
node -v
npm -v
pnpm -v
```
