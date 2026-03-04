---
layout: center
class: text-center
---

# Introduction to Collaborative Software Development
## Course Overview and Learning Objectives
---

# Course Structure
## Day 1

- Introduction to Collaborative Software Development
- Environment Management & Git Essentials
- Organizational Strategies, and Collaborative Development Workflows
- Pre-Commit Hooks, Linters, Code Formatters


## Day 2

- Unit Testing and Test-Driven Development (TDD)
- Setting up Continuous Integration Pipelines on GitHub
- Public-Facing Documentation
---

# Expectations
## Coding with Python

- Mandatory
  - How to work with Python Data Structures (dictionaries, lists, tuples, etc.)…
  - Python Control Flow (for, while, if, else, elif, break, continue)…
- Recommended
  - Object Oriented Programming (classes, objects, inheritance)…
- Bonus
  - Parallel Processing with Python (multi-threading, multi-processing)…
---

# Goals
## Building a Foundation

- Establish your own Repository with CI, Documentation, etc.
- Maintain stable, clean code.
- Work collaboratively on software development.
- Be able to contribute to an Open-Source Project.

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
layout: center
class: text-center
---

# Lecture 4
## Organization and MVC

---

# Repository Organizational Strategies
## Fighting Entropy

- Organizing a GitHub repository for Python software in a structured and consistent manner is crucial for clarity, collaboration, and maintainability.

#### Directory Structure:

- Use a standard project layout. Common directories include:

  - `src/` For the main source code.

  - `tests/` For unit tests.

  - `docs/` For documentation.

  - `scripts/` For utility scripts and auxiliary code.

  - `data/` For data files, if applicable.

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

- Issue/PR templates for consistent submissions.

- Dependabot (or similar) for dependency security.

---

# Code Organizational Strategies
## Maintaining Structure as Projects Scale

- Organizing code in Python is crucial for maintainability, scalability, and clarity.

  - **Modularity:** Divide your code into modules and packages, each with a specific responsibility.
  
  - **Naming Conventions:** Use clear and descriptive naming conventions. For example:  `data_source.py`, `file_management.py`, `data_visualization.py`.
  
  - **Code Reusability:** Abstract out common functionalities into utility functions or base classes to avoid repetition and enhance reusability.

---

# Model-View-Controller Architecture
## A Guiding Framework

- The "Model" represents the data and logic, governing the rules and data manipulation.

- The "View" displays the data, handling the presentation and user interface elements.

- The "Controller" manages user input, interpreting it to update the model and view accordingly, acting as a bridge between the two.

- The Model-View-Controller (MVC) architecture is a design pattern that separates software applications into three interconnected components.
---

# Model-View-Controller Architecture
## The View

- Handles the **User Interface (UI):** Defines how data is presented to the user and how they interact with it.

- **Receives User Input** - While the View primarily focuses on display, it also captures user input, such as button clicks, text input, or gestures, and forwards them to the Controller for processing.

- **Stateless** - Ideally, the View should be stateless, meaning it displays data without storing or processing it. Any data or logic-related tasks should be handled by the Model or Controller.

- **Reactive to *Model*** - The View reflects changes in the Model. When the data in the Model changes, the View updates automatically to display the latest information to the user.

- **Decoupled from *Model* and *Controller*** - To maintain the separation of concerns, the View should be decoupled from the Model and Controller. This means changes in the View shouldn't directly affect the Model's data or the Controller's logic, ensuring modularity and ease of maintenance.

---

# Model-View-Controller Architecture
## The View: How to Build

- Python offers a variety of libraries and frameworks for creating Graphical User Interfaces (GUIs). <br>Here are some of the most popular ones:

- Tkinter:
  - The standard GUI library for Python, bundled with most Python installations.
  - Offers a simple way to create windows, dialogs, buttons, and other GUI elements.

- PyQt and PySide:
  - Bindings for the Qt framework: Create professional-looking applications with advanced features.
  - PyQt is available under GPL or commercial licenses, while PySide is available under LGPL.

- wxPython:
  - Bindings for wxWidgets C++ library: Native-looking GUI applications for Windows, macOS, and Linux.


---

# Model-View-Controller Architecture
## The Controller

- Acts as a ***mediator*** between the Model and the View. It receives user input from the View, processes it (possibly updating the Model), and then returns the display output to the View.

- **Event Specification** - It specifies which elements in the view should trigger events when selected.

- **User Input Handling** - One of the primary responsibilities of the Controller is to handle user input. Whether it's a button click, form submission, or any other interaction in the View, the Controller decides what should happen in response.

