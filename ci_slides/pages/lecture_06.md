---
layout: center
class: text-center
---

# Lecture 6
## CI/CD Fundamentals

---

# What Is CI/CD?
## CI validates code changes; CD manages release automation

- **Continuous Integration (CI):** Merge small changes frequently and run automated checks on every push or pull request.

- **Continuous Delivery:** Keep the default branch releasable at all times.

- **Continuous Deployment:** Automatically deploy after all quality gates pass.

---
layout: image-right
image: /images/lecture-05/t03_from_s03.png
backgroundSize: contain
---

# Vocabulary
## Core CI/CD Terminology

- *Build:* Turn source code into an installable or runnable artifact.

- *Test:* Verify expected behavior automatically.

- *Release:* Version and publish an artifact for users.

- *Deploy:* Promote a release to an environment (staging/production).

- *Pipeline:* Ordered automation steps that enforce quality gates.

---
layout: image-right
image: /images/lecture-05/t04_from_s04.png
backgroundSize: contain
---

#  Unit Tests
#### How Do We Know This Function Works?

```python
def square(x):
    """Return the square of a number."""
    return x * x
```

#### You Write Tests
```python
def test_square():
    """Ensure the square function works correctly."""
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```

---

# Python Testing Frameworks
## 

**`unittest` (built-in)**
  - ✅ Standard library, no extra dependency.
  - ✅ Class-based test organization (`TestCase`), good for large suites.
  - ✅ Comes with useful tools like `mock`.
  - ❌ More boilerplate (classes, `self.assert...` methods).
  - ❌ Less ergonomic parametrization/fixtures (though possible).

**`pytest` (third-party)**
  - ✅ Minimal boilerplate: plain `assert` and simple test functions.
  - ✅ Powerful **fixtures** and **parametrization**.
  - ✅ Great plugin ecosystem (`pytest-cov`, `pytest-xdist`, etc.).
  - ❌ External dependency (needs installing/pinning).
  - ❌ More “magic” (auto-discovery, fixture injection) to learn at first.

---

# Python Testing Frameworks
## `pytest` vs `unittest`

**Rule of thumb**
  - Use **`pytest`** for most new projects (clean syntax + great CI experience).
  - Use **`unittest`** when you need pure-stdlib or you’re extending an existing `unittest` suite.


**Common test levels**
  - *Unit:* isolated behavior in a function/module.
  - *Integration:* interaction between components.
  - *System:* end-to-end behavior in realistic conditions.
  - *Regression:* prevents previously fixed bugs from returning.

---

# Typical Pipeline Stages
## From commit to deploy in repeatable steps

- Lint and format checks (`ruff`, `black --check`)

- Unit/integration tests (`pytest`)

- Package build (`python -m build`)

- Optional checks (coverage, docs, security)

- Release/deploy only when required checks succeed

---
layout: image-right
image: /images/lecture-05/t11_from_s16.png
backgroundSize: contain
---

# Goal of CI/CD
## Keep changes close to `main` through frequent integration

- Prefer short-lived branches and small pull requests.

- Run checks on every pull request before merge.

- Block merge when required checks fail.

- Reduce late merge conflicts and release surprises.

---

# Why is CI/CD useful?
## Quality, reliability, and faster feedback cycles


- Makes failures visible within minutes, not days.

- Prevents broken code from reaching shared branches.

- Improves reproducibility for research code and analysis workflows.

- Increases confidence when multiple contributors are involved.

---

# Implementing CI/CD in Practice
## A minimum viable pipeline for this course

- Version control with pull requests (`git` + GitHub).

- Install dependencies from `pyproject.toml`.

- Run linting and tests (`ruff`, `pytest`) on push and pull request.

- Require passing checks before merging to `main`.

- Optional extension: publish docs and releases automatically.

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

---
layout: image-right
image: /images/lecture-05/t17_from_s22.png
backgroundSize: contain
---

# GitHub Actions Dashboard
## Viewing workflow runs and statuses

- Check whether a run passed, failed, or was canceled.

- Open failed jobs to inspect logs and traceback output.

- Re-run failed jobs after fixing the issue.

---
layout: image-right
image: /images/lecture-05/t18_from_s23.png
backgroundSize: contain
---

# GitHub Actions Workflow Example
## Reading a basic workflow YAML file

- Core keys you will see: `name`, `on`, `jobs`, `runs-on`, `steps`.

- Each job runs in a clean environment unless artifacts/cache are restored.

- We will build one of these step-by-step in Lecture 8.