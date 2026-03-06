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
src: ./pages/lecture_08.md
---

---
src: ./pages/lecture_09.md
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