- **Logic Execution** - While the Model deals with data and the View deals with presentation, the Controller is where much of the application's business logic is executed. It determines how the application should respond to various user inputs and actions.

- **State Management** - The Controller often manages the flow of data and the state of the application. It can decide which View to display next, fetch data from the Model to update the View, or store data in the Model based on user input.

---

# Model-View-Controller Architecture
## The Model

- **Data Representation** - The Model represents the application's data and the rules that govern access to and updates of this data. It is the central component that holds the core functionality.

- **Data Storage** - Often, the Model is responsible for retrieving or storing data, which can be in a database, file, or any other storage mechanism.

- **Data Notification** - When data in the Model changes, it can notify the View so that the interface can be updated accordingly. This ensures that the user interface reflects the current state of the data.

- **Logic** - While the Controller handles user interactions, the Model contains the core logic that dictates how data can be created, stored, modified, and retrieved. It enforces rules, constraints, and validations related to the data.

---

# Organization and MVC
## Activity #7

- Upload individual files to GitHub.

- Place code in appropriate organizational structure.

---
layout: center
class: text-center
---

# Lecture 5
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

# How Do We Know This Function Works?
## Unit tests catch regressions early

```python
def square(x):
    """Return the square of a number."""
    return x * x

def test_square():
    """Ensure the square function works correctly."""
    assert square(2) == 4
    assert square(-3) == 9
```

---
layout: image-right
image: /images/lecture-05/t04_from_s04.png
backgroundSize: contain
---

# How Do We Know This Function Works?

- Run tests quickly with `pytest -q` locally and in CI.

- Common test levels:
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

---
layout: center
class: text-center
---

# Lecture 6
## Code Quality and Linting

---

# Outline
## Defining Clean Code

- Techniques to Maintain Clean Code
  - Code formatters and linting

- Utilizing pre-commit hooks to enforce coding standards and maintain code with Github.

- Exercise

---

# What is Clean Code?
## Readable, maintainable code is easier to review and evolve

- Consistent formatting. Should follow PEP 8 standards for Python.

- Meaningful names - descriptive variable, function, and class names.

- Simple. Functions and classes should do one thing only, and do it well.

- Well-documented.

- Type hinted.

- Testable.

---

# PEP 8 Naming Conventions
## Classes - CamelCase (MyClass)

- *Variables* - snake_case and lowercase (`first_name`)

- *Functions* - snake_case and lowercase (`quick_sort()`)

- *Constants* - snake_case and uppercase (`PI = 3.14159`)

- Modules should have short, snake_case names and all lowercase (`numpy`)

- Single quotes and double quotes are treated the same (just pick one and be consistent)

- Triple quotes should always be """Your text here""" not '''Your text here'''

---

# Variable Naming
## Use descriptive `snake_case` identifiers

- Use descriptive, lowercase names – Variables should be meaningful and easy to understand.<br>
  ✅ `max_users = 100`  
  ❌ `mu = 100`

- Use underscores for multi-word names (snake case) – Improves readability.<br>
  ✅ `user_count = 10`  
  ❌ `userCount = 10` *(CamelCase is for classes, not variables)*

- Avoid single-letter names (except for short loops) – Be explicit.<br>
  ✅ `temperature_celsius = 25.0`<br>
  ❌ `t = 25.0` *(Is this Time? Temperature? ... Units?)*

---

# Variable Naming
## Use descriptive `snake_case` identifiers

- Constants should be uppercase with underscores – Used for values that don’t change.<br>
  ✅ `MAX_RETRIES = 5`<br>
  ❌ `maxRetries = 5`

- Private variables start with an underscore – Signals internal use.<br>
  ✅ `_cache = {}`<br>
  ❌ `cache = {}` *(unless public)*

- Avoid reserved keywords – Prevent conflicts with Python’s built-in functions.<br>
  ✅ `class_name = "Intro to CI"`<br>
  ❌ `class = "Intro to CI"` *(conflicts with the class keyword)*

---

# Function Naming
## Choose verb-based, descriptive function names

- Use lowercase with underscores – Improves readability and consistency.<br>
  ✅ `def get_user_data():`<br>
  ❌ `def GetUserData():` *(CamelCase is for classes)*

- Use descriptive names – Functions should clearly indicate their purpose.<br>
  ✅ `def calculate_total_price():`  
  ❌ `def calc():`

- Use verbs for function names – Functions perform actions, so names should reflect that.<br>
  ✅ `def fetch_records():`  
  ❌ `def records():`

---

# Function Naming
## Choose verb-based, descriptive function names

