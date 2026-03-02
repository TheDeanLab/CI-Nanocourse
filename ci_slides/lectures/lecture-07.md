# Unit Testing and Test Driven Development

- Conor McFadden
- Continuous Integration with Python Nanocourse 2023
---

# Unit Testing overview
## Importance of unit testing in software development.

- Writing effective unit tests using python's testing frameworks.
- Incorporating test-driven development principles
---

# Software Review Overview
## Verification: Formal proof that a program is correct.

- Tedious to do by hand, and automated tool support for verification is 	still an active area of research.
- Code review: Having somebody else carefully read your code, and reason informally about it, can be a good way to uncover bugs. It’s much like having somebody else proofread an essay you have written.
- Testing: Running the program on carefully selected inputs and checking the results.
- User Inputs? Logic errors? Hardware bugs?
---

# Types of Tests
## Unit Test: Isolated method, function or component.

- Integration Test: Combined Unit Tests tested as a group.
- System (Smoke) Testing: Tests the entire system as a whole to verify that critical functionalities work.
---

# Python Testing Frameworks

- unittest: A testing framework included in the Python standard library. It provides a basic set of tools for writing and executing tests.
- pytest: A popular and powerful third-party testing framework. It encourages test-driven development (TDD) and provides features like fixtures and parameterized testing.
- doctest: A testing framework that allows you to embed tests within docstrings, making it useful for creating documentation that also serves as executable test cases.
---

# Writing a Unit Test
## Arrange: prepare for test, preparing objects, starting or killing services, entering records.

- Act: action that we would like to test, function or process.
- Assert: checking the result state to see if it matches expectations. Look at output and make judgment
- Cleanup: cleanup tests so other downstream tests aren’t influenced by results or attributes.
---

# Running pytest
## Just type >> pytest in prompt

- Assert is True, the test passes!
---

# Running pytest
## Assert is False, the test fails!
---

# Any “test_” function will be recognized by pytest automatically
---

# Parameterization in tests
## Test multiple parameters at once using pytest parameterize
---

# Fixtures in pytest
## A way to set up and clean up things before and after running tests.

- They help avoid repeating setup code in multiple tests.
- Why Use Fixtures?
- Avoid duplicating setup code in every test.
- Keep test files clean and readable.
- Automatically clean up after tests run.
---

# Fixtures in pytest
---

# Key Binding Test in PyCalc Exercise
## conftest.py

- test_controller.py
- Fixtures  conftest.py
- Yield keyword to free resources after test.
---

# What is yield doing?
## SETUP: prepare resources

- YIELD: give it to your tests
- TEARDOWN: free your resources
---

# Unit Testing Best Practices
## Unit test cases should be independent.

- Test only one code or component at a time.
- Clear and consistent naming conventions.
- Fix bugs before moving on!
- “Test as you code”  Write you tests while the idea is still fresh.
---

# Testing-Driven Development/Deployment
---

# Conclusions

- Writing tests are useful for making sure code is functioning properly and removing bugs during development
- Pytest is a useful framework for setting up tests
---

# Exercise
## Install pytest in environment using pyproject.toml

- pip install –e .[dev] or pip install –e “.[dev]” on Mac
- Write a unit test to test _calculateResult function in controller.py
- If time is remaining, parameterize the test for _calculateResult
