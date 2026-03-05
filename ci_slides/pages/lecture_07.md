---
layout: center
class: text-center
---

# Lecture 7
## Code Quality

---

# What is Clean Code?
## Readable, maintainable code is easier to review and evolve

- Consistent formatting. Should follow PEP 8 standards for Python.

- Meaningful names - descriptive variable, function, and class names.

- Functions and classes should do one thing only, and do it well.

- Well-documented.

- Type-hinted.

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