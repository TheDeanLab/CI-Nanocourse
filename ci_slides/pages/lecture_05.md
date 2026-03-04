---
layout: center
class: text-center
---

# Lecture 5
## Repository Organization

---

# Repository Organizational Strategies
## Fighting Entropy

Organizing a GitHub repository for Python software in a structured and consistent manner is crucial for clarity, collaboration, and maintainability. 

- Use a standard project layout. Common directories include:

  - `src/` For the main source code.

  - `tests/` For unit tests.

  - `docs/` For documentation.

  - `scripts/` For utility scripts and auxiliary code.

  - `data/` For data files, if applicable. See [Git LFS](https://git-lfs.com) for large files.

---

# Repository Organizational Strategies
## Must-Have Repository Files

- **README File** - Always have a README.md at the root. It should include:
  
  - Project title and brief description.
  
  - Installation and usage instructions.
  
  - Contribution guidelines.
  
  - Licensing information.

- License - Include a **LICENSE file** that clearly states the licensing terms.

- Badges - Use badges in the README.md to quickly display project status, such as build status, test coverage, and package version.

---
layout: image-right
image: /images/lecture-04/t03_from_s03.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Must-Have Repository Structure

- `.gitignore` for generated and local-only files.

- `requirements.txt` or `pyproject.toml` for dependencies.

- `docs/` for documentation.

- `tests/` for automated validation.

- `src/` for application code.

---
layout: image-right
image: /images/lecture-04/t04_from_s04.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Bonus Tools


- `CODE_OF_CONDUCT.md` for community expectations.

- `CONTRIBUTING.md` for contributor workflow.

- `CHANGELOG.md` for release history.

- Templates for consistent submissions.
  - `.github/ISSUE_TEMPLATE.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`

---

# Code Organizational Strategies
## Maintaining Structure as Projects Scale

- Organizing code in Python is crucial for maintainability, scalability, and clarity.

  - **Modularity:** Divide your code into modules and packages, each with a specific responsibility.
  
  - **Naming Conventions:** Use clear and descriptive naming conventions. For example:  `data_source.py`, `file_management.py`, `data_visualization.py`.
  
  - **Code Reusability:** Abstract out common functionalities into utility functions or base classes to avoid repetition and enhance reusability.

---

# Code Organizational Strategies
## Activity #7

You’re going to take a “messy” repository and make it look like a professional Python project.

- **1) Create a standard layout** (commit as you go)
  - `src/<package_name>/__init__.py`
  - `tests/`
  - `docs/` (can be empty for now)
  - `scripts/` (optional, if you have helper scripts)
  - `.github/` (for GitHub-specific config)

- **2) Move code into `src/`**
  - Put your Python module(s) under `src/<package_name>/`
  - Update imports so code still runs.

---

# Code Organizational Strategies
## Activity #7 (cont.)

- **3) Add “community health” files**
  - `README.md` (clear install + usage)
  - `LICENSE`
  - `CONTRIBUTING.md` (how to run tests + how to propose changes)
  - `CODE_OF_CONDUCT.md` (short, standard expectations)

- **4) Add GitHub templates**
  - `.github/ISSUE_TEMPLATE/bug_report.md`
  - `.github/ISSUE_TEMPLATE/feature_request.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`

---

# Code Organizational Strategies
## Activity #7 (cont.)

- **5) Open one Issue + one PR**
  - Create an Issue using your new template.
  - Create a branch, make at least one improvement commit, and open a PR using the PR template.

