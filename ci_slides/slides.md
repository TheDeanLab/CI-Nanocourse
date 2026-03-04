---
src: ./pages/intro.md
---

---
src: ./pages/lecture_01.md
---

---
src: ./pages/lecture_02.md
---

---
src: ./pages/lecture_03.md
---

---
src: ./pages/lecture_04.md
---

---
src: ./pages/lecture_05.md
---

---
src: ./pages/lecture_06.md
---

---
src: ./pages/lecture_07.md
---


---

layout: center
class: text-center
---

# Lecture 7
## Unit Testing and TDD

---

# Session Context
## Instructor and Course Context

- Conor McFadden
- Continuous Integration with Python Nanocourse 2023
---

# Unit Testing Overview
## Why unit tests are essential for reliable code

- Writing effective unit tests using python's testing frameworks.
- Incorporating test-driven development principles
---

# Software Review Overview
## Verification, code review, and testing in practice

- Tedious to do by hand, and automated tool support for verification is 	still an active area of research.
- Code review: Having somebody else carefully read your code, and reason informally about it, can be a good way to uncover bugs. It’s much like having somebody else proofread an essay you have written.
- Testing: Running the program on carefully selected inputs and checking the results.
- User Inputs? Logic errors? Hardware bugs?

---
layout: image-right
image: /images/lecture-07/t04_from_s04.png
backgroundSize: contain
---

# Types of Tests
## Unit, integration, and system testing levels

- Integration Test: Combined Unit Tests tested as a group.
- System (Smoke) Testing: Tests the entire system as a whole to verify that critical functionalities work.
---

# Python Testing Frameworks
## Comparing `unittest`, `pytest`, and `doctest`

- unittest: A testing framework included in the Python standard library. It provides a basic set of tools for writing and executing tests.
- pytest: A popular and powerful third-party testing framework. It encourages test-driven development (TDD) and provides features like fixtures and parameterized testing.
- doctest: A testing framework that allows you to embed tests within docstrings, making it useful for creating documentation that also serves as executable test cases.
---

# Writing a Unit Test
## Arrange, Act, Assert, and Cleanup

- Act: action that we would like to test, function or process.
- Assert: checking the result state to see if it matches expectations. Look at output and make judgment
- Cleanup: cleanup tests so other downstream tests aren’t influenced by results or attributes.


---
layout: image-right
image: /images/lecture-07/t07_from_s07.png
backgroundSize: contain
---

# Running Pytest
## Run tests from the command line with `pytest`

- Assert is True, the test passes!


---
layout: image-right
image: /images/lecture-07/t09_from_s09.png
backgroundSize: contain
---

# Pytest Test Discovery
## Pytest discovers functions prefixed with `test_`
---
layout: image-right
image: /images/lecture-07/t10_from_s10.png
backgroundSize: contain
---

# Test Parameterization
## Test multiple cases with `pytest.mark.parametrize`


---
layout: image-right
image: /images/lecture-07/t11_from_s12.png
backgroundSize: contain
---

# Fixtures in Pytest
## Reuse setup and teardown logic across tests

- They help avoid repeating setup code in multiple tests.
- Why Use Fixtures?
- Avoid duplicating setup code in every test.
- Keep test files clean and readable.
- Automatically clean up after tests run.

---
layout: image-right
image: /images/lecture-07/t12_from_s13.png
backgroundSize: contain
---

# Fixtures in Pytest: Example in PyCalc
## Using shared setup in `conftest.py`
---
layout: image-right
image: /images/lecture-07/t13_from_s14.png
backgroundSize: contain
---

# Key Binding Test in PyCalc Exercise
## Shared test fixtures and setup

- test_controller.py
- Fixtures  conftest.py
- Yield keyword to free resources after test.

---
layout: image-right
image: /images/lecture-07/t14_from_s15.png
backgroundSize: contain
---

# What Does `yield` Do?
## Fixture lifecycle: setup, yield, teardown

