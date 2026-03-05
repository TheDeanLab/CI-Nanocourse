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

# Fixtures in Pytest: Example in PyCalc
## Using shared setup in `conftest.py`

<img
  src="/images/lecture-07/t12_from_s13.png"
  style="max-width: 100%; max-height: 65vh; display: block; margin: 1rem auto; object-fit: contain;"
/>


---
layout: image-right
image: /images/lecture-07/t13_from_s14.png
backgroundSize: contain
---

# Key Binding Test in PyCalc Exercise
## Shared test fixtures and setup

- `test_controller.py`
- Fixtures `conftest.py`
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

# Final Activity: Write a function + a unit test
## Mirror `src/` in `tests/`, then run `pytest`

- **Goal:** Practice the full loop: implement → test → run.

- **1) Create a small function in `src/`**
  - Create `src/<package_name>/math_utils.py`:

```python
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b
```

```text
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b
```

- **2) Mirror the path in `tests/` and write a test**
  - Create `tests/<package_name>/test_math_utils.py`:

```text
from <package_name>.math_utils import add


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

- **3) Run the tests**

```bash
pytest -q
```

- **4) Stretch goals**
  - Add a parameterized version of the test with `@pytest.mark.parametrize`.
  - Add a failing case intentionally, see it fail, then fix it.

---