- Use a leading underscore for internal or private functions – Signals intended internal use.<br>
  ✅ `def _connect_to_db():`  
  ❌ `def connect_to_db():` *(if meant to be private)*

- Avoid using built-in function names – Prevents accidental overrides.<br>
  ✅ `def format_report():`  
  ❌ `def format():` *(overrides Python’s built-in format function)*

- Use double leading underscores only for name-mangling in classes – Rarely needed.<br>
  ✅ `class Example:  def __private_method(self):` <br>
  *Double underscore automatically renamed within a class…*

---

# Class Naming
## Use `PascalCase` nouns for class names

- Use CapWords (PascalCase) – Each word starts with a capital letter, with no underscores.<br>
  ✅ `class DataProcessor:`<br>
  ❌ `class data_processor:`

- Class names should be nouns or noun phrases – Represents objects or entities.<br>
  ✅ `class UserProfile:`<br>
  ❌ `class processUser():` *(Functions use verbs, not classes)*

- Avoid abbreviations – Use clear and meaningful names.<br>
  ✅ `class AuthenticationManager:`<br>
  ❌ `class AuthMgr:`

---

# Class Naming
## Use `PascalCase` nouns for class names

- Use leading underscores for internal classes – Signals that the class is for internal use only.<br>
  ✅ `class _InternalHelper:` <br>
  ❌ `class InternalHelper:` *(if not meant for external use)*

- Use metaclass naming convention – Append "Meta" if defining a metaclass.<br>
  ✅ `class CustomMeta(type):` <br>
  ❌ `class CustomMetaclass:`

- Exception classes should end with `Error` – Makes it clear they are exceptions.<br>
  ✅ `class ValidationError(Exception):`<br>
  ❌ `class ValidationIssue:`

---

# Line Formatting
## Prefer readable line lengths and wrapped signatures

<!-- code:start -->
```python
def process_large_dataset(data):
    """Processes a dataset and returns useful statistics."""
    # implementation here
    return {}


def process_large_dataset_with_very_long_name(
    data,
    additional_parameters,
    more_params,
):
    """Prefer wrapped signatures over single long lines."""
    return {}
```
<!-- code:end -->

- Lines should not exceed 79 characters
- Improves readability, especially in side-by-side comparisons.
---

# Line Formatting
## Clean Code

- Avoid multiple statements or imports on the same line
- Use separate lines for clarity.
<!-- code:start -->
```python
import os, sys

x = 5; y = 10
print(x + y)
```
<!-- code:end -->

<!-- code:start -->
```python
import os
import sys

x = 5
y = 10
print(x + y)
```
<!-- code:end -->
---

# In-line Comments
## Comments Should Clarify, Not Contradict

- Comments should be complete sentences.

- Comments should have a space after the # sign with the first word capitalized.

- Don’t litter commented code throughout your software.

---

# Documenting Code
## Write clear, structured docstrings:
<br>
<div style="max-height: 400px; overflow-y: auto;">

```python
def divide(a: float, b: float) -> float:
    """
    Divides two numbers.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        Result of division.

    Raises
    ------
    ZeroDivisionError
        If `b` is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

</div>

---

# Coding Principles
## Don’t Repeat Yourself

- Keep it Simple

- Separation of Concerns

- Split classes into multiple subclasses, inheritances, abstractions, interfaces.

- SOLID Principles of Coding: (https://www.pentalog.com/blog/it-development-technology/solid-principles-object-oriented-programming/)

---

# Methods to Improve Code Formatting
## Decorators

<!-- code:start -->
```python
from functools import wraps