- YIELD: give it to your tests
- TEARDOWN: free your resources
---

# Unit Testing Best Practices
## Keep tests isolated, clear, and deterministic

- Test only one code or component at a time.
- Clear and consistent naming conventions.
- Fix bugs before moving on!
- “Test as you code”  Write you tests while the idea is still fresh.
---

# Test-Driven Development (TDD)
## Write tests first to drive implementation
---

# Conclusions
## Key takeaways from unit testing and pytest

- Writing tests are useful for making sure code is functioning properly and removing bugs during development
- Pytest is a useful framework for setting up tests
---

# Exercise
## Add test dependencies and write initial unit tests

- pip install –e .[dev] or pip install –e “.[dev]” on Mac
- Write a unit test to test _calculateResult function in controller.py
- If time is remaining, parameterize the test for _calculateResult

---
layout: center
class: text-center
---

# Lecture 8
## GitHub Actions


---

# Creating a GitHub Workflow
## Follow the official GitHub Actions quickstart

- Goal: run automated checks whenever code is pushed or a PR is opened.
- Start with one simple workflow, then extend it iteratively.
- Keep commands in CI aligned with commands you run locally.

---
layout: image-right
image: /images/lecture-08/t05_from_s06.png
backgroundSize: contain
---

# Workflow File Location
## Store workflow files in `.github/workflows`

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
layout: image
image: /images/lecture-08/t07_from_s08-09.png
backgroundSize: contain
---

# What Do These Two Lines Do?
## Understanding core workflow declarations

- `name`: label displayed in the Actions UI.
- `on`: events that trigger this workflow.
- Example: `on: [push, pull_request]` catches both direct pushes and PR updates.
---

# What Is `${{ }}`?
## GitHub expressions evaluate runtime context values

- Expressions are evaluated by Actions at runtime.
- `${{ github.actor }}` resolves to the username that triggered the run.
- `${{ github.ref_name }}` resolves to the branch or tag name.
- Use expressions in `if:`, `env:`, `with:`, and step arguments.

---
layout: image-right
image: /images/lecture-08/t09_from_s11.png
backgroundSize: contain
---

# What Do These Entries Do?
## Workflow triggers define when jobs run

- Common trigger patterns:
  - push to specific branches (e.g., `main`)
  - pull request opened/synchronized
  - manual execution with `workflow_dispatch`
- Use branch filters to avoid unnecessary runs.
---

# Defining the jobs
## Understanding the `jobs` key

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-08/t11_from_s13-14-15-16-17-18-19.png" alt="lecture-02 slide 13 image 1" class="max-h-80 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- Each job has an ID (for example `test`, `lint`, `docs`).
- Jobs can run in parallel unless dependencies are declared with `needs:`.
- Keep job responsibilities narrow for clearer failures.

---

# Defining the jobs: Key fields
## A workflow can contain one or more named jobs

- `runs-on`: execution environment (for example `ubuntu-latest`).
- `steps`: ordered units of work inside the job.
- `uses`: run a reusable action.
- `run`: execute shell commands directly.

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
layout: image-right
image: /images/lecture-08/t14_from_s23.png
backgroundSize: contain
---

# GitHub Marketplace
## Finding reusable actions for workflows

- Prefer well-maintained actions with clear documentation.
- Check update frequency, issue activity, and publisher trust.
---
layout: image-right
image: /images/lecture-08/t15_from_s24.png
backgroundSize: contain
---

# Search for Codecov
## Locating coverage-reporting actions

- Add coverage upload only after tests reliably run in CI.
- Coverage reports are useful for tracking testing gaps over time.
---
layout: image-right
image: /images/lecture-08/t16_from_s25.png
backgroundSize: contain
---

# Use the Latest Version
## Selecting the latest action reference

- Avoid unpinned `@main`.
- Prefer stable major tags (for example `@v4`) or pinned SHAs for stricter reproducibility.
---
layout: image-right
image: /images/lecture-08/t17_from_s26.png
backgroundSize: contain
---

