# Public-facing documentation
## Introduction to Python Software Development on GitHub 2023

- Lyda Hill Department of Bioinformatics
- UT Southwestern Medical Center
---

# Why do we care about documentation?
## It helps us remember how and why we built our software.

- It helps other people use our software.
- It helps other people contribute to our software.
- It helps us write better software.
- [https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
---

# Types of documentation
## Requirements – What does the software do? High level.

- Architecture – How do the pieces of the software fit together?
- Technical – How does each function work? Application programming interface (API) docs.
- End user – Getting started guides. How-tos.
---

# Software licenses are an important part of documentation, and should be chosen based on what you want to do with your software

- [https://choosealicense.com/](https://choosealicense.com/)
---

# GPLv3 is the premier copyleft license, but if you want to license your code to a company, you are better off with an MIT license
---

# Companies may enforce use of their own preferred licenses

- UT Southwestern’s open-source software license is here: https://www.utsouthwestern.edu/about-us/administrative-offices/technology-development/agreements/open-source-release-of-software.html
- You MUST use this license if you develop software on any UTSW machine or for any UTSW purpose.
- UNLESS you are using code from a GPLv3-licensed software, in which case I think you should use a GPLv3 license, but you should confirm this with a UTSW lawyer.
---

# Documentation languages
## Hypertext markup language (HTML) (.html)

- Markdown (.md)
- reStructuredText (.rst)
- Many more: https://en.wikipedia.org/wiki/List_of_document_markup_languages
---

# Documentation languages are simple languages, close to standard word processing

- [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)
- [https://sphinx-tutorial.readthedocs.io/cheatsheet/](https://sphinx-tutorial.readthedocs.io/cheatsheet/)
---

# GitHub uses Markdown
---

# Exercise: Write a README.md
## README.md files serve as an entry point to your entire code base. They should include

  - A brief description of the project
  - Installation instructions
  - Links to further documentation, including how to contribute
  - How to cite the repository, if applicable
  - Badges, if applicable
  - See https://github.com/mwaskom/seaborn/blob/master/README.md for a good example
- GitHub will display README.md by default on the home page of your repo
---

# Python docstrings can be written in a variety of documentation languages, including reStructuredText
## reStructuredText

- Google style
---

# Python docstrings can be written in a variety of documentation languages, including reStructuredText
## NumPy style
---

# Documentation frameworks
## Automate documentation of code

- Import the code to generate documentation based on runtime inspection
- Parse and analyze the code statically (without running it)
- Compile documentation languages to PDFs, HTML, etc.
- [https://wiki.python.org/moin/DocumentationTools](https://wiki.python.org/moin/DocumentationTools)
---

# is the primary documentation framework for Python

- [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/)
- Compiles Python docstrings and reStructuredText files to PDFs, HTML
- Can be modified to use Markdown: https://www.sphinx-doc.org/en/master/usage/markdown.html
---

# An example of a docstring compiled to HTML by Sphinx
---

# Let’s build some documentation for our program
## Follow along at https://www.sphinx-doc.org/en/master/usage/quickstart.html
---

# First, make sure we have the right dependencies
## Does anyone know how to install the right sphinx dependencies for documentation?

- pip install –e .[docs] from within your repository folder(pip install –e ‘.[docs]’ on a Mac)
- This installs the optional dependencies listed under docs in pyproject.toml
---

# Let’s generate a source folder
## Create a docs/ folder in your repo.

- Run sphinx-quickstart in this folder.
---

# Directory structure of documentation folder
---

# Now try make html in the docs folder
## There’s a web page! But nothing on it.
---

# The toctree defines what we see
## toctree stands for Table of Contents Tree

- It is empty by default
- You can add documents by listing them in three
---

# Autosummary helps us with the API documentation

- [https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
---

# Templating
## Sphinx uses Jinja templates (https://jinja.palletsprojects.com/)

- These allow us to change the way data is presented on different pages
- For example, the autosummary module template is located at
---

# Templates enable us to produce a more comprehensive autosummary
## custom_module.rst: https://github.com/sphinx-doc/sphinx/issues/7912#issue-650871700
---

# Templates enable us to produce a more comprehensive autosummary
---

# Exercises

- Write installation.rst and/or quickstart.rst. Compile the new docs to HTML. Verify the compilation worked by opening the docs in your web browser.
- What happens if you change api.rst to the following? Why?
---

# Public-facing documentation
## We want to put our compiled HTML files on the internet.

- Ideally, we do this automatically, updating whenever new documentation is written.
- GitHub actions lets you do this easily with GitHub Pages.
---

# GitHub Pages

- [https://pages.github.com/](https://pages.github.com/)
- Hosts websites directly out of a GitHub repository
---

# Exercise: Create a GitHub workflow that builds your docs and deploys it to a GitHub page

- Hint: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
