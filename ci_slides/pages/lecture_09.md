---
layout: center
class: text-center
---

# Lecture 9
## GitHub Actions

---
layout: image-right
image: /images/lecture-08/t05_from_s06.png
backgroundSize: contain
---


# Workflow File Location
## Store workflow files in `.github/workflows`

<br>

- Workflow files must live in `.github/workflows/`.
- Use descriptive names, for example: `ci.yml`, `tests.yml`, `docs.yml`.
- One repository can have multiple workflow files.

---
layout: image-right
image: /images/lecture-08/t06_from_s07.png
backgroundSize: contain
---

# The `github-actions-demo.yml` Workflow
## Workflow file structure and key sections

- [https://docs.github.com/en/actions/quickstart](https://docs.github.com/en/actions/quickstart)

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest -q
```

---
layout: two-cols-header
---

# What Do These Two Lines Do?
## Understanding core workflow declarations

::left::


- `name`: label displayed in the Actions UI.
- `on`: events that trigger this workflow.
  - Example: `on: [push, pull_request]` catches both direct pushes and PR updates.
- Common trigger patterns:
  - push to specific branches (e.g., `main`)
  - pull request opened/synchronized
  - manual execution with `workflow_dispatch`
  - Use branch filters to avoid unnecessary runs.

::right::


```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest -q
```

---

# Triggering Workflows: `push` vs `pull_request`
## Why PR checks are usually the default

- `push`: runs when commits are pushed to a branch.
- `pull_request`: runs when proposed changes are opened or updated in a PR.
- For CI, **PR checks are the default** because they catch problems **before merge**.
- A common pattern is:
  - run on every `pull_request`
  - also run on `push` to `main` / `develop` after merges land

```yaml
on:
  pull_request:
  push:
    branches: [main, develop]
```
 
---
 layout: two-cols-header
---

# What Is `${{ }}`?
## GitHub expressions evaluate runtime context values

::left::

- Expressions are evaluated by Actions at runtime.
- `${{ github.actor }}` resolves to the username that triggered the run.
- `${{ github.ref_name }}` resolves to the branch or tag name.
- Use expressions in `if:`, `env:`, `with:`, and step arguments.
- `${{ matrix.operating-system }}` is used in matrix jobs to access the current OS value.

::right::
<br>
<br>
```yaml
jobs:
  test:
    runs-on: ${{ matrix.operating-system }}
    strategy:
      matrix:
        python-version: ["3.9"]
        operating-system: [windows-latest]  # [ubuntu-latest, windows-latest]
    env:
```

---


# Defining the jobs
## Understanding the `jobs` key

- Each job has an ID (for example `test`, `lint`, `docs`).
- Jobs can run in parallel unless dependencies are declared with `needs:`.
- Keep job responsibilities narrow for clearer failures.

---
layout: two-cols-header
---

# Defining the jobs: Key fields
## A workflow can contain one or more named jobs

::left::

- `runs-on`: execution environment (for example `ubuntu-latest`).
- `steps`: ordered units of work inside the job.
- `uses`: run a reusable action.
- `run`: execute shell commands directly.

::right::

```yaml
jobs:
  test:
    runs-on: ${{ matrix.operating-system}}
    strategy:
      matrix:
        python-version: ["3.9"]
        operating-system: [windows-latest]
    env:
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e '.[dev]'
      - name: Test with pytest
        env:
        run: |
          python3 -m pytest
```

---
layout: image-right
image: /images/lecture-08/t12_from_s20-21.png
backgroundSize: contain
---

# The full Explore-GitHub-Actions job
## Combining runner settings, steps, and actions

- Read from top to bottom: setup, install, validate, report.
- Every step should have a clear purpose and deterministic output.
- Fail fast on setup errors to save runner time.

---

# Job Dependencies with `needs:`
## Build pipelines from small jobs

- Jobs run in parallel by default.
- Use `needs:` to enforce ordering and to gate later jobs on earlier success.
- Keep jobs focused: `lint` → `test` → `build` → `release`.

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: ...

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps: ...
```

---
layout: two-cols-header
---
# Useful Job/Step Fields (Quick Hits)
## Keys you will see in most real workflows

::left::

- `name`: label in UI.
- `needs`: ordering/dependencies.
- `strategy.matrix`: run across versions.
- `env`: environment variables.
- `defaults`: default `shell` / `working-directory`.
- `if`: conditional execution.
- `timeout-minutes`: prevent hangs.

::right::

```yaml
jobs:
  test:
    name: Unit tests
    timeout-minutes: 10
    defaults:
      run:
        shell: bash
    env:
      PYTHONUNBUFFERED: "1"
    if: ${{ github.event_name == 'pull_request' }}
    steps:
      - name: Run tests
        run: pytest -q
```

---

# Secrets and Permissions
## Keep credentials safe and minimize access

- **Secrets:** stored in repo/org settings, referenced as `${{ secrets.NAME }}`. 
- **Permissions:** scope the default `GITHUB_TOKEN` to least privilege.

```yaml
permissions:
  contents: read

jobs:
  deploy:
    permissions:
      contents: read
      pages: write
      id-token: write
```

Don’t print secrets in logs; treat logs as public within the repo.
---

# Artifacts and Caching
## Speed up CI and keep the evidence

- **Artifacts:** upload test reports, logs, coverage, build outputs.
- **Caching:** speed up dependency installs (pip cache) and builds.

Artifact example:
```yaml
- name: Upload test results
  uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: .
```

---

# Debugging Failed Workflows
## Fast ways to find the real error

- Click the failed job → expand the failing step → read the first traceback/error.
- Add temporary debug output:
  - `python -V`, `pip list`, `pwd`, `ls -la`
- Re-run jobs after fixing the issue (avoid “retry until green” without changes).
- Keep your local commands aligned with CI (`ruff check .`, `pytest -q`).
---

# Building a Useful Sequence of Steps
## We can copy commands that work locally into run: operations

- Good ordering:
  - checkout repository
  - setup Python
  - install dependencies
  - run lint/tests
  - upload artifacts or coverage
- Marketplace actions: https://github.com/marketplace?type=actions

---

# Finding and Using Marketplace Actions
## Search, evaluate, pin, and add under `steps`

- Search the **GitHub Marketplace** for common tasks like coverage upload, docs deploy, or artifact handling.
- Prefer actions with:
  - clear documentation
  - recent updates
  - trusted publishers / healthy issue activity
- Avoid unpinned `@main`; prefer a stable major tag like `@v5` or a pinned SHA.
- Add optional actions only after your core CI (`ruff`, `pytest`) already works.

Example:
```yaml
- name: Upload coverage
  uses: codecov/codecov-action@v5
```

- This step belongs under the job’s `steps:` list.

---
layout: image-right
image: /images/lecture-08/t18_from_s27.png
backgroundSize: contain
---

# Actions for Common CI Tasks
## Reusable actions for testing, docs, and releases

- `actions/checkout` for repository checkout
- `actions/setup-python` for Python runtime
- `codecov/codecov-action` for coverage reporting
- `actions/upload-artifact` for logs/build outputs
- `.../emoji commit` for fun commit messages

Use these to avoid reinventing the wheel and to follow best practices.

---

# Activity: Build a PR-first pytest workflow
## Run tests on pull requests and on pushes to `main` / `develop`

- **Goal:** Create `.github/workflows/ci.yml` that runs `pytest` for proposed changes and merged code.

- **Workflow requirements:**
  - trigger on every `pull_request`
  - trigger on `push` only for `main` and `develop`
  - set up Python
  - install dependencies from `pyproject.toml`
  - run `pytest -q`

---

# Activity: Build a PR-first pytest workflow
## Run tests on pull requests and on pushes to `main` / `develop`

- **Starter YAML shape:**

```yaml
on:
  pull_request:
  push:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[tests]"
      - run: pytest -q
```

---

# Activity: Build a PR-first pytest workflow
## Run tests on pull requests and on pushes to `main` / `develop`

- **Starter files you may copy from this repo if helpful:**
  - `pytest.ini`
  - `test/` or `tests/`
  - `conftest.py`
  - `docs/` (optional, if you want a more complete project scaffold)

- **Stretch goals:**
  - add `ruff check .` before `pytest`
  - add a Python matrix (`3.10`, `3.11`, `3.12`)
  - verify the PR shows a green ✅ check before merge

- Reference: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