# Copy the action as a step in your job
## Adding reusable actions under `steps`

```yaml
- name: Upload coverage
  uses: codecov/codecov-action@v5
```
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
---

# Exercise: Add a workflow to automatically run unit tests on git push to your repository
## Implement a workflow that runs `pytest`

- Minimum requirements:
  - trigger on `push` and `pull_request`
  - install dependencies from `pyproject.toml`
  - run `pytest -q`
- Stretch goals:
  - add a Python matrix (for example 3.10, 3.11, 3.12)
  - test on multiple OS runners (`ubuntu`, `macos`, `windows`)
- Reference: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

---
layout: center
class: text-center
---

# Lecture 9
## Public-Facing Documentation

---
layout: image-right
image: /images/lecture-09/t01_from_s01.png
backgroundSize: contain
---

# Public-Facing Documentation
## Principles for clear and maintainable project docs

- Lyda Hill Department of Bioinformatics
- UT Southwestern Medical Center
---

# Why do we care about documentation?
## Documentation supports users, collaborators, and future maintenance

- It helps other people use our software.
- It helps other people contribute to our software.
- It helps us write better software.
- [https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
---

# Types of documentation
## Requirements, architecture, API, and end-user docs

- Architecture – How do the pieces of the software fit together?
- Technical – How does each function work? Application programming interface (API) docs.
- End user – Getting started guides. How-tos.

---
layout: image-right
image: /images/lecture-09/t04_from_s04.png
backgroundSize: contain
---

# Software Licenses and Project Documentation
## Choose a license aligned with your collaboration goals

- [https://choosealicense.com/](https://choosealicense.com/)
---
layout: image-right
image: /images/lecture-09/t05_from_s05.png
backgroundSize: contain
---

# GPLv3 and MIT: Practical Trade-Offs
## Copyleft obligations versus permissive reuse
---

# Companies may enforce use of their own preferred licenses
## Account for institutional and employer policy requirements

- UT Southwestern’s open-source software license is here: https://www.utsouthwestern.edu/about-us/administrative-offices/technology-development/agreements/open-source-release-of-software.html
- You MUST use this license if you develop software on any UTSW machine or for any UTSW purpose.
- UNLESS you are using code from a GPLv3-licensed software, in which case I think you should use a GPLv3 license, but you should confirm this with a UTSW lawyer.
---

# Documentation languages
## HTML, Markdown, and reStructuredText basics

- Markdown (.md)
- reStructuredText (.rst)
- Many more: https://en.wikipedia.org/wiki/List_of_document_markup_languages

---
layout: image-right
image: /images/lecture-09/t08_from_s08.png
backgroundSize: contain
---

# Documentation languages are simple languages, close to standard word processing
## Readable markup for technical writing

- [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)
- [https://sphinx-tutorial.readthedocs.io/cheatsheet/](https://sphinx-tutorial.readthedocs.io/cheatsheet/)
---
layout: image-right
image: /images/lecture-09/t09_from_s09.png
backgroundSize: contain
---

# GitHub uses Markdown
## READMEs, issues, and PRs render Markdown by default
---

# Exercise: Write a README.md
## Essential sections for an effective README

  - A brief description of the project
  - Installation instructions
  - Links to further documentation, including how to contribute
  - How to cite the repository, if applicable
  - Badges, if applicable
  - See https://github.com/mwaskom/seaborn/blob/master/README.md for a good example
- GitHub will display README.md by default on the home page of your repo

---
layout: image-right
image: /images/lecture-09/t11_from_s11.png
backgroundSize: contain
---

# Docstring style examples
## Google-style docstrings with reStructuredText

- Google style

---
layout: image-right
image: /images/lecture-09/t12_from_s12.png
backgroundSize: contain
---

# Docstring style examples (NumPy)
## NumPy-style docstrings
---

# Documentation frameworks
## Tools that generate docs from code and text

- Import the code to generate documentation based on runtime inspection
- Parse and analyze the code statically (without running it)
- Compile documentation languages to PDFs, HTML, etc.
- [https://wiki.python.org/moin/DocumentationTools](https://wiki.python.org/moin/DocumentationTools)
---
layout: image-right
image: /images/lecture-09/t14_from_s14.png
backgroundSize: contain
---

# Sphinx is the primary documentation framework for Python
## Generate API and narrative documentation from source

- [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/)
- Compiles Python docstrings and reStructuredText files to PDFs, HTML
- Can be modified to use Markdown: https://www.sphinx-doc.org/en/master/usage/markdown.html
---
layout: image-right
image: /images/lecture-09/t15_from_s15-16.png
backgroundSize: contain
---

# An example of a docstring compiled to HTML by Sphinx
## From docstrings to publishable HTML output
---

# Building Documentation for the Project
## Using the Sphinx quickstart workflow
---

# Installing Documentation Dependencies
## Install documentation dependencies from `pyproject.toml`

- pip install –e .[docs] from within your repository folder(pip install –e ‘.[docs]’ on a Mac)
- This installs the optional dependencies listed under docs in pyproject.toml

---
layout: image-right
image: /images/lecture-09/t18_from_s19-20.png
backgroundSize: contain
---

# Generating the Documentation Source Folder
## Initialize a `docs/` project with `sphinx-quickstart`

- Run sphinx-quickstart in this folder.

---
layout: image-right
image: /images/lecture-09/t19_from_s21.png
backgroundSize: contain
---

# Directory structure of documentation folder
## Understanding `source/`, `_build/`, and configuration files
---
layout: image-right
image: /images/lecture-09/t20_from_s22.png
backgroundSize: contain
---

# Build HTML in the `docs` Folder
## Build output exists before content is configured

---
layout: image-right
image: /images/lecture-09/t21_from_s23.png
backgroundSize: contain
---

# How `toctree` Defines Site Navigation
## Control site navigation with the `toctree`

- It is empty by default
- You can add documents by listing them in three

---
layout: image-right
image: /images/lecture-09/t22_from_s24-25.png
backgroundSize: contain
---

# Autosummary helps us with the API documentation
## Automatically generate API reference stubs

- [https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
---
layout: image-right
image: /images/lecture-09/t23_from_s26.png
backgroundSize: contain
---

# Templating
## Customize generated pages with Jinja templates

- These allow us to change the way data is presented on different pages
- For example, the autosummary module template is located at


---
layout: image-right
image: /images/lecture-09/t24_from_s27.png
backgroundSize: contain
---

# Templates enable us to produce a more comprehensive autosummary
## Reference template for richer module pages


---
layout: image-right
image: /images/lecture-09/t25_from_s28.png
backgroundSize: contain
---

# Autosummary output with custom templates
## Enhance generated pages with custom Jinja templates

---
layout: image-right
image: /images/lecture-09/t26_from_s29.png
backgroundSize: contain
---

# Documentation Exercises
## Hands-on documentation practice

- Write installation.rst and/or quickstart.rst. Compile the new docs to HTML. Verify the compilation worked by opening the docs in your web browser.
- What happens if you change api.rst to the following? Why?
---

# Publishing documentation with GitHub Pages
## Publish compiled documentation automatically

- Ideally, we do this automatically, updating whenever new documentation is written.
- GitHub actions lets you do this easily with GitHub Pages.


---
layout: image-right
image: /images/lecture-09/t28_from_s32.png
backgroundSize: contain
---

# GitHub Pages
## Host documentation directly from your repository

- [https://pages.github.com/](https://pages.github.com/)
- Hosts websites directly out of a GitHub repository
---

# Exercise: Create a GitHub workflow that builds your docs and deploys it to a GitHub page
## Automate docs build and deployment with GitHub Actions

- Hint: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages






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


