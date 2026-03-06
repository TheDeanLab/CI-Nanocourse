---
layout: center
class: text-center
---

# Lecture 10
## Public-Facing Documentation
---

# Why do we care about documentation?
## Supports users, collaborators, and future maintenance

- It helps other people use our software.
- It helps other people contribute to our software.
- It helps us write better software.

## Requirements, architecture, API, and end-user docs

- Architecture – How do the pieces of the software fit together?
- Technical – How does each function work? Application programming interface (API) docs.
- End user – Getting started guides. How-tos.

---

# Documentation languages
## Markdown and reStructuredText

**Markdown (.md).** This is the most common documentation language.

```markdown
# Markdown example
This is a **bold** word and this is an *italic* word.

## Links and lists:
- [Google](https://www.google.com)
- [GitHub](https://www.github.com)

```

**reStructuredText (.rst).** Commonly used for Python docstrings and Sphinx documentation.


```rst
reStructuredText example
========================

This is a **bold** word and this is an *italic* word.
Links and lists:
- `Google <https://www.google.com>`_
- `GitHub <https://www.github.com>`_

```


# GitHub uses Markdown
## READMEs, issues, and PRs render Markdown by default
---

# Activity: Write a README.md
## Essential sections for an effective README

  - A brief description of the project
  - Installation instructions
  - Links to further documentation, including how to contribute
  - How to cite the repository, if applicable
  - Badges, if applicable

GitHub will display README.md by default on the home page of your repo

---

# Docstring style examples
## Google-style docstrings with reStructuredText


<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-09/t11_from_s11.png" alt="lecture-01 slide 13 image 1" class="max-h-80 w-auto object-contain rounded shadow" />
</div>


---

# Docstring style examples (NumPy)
## NumPy-style docstrings
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-09/t12_from_s12.png" alt="lecture-01 slide 13 image 1" class="max-h-80 w-auto object-contain rounded shadow" />
</div>

---

# Documentation Frameworks
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

# Sphinx Documentation Framework
## Generate API and narrative documentation from source

- [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/)
- Compiles Python docstrings and reStructuredText files to PDFs, HTML
- Can be modified to use Markdown: https://www.sphinx-doc.org/en/master/usage/markdown.html
---

# Docstrings compiled to HTML by Sphinx
## Sphinx compiles docstrings and reStructuredText to HTML

<br>
<img src="/images/lecture-09/t15_from_s15-16.png" alt="Sphinx-generated HTML documentation example">

---

# Activity: Set up your `docs/` folder
## Install docs dependencies and initialize Sphinx

- **1) Install the optional `docs` dependencies** from `pyproject.toml`:

```bash
python -m pip install -e ".[docs]"
```

- **2) From your repository root, initialize Sphinx**:

```bash
sphinx-quickstart docs
```

- **3) Accept the defaults** (or set your project name/author if prompted).

- **By the end of this step, you should have:**
  - a new `docs/` folder
  - `docs/source/conf.py`
  - `docs/source/index.rst`
  - a Makefile / build helper files

---

# Activity: Build and inspect the HTML docs
## Confirm your Sphinx project actually works

- **4) Build the HTML output**:

```bash
cd docs
make html
```

- **5) Open the generated site** in your browser:

```bash
open _build/html/index.html
```

- **Success check:**
  - the build finishes without errors
  - `_build/html/` now exists
  - `index.html` opens in your browser

- If the build fails, read the first error carefully—usually it’s a missing package or a syntax problem in `index.rst` or `conf.py`.

---

# How `toctree` Defines Site Navigation
## Control site navigation with the `toctree`

- It is empty by default
- You can add documents by listing them in three

---

# Autosummary helps us with the API documentation
## Automatically generate API reference stubs

<img src="/images/lecture-09/t22_from_s24-25.png">
https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

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

---

#  Unit Tests
#### How Do We Know This Function Works?

```text
 def square(x):
     """Return the square of a number."""
     return x * x
 ```
 
 #### You Write Tests
```text
 def test_square():
     """Ensure the square function works correctly."""
     assert square(2) == 4
     assert square(-3) == 9
     assert square(0) == 0
```

