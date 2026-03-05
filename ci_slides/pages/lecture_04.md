---
layout: center
class: text-center
---
# Lecture 4
## Github Essentials

---

# Github Essentials
## What GitHub Gives You

- **Git hosting + collaboration**: repos, branches, forks, PRs, reviews.

- **Project planning**: Issues, Labels, Milestones, Projects (boards), assignees.

- **Automation**: GitHub Actions (CI), scheduled jobs, reusable workflows.

- **Release management**: tags, Releases, release notes, changelogs.

- **Documentation**: Markdown rendering, wikis, GitHub Pages.

- **Code quality**: required checks, branch protection rules, CODEOWNERS.

- **Security**: Dependabot alerts/PRs, secret scanning, security advisories.

- **Integrations**: Apps/webhooks, Marketplace, IDE integrations.

---

# Github Essentials
## Issue Tracking


- GitHub provides integrated issue, branch, and PR tracking.

- Each issue assigned a number (#638) which can be used as a tag in commits, comments, etc.

- Can be designated with a label (e.g., low priority).

- Can be assigned to an individual.

- Links PRs automatically

---
layout: image-right
image: /images/lecture-03/s13_img01.png
backgroundSize: contain
---

# Github Essentials
## Issue Creation

- Title: concise and descriptive.

- Expected behavior vs actual behavior.

- Steps to reproduce.

- Full traceback or error output.

- Environment: OS, Python, package versions.

- Relevant logs.

---
layout: image-right
image: /images/lecture-03/s14_img01.png
backgroundSize: contain
---

# Github Essentials
## Issue Creation

- Add screenshots or recordings when useful.

- Include severity and user impact.

- Provide workaround or minimal repro code.

- Add labels and regression details when relevant.

- Include extra context: frequency and scope.

---
layout: two-cols-header
---

# Github Essentials
## Issue Formatting

::left::

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s16_img01.png" alt="lecture-03 slide 16 image 1" class="max-h-90 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

::right:: 

- GitHub Issues support styling with Markdown.

- Can create checklists, headers, links, images, mention people/teams/issues/pull requests, quote code, create blocks, dropdowns, and more.

- [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

---

# Github Essentials
## Branch Linking


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s17_img01.png" alt="lecture-03 slide 17 image 1" class="max-h-50 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-03/s17_img02.png" alt="lecture-03 slide 17 image 2" class="max-h-50 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- By creating a branch that is directly linked to the issue, all progress on that issue is tracked.

- When a PR is approved, the issue is automatically closed.

---
layout: image-right
image: /images/lecture-03/s12_img01.png
backgroundSize: contain
---

# Github Essentials
## Pull Request (PR) Workflow

- Create a branch from `main` (often linked to an Issue).
- Make small commits; reference the issue in commits/PR (`Fixes #123`).
- Open a PR early (**Draft PR** if it’s not ready).
- Request review; respond to feedback with additional commits.
- Keep the PR up to date (resolve conflicts, re-run checks).
- Merge (squash/merge/rebase) and delete the branch.
- Confirm the issue is closed and the change is deployed/released if needed.

--- 

# Github Essentials
## Event Driven Tests

- Run automated checks when repository events occur (push, pull request, release).

- In GitHub Actions, each workflow defines **triggers** (e.g., `on: push`, `on: pull_request`).

- On a PR, GitHub aggregates results as **status checks** (✅/❌) directly on the PR.

- If branch protection is enabled, you can require these checks to pass **before merge**.

- Typical PR “checks” include linting, unit tests, type checks, build/docs, and security scans.
 
- Start with fast checks: linting and unit tests.
 
- Add project-specific checks: documentation build, coverage, and security scans.
 
- In this course, we implement these checks with GitHub Actions in Lecture 8.
