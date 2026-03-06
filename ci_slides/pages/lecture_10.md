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
- `toctree` is usually placed in `index.rst` and defines the page hierarchy for your docs.

```rst
.. toctree::
  :maxdepth: 2
  :caption: Contents:

  getting_started
  installation
  api
```

- Each listed page becomes part of the generated navigation.
- Indentation matters: the child pages must be aligned under the directive.

---

# Autosummary helps us with the API documentation
## Automatically generate API reference stubs

<img src="/images/lecture-09/t22_from_s24-25.png" alt="Autosummary-generated API documentation example">
https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

---

# Turning docstrings into API pages
## Use Sphinx extensions before you worry about templates

- For a beginner docs site, **extensions matter more than Jinja templates**.
- A practical starting point in `conf.py` is:

```text
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]
```

- `autodoc`: pulls docstrings from your Python code.
- `autosummary`: creates stub API pages automatically.
- `napoleon`: understands Google-style and NumPy-style docstrings.

- Get the basic docs site working first; template customization can come later.

---

# Activity: Hands-on documentation practice
## Add new pages and link them in the `toctree`


- **1) Create two new pages** in `docs/source/`:
  - `installation.rst`
  - `quickstart.rst`

- **2) Add a title + a few lines of content** to each file.
  - Example title pattern:

```rst
Installation
============

Describe how to install your package here.
```

---

# Activity: Hands-on documentation practice
## Add new pages and link them in the `toctree`

- **3) Edit `docs/source/index.rst`** and add the new pages to the `toctree`:

```rst
.. toctree::
  :maxdepth: 2
  :caption: Contents:

  installation
  quickstart
```

- **Stretch goal:** also create `api.rst` and add it to the same `toctree`.

---

# Activity: Build and verify your new docs pages
## Make sure the pages appear in the generated site

- **4) Rebuild the docs** from the `docs/` folder:

```bash
cd docs
make html
```

- **5) Open the generated homepage**:

```bash
open _build/html/index.html
```

- **6) Check your work**
  - `installation` and `quickstart` appear in the sidebar/navigation.
  - Clicking them opens the pages you created.
  - The docs build finishes without errors.

---

# Activity: Hands-on documentation practice
## Add new pages and link them in the `toctree`

- **Definition of Done**
  - `docs/source/installation.rst` exists
  - `docs/source/quickstart.rst` exists
  - `docs/source/index.rst` links them in the `toctree`
  - `make html` succeeds

---

# Publishing documentation with GitHub Pages
## Publish compiled documentation automatically

- Ideally, we do this automatically, updating whenever new documentation is written.
- GitHub actions lets you do this easily with GitHub Pages.
- [https://pages.github.com/](https://pages.github.com/)
- Hosts websites directly out of a GitHub repository
---

# Activity: Automatically publish docs with GitHub
## A Docs workflow outline

- **1) Make sure your docs build locally first**
  - From the repo root, confirm this works:

    ```bash
    cd docs
    make html
    ```

- **2) Create the workflow file**
  - Create: `.github/workflows/docs.yml`

---

# Activity: Automatically publish docs with GitHub
## A Docs workflow outline

- **3) Add the workflow trigger**
  - Run it on pushes to your main branch (or `develop` if that’s your default docs branch).

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
```

- **4) Add the build job**
  - Your workflow should:
    - check out the repo
    - set up Python
    - install docs dependencies from `pyproject.toml`
    - build the docs with `make html`

---

# Activity: Automatically publish docs with GitHub
## A Docs workflow outline

- **5) Add the deploy steps for GitHub Pages**
  - Use the official GitHub Pages actions:
    - `actions/configure-pages`
    - `actions/upload-pages-artifact`
    - `actions/deploy-pages`

- **6) Upload the built HTML folder**
  - The artifact path should be:

```text
docs/_build/html
```

---
layout: two-cols-header
---

# Activity: Publish docs with GitHub Pages
## Commit, enable Pages, and verify the site

- **7) Minimal workflow outline**

::left:: 

```yaml
name: Build and deploy docs

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
```

::right::

```yaml
          
      - run: python -m pip install -e ".[docs]"
      - run: make html
        working-directory: docs
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/_build/html

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/deploy-pages@v4
```

---

# Activity: Publish docs with GitHub Pages
## Commit, enable Pages, and verify the site

- **8) Commit and push the workflow**

```bash
git add .github/workflows/docs.yml
git commit -m "Add docs build and deploy workflow"
git push
```

- **9) Enable GitHub Pages in repository settings**
  - Go to **Settings → Pages**
  - Set **Source** to **GitHub Actions**

- **10) Verify it worked**
  - Open the **Actions** tab and watch the workflow run.
  - When it finishes, open the Pages URL and confirm your docs site loads.

---

# Activity: Publish docs with GitHub Pages
## Commit, enable Pages, and verify the site

- **Definition of Done**
  - `.github/workflows/docs.yml` exists
  - the workflow run is green ✅
  - your docs site is live on GitHub Pages