def log_runtime(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Running {fn.__name__}...")
        return fn(*args, **kwargs)

    return wrapper


@log_runtime
def load_dataset(path):
    return open(path, encoding="utf-8").read()
```
<!-- code:end -->

- Define inner function inside function to call instead of defining inner function in each function call

- Improves modularity

---

# Methods to Improve Code Formatting
## Context Managers

<!-- code:start -->
```python
from pathlib import Path

config_path = Path("settings.toml")

with config_path.open("r", encoding="utf-8") as f:
    config_text = f.read()
```
<!-- code:end -->

- Manage how to interact with external databases and files.

- Automatically opens and closes files, avoiding complications when errors occur.

---

# Methods to Improve Code Formatting
## Iterators

<!-- code:start -->
```python
def iter_valid_rows(rows):
    for row in rows:
        if row.get("is_valid"):
            yield row


for row in iter_valid_rows(records):
    print(row["id"])
```
<!-- code:end -->

- Use functions to iterate through variables

---

# Linting and Code Formatting
## Static analysis versus style formatting

- Linting identifies formatting errors that can alter functionality of code and can correct for formatting
  - Indentation errors, unused variables, etc. Enforces PEP 8 standards.

- Code formatting changes stylistic appearance of code

- Linting is distinct from formatting because linting analyzes how the code runs and detects errors whereas formatting only restructures how code appears.

---

# Automated Linting and Code Formatting

- **Pylint:** Basic Python Code Linter

- **Flake8:** Python Code Linter to identify style differences in code

- **Black:** "Uncompromising and opinionated" PEP 8 compliant code formatter

- **Ruff:** Extremely fast, Rust-based code formatter and linter

---

# Black: Automated Code Formatting
## Automatically enforce consistent style with Black

<!-- code:start -->
```bash
black src tests
black --check .
black --diff .
```
<!-- code:end -->

<br>
<hr>
<br>

# Ruff: Automated Code Linting
## Detect unused imports, variables, and style violations

<!-- code:start -->
```bash
ruff check .
ruff check . --fix
```
<!-- code:end -->

- Style guides for code and whitespace organization

- 700 different rules

---

# Configuring Ruff
## Rule selection and configuration

<!-- code:start -->
```toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "D"]
ignore = ["D203", "D213"]
```
<!-- code:end -->

- Naming

- Pydocstyles

- Pyupgrade

- Flake8 rules

- Rules can be configured to specific styles or ignored to match the needs of your project

- [https://docs.astral.sh/ruff/configuration/](https://docs.astral.sh/ruff/configuration/)

---

# Configuring Ruff in VS Code and Other IDEs
## Enable real-time linting in your editor

- Many IDEs such as **VSCode** or **PyCharm** have built in linters that identify smaller coding errors and improve code formatting

- Possible to install Ruff into **VSCode**

- Linting is run when files are opened or saved

---

# Integrate Ruff and Black with GitHub Pre-Commit Hooks
## Run formatters and linters automatically at commit time

<!-- code:start -->
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.13.0
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
```
<!-- code:end -->

- Linters and formatters such as Ruff and Black can be integrated into Github

- Install pre-commit in conda environment using `pip install pre-commit` or integrate pre-commit dependence in pyproject.toml

- Add a pre-commit config file called .pre-commit-config.yaml to project. Add ruff repo in .yaml.

---

# Run Ruff Locally to Identify Errors
## Install Ruff and run an initial check

- `pip install ruff`

- Once installed, go to folder where repo is located

- Go to src folder

- Type “ruff check .” In command line

---

# Setting Up Pre-Commit
## Install and initialize pre-commit

<!-- code:start -->
```bash
pip install pre-commit
pre-commit sample-config > .pre-commit-config.yaml
```
<!-- code:end -->

- `pip install pre-commit`

- Add dependency in *pyproject.toml* (it should already be added)

- create *.pre-commit-config.yaml* file and add to repo

- In *.pre-commit-config.yaml* file: add the following pre-commit information

---

# Editing `.pre-commit-config.yaml`
## Configure hooks for Ruff (and optionally Black)

<!-- code:start -->
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.13.0
    hooks:
      - id: ruff
      - id: ruff-format
```
<!-- code:end -->

- Add ruff pre-commit to pre-commit.yaml file to include ruff
- Find information for other packages for pre-commits here:
  - [https://pre-commit.com/](https://pre-commit.com/)
  - [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html)
  - Push yaml file to repo on github
---

# Using pre-commit
## Install and run hooks from configuration

<!-- code:start -->
```bash
pre-commit install
pre-commit run --all-files
pre-commit run ruff --all-files
```
<!-- code:end -->

  - pre-commit install
  - This install pre-commit hooks for each upcoming commit
- To run pre-commit hooks on current files, go to specific directory and run
  - Pre-commit run --all-files
- This will identify all errors
  - We can autofix errors by specifying autofix.

---

# Conclusions
## Clean, consistent code improves collaboration

- Code formatters and linters such as ruff can be used to automatically format and detects formatting errors in code
- Linting can be implemented as a precommit hook and can be part of IDEs such as vscode or pycharm
- Clean code will lead to more understandable, reliable, and reproducible code.
---

# Exercise
## Configure local linting and pre-commit checks

- Set up a pre-commit hook to run Ruff and black and install it in pyproject.toml to format calculator codebase.
---

# Further Reading
## Key references for linting and formatting

- Black documentation: https://black.readthedocs.io/en/stable/
- Linting in vscode: https://code.visualstudio.com/docs/python/linting
- Pre-commit documentation: https://pre-commit.com
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
