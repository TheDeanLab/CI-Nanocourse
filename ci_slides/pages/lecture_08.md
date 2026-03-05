---
layout: center
class: text-center
---

# Lecture 8
## Unit Testing and Test Driven Development

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
layout: image-right
image: /images/lecture-07/t07_from_s07.png
backgroundSize: contain
---

# Writing a Unit Test
## Arrange, Act, Assert, and Cleanup

- Act: action that we would like to test, function or process.
- Assert: checking the result state to see if it matches expectations. Look at output and make judgment
- Cleanup: cleanup tests so other downstream tests aren’t influenced by results or attributes.

---


# Activity: 
## Install `pytest` via optional dependencies

- **1) Edit `pyproject.toml`**
  - Add (or extend) an optional dependency group:

```toml
[project.optional-dependencies]
tests = [
  "pytest",
]
```

- **2) Install the test extras**

```bash
python -m pip install -e ".[tests]"
```

- **3) Verify install**
```bash
pytest --version
```

*Tip: Many projects use `dev` instead of `tests` and include linters + testing tools together. Either is fine—be consistent.*

---

# Pytest Test Discovery
## Pytest discovers functions prefixed with `test_`

<img
  src="/images/lecture-07/t09_from_s09.png"
  style="max-width: 100%; max-height: 65vh; display: block; margin: 1rem auto; object-fit: contain;"
/>
- Pytest finds tests automatically—no registration step required. By default, finds: 
  - files named `test_*.py` or `*_test.py`
  - functions named `test_*`
  - classes named `Test*` (don’t define `__init__`)
- Put tests in a `tests/` directory so it’s clear what’s production code vs test code.
- Run a single test fast while debugging: `pytest -q tests/test_file.py::test_name`

---

# Test Parameterization
## Test multiple cases with `pytest.mark.parametrize`

<img
  src="/images/lecture-07/t10_from_s10.png"
  style="max-width: 100%; max-height: 65vh; display: block; margin: 1rem auto; object-fit: contain;"
/>

- Parameterization lets you test many input/output cases with **one** test function.

- Keeps tests DRY: same logic, different examples (edge cases are easy to add).

- When a case fails, pytest reports **which parameter set** failed.

- Example pattern:
  - `@pytest.mark.parametrize("x, expected", [(2, 4), (-3, 9), (0, 0)])`

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

# Fixtures in Pytest
## Using shared setup in `conftest.py`

- `conftest.py` is a special pytest file where you define **shared fixtures** for a folder (and its subfolders).
- Tests can use fixtures by **naming them as function arguments** (pytest injects them automatically).
- Use fixtures for: common objects, temp files/dirs, test data, or expensive setup.
- Keep fixtures small and focused—one responsibility each.

Example structure:

```text
tests/
  conftest.py
  test_math_utils.py
```


---

# Fixtures in Pytest
## Using shared setup in `conftest.py`

`tests/conftest.py`:
```text
import pytest


@pytest.fixture
def sample_numbers() -> tuple[int, int]:
    return (2, 3)
```

`tests/test_math_utils.py`:
```text
def test_add_uses_fixture(sample_numbers):
    a, b = sample_numbers
    assert a + b == 5
```

***Tip:** You don’t import fixtures into tests—pytest discovers them automatically from `conftest.py`.*

---

# Activity: Build a tiny test suite
## Add `src/` code + `tests/` with a fixture, then run `pytest`

- **Goal:** Build a clean, repeatable testing setup you can reuse in any repo.

- **1) Create a tiny module (production code)**
  - Create `src/<package_name>/stats.py`:

```text
def mean(values: list[float]) -> float:
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
```

- **2) Set up the tests folder (mirrors `src/`)**
  - Create this structure:

```text
tests/
  conftest.py
  <package_name>/
    test_stats.py
```

---

# Activity: Build a tiny test suite
## Add `src/` code + `tests/` with a fixture, then run `pytest`

- **3) Write a fixture in `tests/conftest.py`**

```text
import pytest

@pytest.fixture
def sample_values() -> list[float]:
    return [1.0, 2.0, 3.0]
```

- **4) Write tests that use the fixture**
  - Create `tests/<package_name>/test_stats.py`:

```text
import pytest
from <package_name>.stats import mean

def test_mean_happy_path(sample_values):
    assert mean(sample_values) == 2.0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])
```

---

# Activity: Build a tiny test suite
## Add `src/` code + `tests/` with a fixture, then run `pytest`

- **5) Run pytest and interpret results**

```bash
pytest -q
pytest -q -x
pytest -q -k mean
```

- **Stretch goals**
  - Parameterize `test_mean_happy_path` with 3 datasets.
  - Add one intentionally failing assertion, see the failure output, then fix it.

***Definition of done:** your repo has `src/…`, `tests/…`, a fixture in `conftest.py`, and `pytest -q` passes.*
