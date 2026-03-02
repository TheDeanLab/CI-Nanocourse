# Setting up a CI/CD Pipeline in GitHub Actions
## Introduction to Python Software Development on GitHub 2023

- Lyda Hill Department of Bioinformatics
- UT Southwestern Medical Center
- [https://www.eslflashcards.com/set/action-flashcards-set-a/](https://www.eslflashcards.com/set/action-flashcards-set-a/)
---

# GitHub Actions Dashboard
---

# GitHub Actions Workflow Example
---

# Let’s create a GitHub workflow
## You can follow along at https://docs.github.com/en/actions/quickstart
---

# Where does the workflow file go?
## They are stored in your Git repository, under .github/workflows

- Create the .github folder
- Create the .github/workflows folder
- Create github-actions-demo.yml
---

# github-actions-demo.yml

- [https://docs.github.com/en/actions/quickstart](https://docs.github.com/en/actions/quickstart)
---

# What are these two lines doing??
---

# `What is ${{ }}?`
## It’s an expression (see https://docs.github.com/en/actions/learn-github-actions/expressions)

- Expressions evaluate what’s inside them
- `${{ github.actor }} evaluates to octocat in the example`
- `${{ github.actor == ”octocat” }} evaluates to true`
---

# What does               do?
## It triggers the jobs under jobs when code is git pushed to the repository

- There are other events. For example,this will trigger a job
  - on a git push to the main branch
  - when a Pull Request is opened
  - if we hit ”Run workflow” in the Actionsdashboard
---

# Defining the jobs
## What is jobs?
---

# Defining the jobs
## What is jobs? The key that holds all the jobs that run in the workflow file.

- What is Explore-GitHub-Actions?
- What is Explore-GitHub-Actions? The name of a job.
- What does runs-on: ubuntu-latest mean?
- What does runs-on: ubuntu-latest mean? This workflow will run on an Ubuntu Linux virtual machine.
- What are steps?
- What are steps? The key that holds all of the steps to run in this job.
---

# The full Explore-GitHub-Actions job
---

# How can we establish a useful set of steps?
## We can copy commands that work locally into run: operations

- We can find common actions on the GitHub Marketplace: https://github.com/marketplace?type=actions
---

# GitHub Marketplace
---

# Search for Codecov
---

# Click “Use latest version”
---

# Copy the action as a step in your job
---

# There’s an action for everything
---

# Exercise: Add a workflow to automatically run unit tests on git push to your repository
## Use pytest

- Can you test on multiple versions of Python? Can you test on windows-latest and macos-latest?
- Hint hint: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
