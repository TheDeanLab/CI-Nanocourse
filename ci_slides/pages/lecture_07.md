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

# What is Clean Code?
## Maintaining Structure as Projects Scale

- Organizing code in Python is crucial for maintainability, scalability, and clarity.

  - **Modularity:** Divide your code into modules and packages, each with a specific responsibility.
  
  - **Naming Conventions:** Use clear and descriptive naming conventions. For example:  `data_source.py`, `file_management.py`, `data_visualization.py`.
  
  - **Code Reusability:** Abstract out common functionalities into utility functions or base classes to avoid repetition and enhance reusability.

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

# Variable Naming (What Actually Matters)
## Make names searchable and unambiguous

- Use **descriptive `snake_case`**: `user_count`, `max_retries`, `temperature_celsius`.

- Prefer **explicit units / types** when helpful: `timeout_seconds`, `dataframe`, `user_id`.

- Constants are **UPPER_SNAKE_CASE**: `MAX_RETRIES`.

- Private/internal: leading underscore: `_cache`.

- Avoid ambiguous abbreviations and built-ins (`list`, `dict`, `id`, `class`).

Examples:
  - ✅ `timeout_seconds = 10`  
  - ❌ `t = 10`

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

# Function Naming (High Impact)
## Verbs + clarity beats cleverness

- Name functions as **verbs** that describe the action: `load_`, `parse_`, `compute_`, `validate_`, `save_`.

- If it returns a boolean, use **`is_` / `has_`**: `is_valid_email()`, `has_permission()`.

- Keep names consistent with your domain: `calculate_total()` not `do_math()`.

- Internal helpers: leading underscore: `_parse_header()`.

Examples:
  - ✅ `def parse_csv(text: str) -> list[str]: ...`
  - ❌ `def parse(text): ...`

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

# Class Naming (High Impact)
## Nouns, PascalCase, and predictable Exceptions

- Use **PascalCase nouns**: `UserRepository`, `ReportBuilder`, `DataProcessor`.

- Exceptions end in **`Error`**: `ConfigError`, `ValidationError`.

- Avoid vague “Manager/Helper/Util” unless it’s truly the best domain name.

Examples:
  - ✅ `class CsvParser:`
  - ❌ `class ParserThing:`

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

```text
MAX_RETRIES = 10  # Maximum number of retries allowed (obvious)

while retries < MAX_RETRIES:
    # Attempt to connect to the database (obvious)
    if connect_to_database():
        break

    # Add 1 to the retry count (obvious).
    retries += 1

```
---

# Documenting Code
## Write clear, structured docstrings:

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
```

---

# Coding Principles
## Don’t Repeat Yourself

- Keep it Simple

- Separation of Concerns

- Split classes into multiple subclasses, inheritances, abstractions, interfaces.

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
```text
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

- **Black:** "Uncompromising and opinionated" PEP 8 compliant code formatter

- **Ruff:** Extremely fast, Rust-based code formatter and linter

<br>

### Ruff can be used to detect unused imports, variables, and style violations

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

```toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "D"]
ignore = ["D203", "D213"]
```

- Rules can be configured to specific styles or ignored to match the needs of your project

---

# Activity: VS Code Setup (Interpreter + Environment)
## Make sure you're running the right Python

- **Goal:** Get VS Code installed and point it at your existing project environment (venv/conda).

- **1) Install VS Code**
  - Download and install: https://code.visualstudio.com/

- **2) Install the Python extension**
  - In VS Code → Extensions → install **Python** (publisher: Microsoft).

- **3) Open your repository folder**
  - File → Open Folder… → select your repo root.

---

# Activity: VS Code Setup (Interpreter + Environment)
## Make sure you're running the right Python

- **4) Select your interpreter (most important step)**
  - Press `Cmd+Shift+P` → **Python: Select Interpreter**
  - Choose the interpreter for your existing environment:
    - `./.venv/bin/python` (common)
    - `./venv/bin/python` (common)
    - or your conda env interpreter

---

# Activity: VS Code Setup (Interpreter + Environment)
## Make sure you're running the right Python

- **5) Verify you're in the right environment**

Open a terminal in VS Code and run:

```bash
python --version
python -m pip --version
python -c "import sys; print(sys.executable)"
```

- **6) (Optional) Save it for the workspace**
  - If prompted, allow VS Code to create/update `.vscode/settings.json` so everyone on your team can be consistent.

---

# Activity: Real-time Ruff Linting (VS Code)
## Get instant feedback while you type

- **Goal:** See Ruff warnings/errors in the editor without running commands.

- **1) Confirm Ruff is available (from Lecture 6)**

```bash
ruff --version
```

- **2) Install the VS Code extension**
  - Extensions → install **Ruff** (publisher: *Astral Software*).

- **3) Confirm VS Code is using your existing interpreter**
  - `Cmd+Shift+P` → **Python: Select Interpreter** → pick your venv/conda env.


---

# Activity: Real-time Ruff Linting (VS Code)
## Get instant feedback while you type

- **4) Verify linting is live**
  - Create a file like `src/<package_name>/scratch.py`:

```text
import os


def hello(name):
    return "hi, " + name


print(hello("world"))
```

  - You should see Ruff flag at least:
    - unused import (`os`)
    - missing type hints (depending on your Ruff config)
    - formatting suggestions


---

# Activity: Real-time Ruff Linting (VS Code)
## Get instant feedback while you type

- **5) Optional: quick auto-fixes**
  - Try: `Cmd+Shift+P` → **Ruff: Fix all auto-fixable problems**.

---

# Activity: Manual Clean-Code Refactor (Pairs)
## Make unclear code readable (behavior must not change)

- **Goal:** 
  - Refactor this function for readability *without changing outputs*.

- **Rules:**
  - Improve names, spacing, and structure.
  - Add type hints + a short docstring.
  - Keep behavior identical (same return values for the same inputs).

- **Hint:**
  - It parses a comma-separated string into a cleaned list of **unique** tokens,
    optionally lowercases them, optionally limits how many are kept, and joins with `|`.

---

# Activity: Manual Clean-Code Refactor (Pairs)
## Make unclear code readable (behavior must not change)


### Before (intentionally ugly)

```python
def p(s,n=0,f=False):
  if s==None or s=="":return ""  # empty
  t=s.split(",");o=[];i=0
  for x in t:
    x=x.strip()
    if x=="":continue
    if f:x=x.lower()
    if len(x)<2:continue
    if x in o:continue
    o.append(x);i+=1
    if n and i>=n:break
  return "|".join(o)

# Examples (use to confirm you didn't change behavior)
# p(" A, Bee, bee, ,  C ")            -> "A|Bee|bee|C"
# p(" A, Bee, bee, ,  C ", f=True)    -> "a|bee|c"
# p("A,B,C", n=2)                     -> "A|B"
```
