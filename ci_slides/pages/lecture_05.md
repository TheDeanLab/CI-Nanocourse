---
layout: center
class: text-center
---

# Lecture 5
## Repository Organization

---
layout: image-right
image: /images/lecture-04/t03_from_s03.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Must-Have Repository Files

Organizing is crucial for clarity, collaboration, and maintainability. Use a standard project layout. Common directories include:

  - `src/<package_name>/` For the main source code.
  - `tests/` For unit tests.
  - `docs/` For documentation.
  - `scripts/` For utility scripts and auxiliary code.
  - `data/` For data files. See [Git LFS](https://git-lfs.com).

---

# Repository Organizational Strategies
## Must-Have Repository Files

- **README File** - Always have a README.md at the root. It should include:
  
  - Project title and brief description.
  
  - Installation and usage instructions.
  
  - Contribution guidelines.

- License - Include a **LICENSE file** that clearly states the licensing terms.


---
layout: image-right
image: /images/lecture-04/t04_from_s04.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Bonus Additions

- Badges - Included in README.md to quickly display project status, test coverage, and package version.
- `CODE_OF_CONDUCT.md` for community expectations.
- `CONTRIBUTING.md` for contributor workflow.
- `CHANGELOG.md` for release history.
- Templates for consistent submissions.
  - `.github/ISSUE_TEMPLATE.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`


---

# Code Organizational Strategies
## Activity

You’re going to make your shared repository look like a professional Python project.

- **1) Create a standard layout** (commit as you go)
  - `src/<package_name>/__init__.py`
  - `tests/`
  - `docs/` (can be empty for now)
  - `scripts/` (optional, if you have helper scripts)
  - `.github/` (for GitHub-specific config)
 

---

# Code Organizational Strategies
## Activity

- **2) Create your first module in `src/`**
  - Create a package at `src/<package_name>/`
  - Add a simple module file, e.g. `src/<package_name>/hello.py`:

```python
def main() -> None:
    print("Hello from your first package!")
```

  - Make sure you have `src/<package_name>/__init__.py` so Python treats it as a package.
  
- **3) Add a shortcut command in `pyproject.toml`**
  - In `pyproject.toml`, add a console script entry point:

```text
[project.scripts]
<package_name> = "<package_name>.hello:main"
```

---

# Code Organizational Strategies
## Activity

  - Reinstall your project to update the console script:
  - After installing your project, you should be able to run:

```bash
<package_name>
```

This should execute the `main()` function in `src/<package_name>/hello.py` and print the message.

