---
layout: center
class: text-center
---

# Lecture 6
## CI/CD Fundamentals

---

# What Is CI/CD?
## Triggered Automation for Software Quality and Delivery

- **Continuous Integration (CI):** Merge small changes frequently and run automated checks on every push or pull request.

- **Continuous Delivery:** Keep the default branch releasable at all times.

- **Continuous Deployment:** Automatically deploy after all quality gates pass.

## How do I do this?
- Use a CI/CD platform (GitHub Actions, GitLab CI, etc.) to define workflows that run on repository events.

```yaml
on:
  push:
    branches: [ develop ]
    paths: [ 'docs/**' ]
  workflow_dispatch:
```

---
layout: image-right
image: /images/lecture-05/t11_from_s16.png
backgroundSize: contain
---

# Goal of CI/CD
## Catch issues early and maintain a high-quality codebase

- Prefer short-lived branches and small pull requests.

- Run checks on every pull request before merge.

- Block merge when required checks fail.

- Reduce late merge conflicts and release surprises.

---
layout: image-right
image: /images/lecture-05/t04_from_s04.png
backgroundSize: contain
---


# Typical Pipeline Stages
## From commit to deploy in repeatable steps

- Lint and format checks (`ruff`, `black --check`)

- Unit/integration tests (`unittest`, `pytest`)

- Package build (`python -m build`)

- Optional checks (coverage, docs, security)

- Release/deploy only when required checks succeed

---


# Implementing CI/CD in Practice
## A minimum viable pipeline for this course

- Version control with pull requests (`git` + GitHub).

- Automatically install dependencies from `pyproject.toml`.

- Run linting and tests (`ruff`, `pytest`) on push and pull request.

- Require passing checks before merging to `main`.

- Publish docs and releases automatically (`sphinx`). 

---

# Additional CI/CD tools in the workflow
## Code quality, coverage, documentation, and security checks

- Coverage reporting (`pytest-cov`, Codecov)

- Documentation build validation (Sphinx)

- Dependency and static security scanning (Dependabot, CodeQL)

- Branch protection rules (required checks and review)

---


# Local CI/CD workflows
## Run checks locally before pushing to the repository

- Use `pre-commit` to run fast checks before each commit.

- Run the same commands locally that CI will run remotely.

- This reduces failed pipelines and review delays.

```bash
pre-commit run --all-files
ruff check .
pytest -q
```

---

# Running the CI/CD workflow
## Selecting a Continuous Integration Platform

- This course uses GitHub Actions because our repositories live on GitHub.

- Other platforms include Jenkins, GitLab CI, CircleCI, and cloud-native CI tools.

- Most CI systems define workflows as YAML files executed by hosted runners.

These can be found in `.github/workflows/` for GitHub Actions.

---
layout: image-right
image: /images/lecture-05/t17_from_s22.png
backgroundSize: contain
---

# GitHub Actions Dashboard
## Viewing workflow runs and statuses

When a workflow is triggered, you can view its progress and results in the GitHub Actions dashboard:

- Check whether a run passed, failed, or was canceled.

- Open failed jobs to inspect logs and traceback output.

- Re-run failed jobs after fixing the issue.

---

# Activity: Add `pre-commit` + `ruff`
## Automatic linting before every commit

- **Goal:** Developers catch style/quality issues *before* pushing (and before CI).

- **1) Add an optional dependency group in `pyproject.toml`**

Add a dev group (name can be `dev`, `lint`, or `tools`):

```toml
[project.optional-dependencies]
dev = [
  "pre-commit",
  "ruff",
]
```

*(If you already have optional groups, just append `pre-commit` + `ruff`.)*

---

# Activity: Add `pre-commit` + `ruff`
## Automatic linting before every commit

- **2) Install the tools**

If you’re using pip:

```bash
python -m pip install -e ".[dev]"
```

Or if you’re not using editable installs:

```bash
python -m pip install ".[dev]"
```

---

# Activity: Add `pre-commit` + `ruff`
## Automatic linting before every commit

- **3) Create `.pre-commit-config.yaml`**

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.4
  hooks:
    # Run the linter.
    - id: ruff-check
    # Run the formatter.
    - id: ruff-format
```

- **4) Install and run pre-commit**

```bash
pre-commit install
pre-commit run --all-files
```

---

# Activity: Add `pre-commit` + `ruff`
## Automatic linting before every commit

- **5) Verify it’s working**
  - Make a tiny formatting error in a `.py` file.
  - Try committing → confirm pre-commit blocks the commit until it’s fixed.

- **Stretch goals**
  - Add `--show-fixes` or `--diff`.
  - Add more hooks (whitespace, trailing commas, check-yaml).
