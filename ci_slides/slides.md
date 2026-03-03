---
layout: center
class: text-center
---

# Introduction to Collaborative Software Development
## Course Overview and Learning Objectives
---

# Course Structure
## Day 1

- Introduction to Collaborative Software Development
- Environment Management & Git Essentials
- Organizational Strategies, and Collaborative Development Workflows
- Pre-Commit Hooks, Linters, Code Formatters


## Day 2

- Unit Testing and Test-Driven Development (TDD)
- Setting up Continuous Integration Pipelines on GitHub
- Public-Facing Documentation
---

# Expectations
## Coding with Python

- Mandatory
  - How to work with Python Data Structures (dictionaries, lists, tuples, etc.)…
  - Python Control Flow (for, while, if, else, elif, break, continue)…
- Recommended
  - Object Oriented Programming (classes, objects, inheritance)…
- Bonus
  - Parallel Processing with Python (multi-threading, multi-processing)…
---

# Goals
## Building a Foundation

- Establish your own Repository with CI, Documentation, etc.
- Maintain stable, clean code.
- Work collaboratively on software development.
- Be able to contribute to an Open-Source Project.
---

---
layout: center
class: text-center
---

# Lecture 1
## Introduction to GIT

---

# The Importance of Collaboration
## Why Collaboration Improves Software Quality

- **Diverse Skill Sets:** No single developer possesses expertise in every aspect of software development. Collaborative efforts ensure that a team with varied skills can address different facets of a project, from front-end design to back-end logic, ensuring comprehensive development.

- **Accelerated Problem-Solving:** Challenges are inevitable in software development. A collaborative team can brainstorm, debate, and ideate solutions faster than an individual. This collective problem-solving often leads to more innovative and efficient solutions.

- **Continuous Feedback Loop:** Collaboration fosters a culture of continuous feedback. Regular code reviews, paired programming, and open discussions ensure that errors are caught early, and best practices are consistently upheld.

---

# The Importance of Collaboration
## Why Collaboration Improves Software Quality

- **Shared Responsibility:** A collaborative environment distributes the responsibility of the project. This not only reduces the pressure on individual team members but also ensures accountability and commitment towards the project's success.

- **Adaptability & Flexibility:** In a collaborative setting, teams are better equipped to adapt to changes, be it in project requirements, technologies, or methodologies. The collective knowledge ensures a smoother transition and quicker adaptation.

- **Knowledge Transfer & Skill Enhancement:** Collaboration is a learning experience. Developers can share knowledge, introduce peers to new tools or methodologies, and elevate the overall skill set of the team.

---

# Overview of Version Control Systems (VCS)
## Git, Subversion, etc.

- **What is VCS?**
  - A tool that tracks changes in files, often used in codebases.

- **Significance of VCS:**
  - *History:* Records every modification, allowing rollbacks.
  - *Collaboration:* Enables multiple developers to work simultaneously.
  - *Accountability:* Tracks who made what change and when.
  - *Backup:* Safeguards code against accidental deletions or errors.
  - *Branching:* Allows development of features in isolation.

- VCS is foundational for collaborative, error-free, and efficient software development.

---

# An Introduction to Git
## Role in Team-Based Development

- **What is Git?**

  - A distributed version control system widely used in software development.

  - Enables software to be developed locally (on a developer's machine) or remote (on a server or hosted platforms like GitHub), facilitating collaboration and version control for projects of any size.

  - Provides control over contributors to code.

---

# An Introduction to Git
## Installing Git

- Visit the official Git website at [git-scm.com](https://git-scm.com/)

- **Windows**
  - Download the latest version for Windows
  - Run the downloaded .exe file and follow the installation prompts with default settings.

- **macOS**
  - Installed by default with Xcode. Otherwise, requires Homebrew or MacPorts.

- **Linux**
  - Installed using Linux distribution package manager. If on BioHPC, available as a module: <br>`module load git/v2.5.3`

---

# Basic Git Commands and Workflows
## Core Concepts and Everyday Commands

- **Repository**: Often abbreviated as "repo", is a storage location where all the files and revision history of a project reside.

- It acts as the central hub for a project's codebase, allowing developers to clone, pull, and push changes to and from it.

- A repository contains the information that Git uses to track the progression of a project.

---

# Basic Git Commands and Workflows
## Cloning a Repo


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-01/s13_img01.png" alt="lecture-01 slide 13 image 1" class="max-h-40 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-01/s13_img02.png" alt="lecture-01 slide 13 image 2" class="max-h-40 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- **Cloning:** Downloads a repository onto your machine locally with all necessary information for tracking code development.

- `git clone` --> Clones a repository into a newly created directory, and creates remote-tracking branches for each branch in the cloned repository.

- [https://git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone)

---

# Basic Git Commands and Workflows
## Isolating Development


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-01/s14_img01.png" alt="lecture-01 slide 14 image 1" class="max-h-40 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- **Branch:** Lightweight movable pointer that points to a specific commit.

- It represents an independent line of development, allowing you to isolate work on different features, bug fixes, or experiments without affecting the main or other branches.

- *Parallel development*: multiple features or fixes can be developed simultaneously in isolation.

- **Main Branch:** By default, every Git repository starts with a branch called "master" or, more recently, "main". This is the primary branch where stable, production-ready code resides.

---

# Basic Git Commands and Workflows
## Creating and Managing Branches: `branch`

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-01/s16_img02.png" alt="lecture-01 slide 16 image 2" class="max-h-40 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-01/s16_img01.png" alt="lecture-01 slide 16 image 1" class="max-h-40 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- **Creating a new branch** does not create a new copy of the repository. Instead, it's a lightweight pointer to a commit. This makes branching in Git very fast and efficient.

- `git branch` --> List, create, or delete branches.

- Read the docs! [https://git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch)

---

# Basic Git Commands and Workflows
## Switching to a Branch: `checkout`


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-01/s17_img02.png" alt="lecture-01 slide 17 image 2" class="max-h-40 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-01/s17_img01.png" alt="lecture-01 slide 17 image 1" class="max-h-40 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- You can easily **switch** between branches using the git checkout command.

- `git checkout` --> Switch branches. (or `git switch` in newer versions of Git)

- [https://git-scm.com/docs/git-checkout](https://git-scm.com/docs/git-checkout)

---

# Basic Git Commands and Workflows
## Merging a Branch: `merge`


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-01/s18_img01.png" alt="lecture-01 slide 18 image 1" class="max-h-30 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-01/s18_img02.png" alt="lecture-01 slide 18 image 2" class="max-h-30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- Once work on a branch is complete, it can be **merged** back into another branch, usually the main branch. This integrates the changes made in the branch into the main line of development.

- `git merge` --> Join two or more development histories together.

- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)

---

# Basic Git Commands and Workflows
## Challenges with Git

- **Complex Commands:** Git's command-line interface can be intimidating, especially for beginners. Remembering and correctly executing multiple commands can lead to errors.

- **Merge Conflicts:** Resolving conflicts when multiple developers make changes to the same section of code can be tedious and confusing.

- **Visualizing History:** The command-line doesn't provide an intuitive way to visualize the commit history, branches, and their relationships.

- **Staging Changes:** Deciding what changes to stage for a commit can be cumbersome, especially in large codebases.

- **Switching Context:** Frequent switching between branches and keeping track of which branch you're on can be error-prone.

---
layout: image-right
image: /images/lecture-01/s20_img01.png
backgroundSize: contain
---

# Basic Git Commands and Workflows
## Using GitHub Desktop for Beginner-Friendly Workflows


- GUI is easier for Git beginners.

- Visual history and branch view.

- Click-based merge conflict support.

- Simple staging and commit workflow.

- **[https://desktop.github.com/](https://desktop.github.com/)**

---

# Basic Git Workflows
## Activity #1

- Install Git

- Create a GitHub account

- Download GitHub Desktop

- Clone the class repo: **https://github.com/TheDeanLab/CI-Nanocourse**

- *Using Git command-line:* create a branch, and switch between main and the branch you created.

- Do the same with *GitHub Desktop*

---
layout: center
class: text-center
---

# Lecture 2
## Environment Management

---

# Environment Management with Anaconda
## Creating Reproducible Development Environments


- An **environment** is like a sandbox or petri dish, ensuring that the software setup for one project doesn't interfere with another and providing a stable and reproducible development space.

- **Version Inconsistencies:** Python libraries and tools are constantly evolving. Different projects might require different versions of the same library, leading to potential conflicts and unexpected behavior.

- **System-wide Installation Risks:** Installing libraries system-wide can lead to "dependency hell", where upgrades for one project break another.

- **Reproducibility:** For scientific computing and data analysis it's crucial to reproduce results. Consistent environment setups ensure that peers can reproduce your published results regardless of their machine.

- **Ease of Sharing:** With a well-managed environment, developers can easily share their projects, ensuring that others can run their code without stumbling upon missing dependencies or version issues.

- **Isolation:** Keeping project environments separate ensures that specific dependencies or version requirements of one project don't interfere with another, leading to cleaner and more stable development.

---

# Environment Management with Anaconda
## *Mini*conda vs *Ana*conda
<br><br>
|              | **Anaconda** | **Miniconda** |
| ------------ | ------------ | ------------- |
| **Content:** | 1500 packages: scientific computing, data science, machine learning | Just `conda` + essentials |
| **Pros:** | Complete, out-of-the-box solution. | Lightweight and flexible. |
| **Cons:** | Heavy disk space load. Superfluous. | Manual installation. |
<br>
- Let's use ***Miniconda*** --> Less bloated, install just what we need.

---

# Advanced Environment Management
## Activity #2
<br><br>
- Install **[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)**!

---
layout: image-right
image: /images/lecture-02/s07_img01.png
backgroundSize: contain
---

# Environment Management with Anaconda
## Activating Your New Environment


- List all Environments: <br>`conda env list`

- Create new environment: <br>`conda create -n my_env python=3.9.7`

- Activate an Environment: <br>`conda activate my_env`

- List Environment Packages: <br>`conda list`

---

# Advanced Environment Management
## Activity #3

- Create an Anaconda environment named `ci_nanocourse` with Python 3.9.7 or newer.

- Activate the environment, list its installed packages.

- Launch python, and run a basic print statement.

---

# Environment Management with Anaconda
## What is a Package?

- **Software Collection:** A package in Anaconda is a bundled collection of software tools, libraries, and dependencies that function together to achieve a specific task or set of tasks.

- **Version Management:** Each package has specific versioning, allowing users to install, update, or rollback to particular versions as needed, ensuring compatibility and stability in projects.

- **Dependency Handling:** When a package is installed in Anaconda, the system automatically manages and installs any required dependencies, ensuring seamless functionality and reducing manual setup efforts.

---
layout: image-right
image: /images/lecture-02/s10_img01.png
backgroundSize: contain
---

# Environment Management with Anaconda
## Creating an Environment from a Text File


- Each package, and all of its dependencies, explicitly imported from a package manager (pip, conda, etc.)

- Version Control (e.g. `pyserial==3.5`)

- Platform Control (e.g. `sys_platform == “darwin”`)

- *Note:* Do not mix package managers. Environment can become unstable.

---

# Environment Management with Anaconda
## What is a YAML File?

- `.yaml` or `.yml` --> Balance between structure and readability.

- **Human-Readable Format:** Designed to be easily readable by humans and is often used for configuration files.

- **Hierarchical Structure:** Uses indentation to represent hierarchical data structures, such as lists and dictionaries.

- **Key-Value Pairs:** Data is typically represented using key-value pairs, making it similar to Python dictionaries.

- **Multiline Strings:** Supports multiline strings, making it convenient to represent longer text.

- **Comments:** Supports comments using the # symbol, allowing for annotations within the file.

- **Widespread Usage:** It's commonly used in various applications, including configuration for CI/CD tools, Kubernetes configurations, and defining infrastructure as code.

---
layout: two-cols-header
---

# Environment Management with Anaconda
## Creating a New Environment from a YAML File

::left::

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-02/s13_img01.png" alt="lecture-02 slide 13 image 1" class="max-h-80 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

::right::

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-02/s13_img02.png" alt="lecture-02 slide 13 image 2" class="max-h-80 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

---
layout: image-right
image: /images/lecture-02/s14_img01.png
backgroundSize: contain
---

# Advanced Environment Management
## Creating a New Environment from a `pyproject.toml`


- `pyproject.toml` is the modern Python packaging standard (PEP 518).

- Centralizes metadata and dependencies.

- Declares build backend and build dependencies.

- Works with tools like `setuptools`, `poetry`, and `flit`.

- **Improves reproducible builds.**

---

# Environment Management with Anaconda
## Creating a New Environment


- Create a new environment from a YAML or text file
  - `conda create --name EnvironmentName file=package_contents.yml`
  - `conda create --name EnvironmentName file=package_contents.txt`

- These approaches still occur, but are considered obsolete.

- Create a new environment from a pyproject.toml file
  - `conda create --name EnvironmentName`
  - `pip install -e .`

---

# Advanced Environment Management
## Activity #4

- Evaluate the .txt, .yaml, and .toml files in the repository.

- Install the required dependencies for the CI-Nanocourse repository using the pyproject.toml file.

- Confirm that the installation is correct and that the dependencies can be imported upon launching python.

---

# Environment Management with Anaconda
## Environment Tips and Tricks


- Don’t mix and match Package Managers (`pip` vs `conda`).

- Be judicious with your dependencies.

- Be explicit with your dependencies.

---

# Advanced Environment Management
## What Approach is Best?


- Large number of package managers creates a fragmented ecosystem.

- To standardize Python packaging, the `pyproject.toml` file was created.

- Significant step forward in the standardization and enhancement of Python packaging tools.

- It offers several benefits over text and YAML files

---

# Advanced Environment Management
## Activity #5

- Add Seaborn to your `pyproject.toml` file - **https://pypi.org/project/seaborn/**

- Reinstall your local package

- Confirm that seaborn was included in the install

- Launch python, import seaborn, and if time permits, plot something with seaborn.

- Install the docs optional dependencies.

---
layout: center
class: text-center
---

# Lecture 3
## Git Essentials

---
layout: image-right
image: /images/lecture-03/s02_img01.png
backgroundSize: contain
---

# Git Essentials
## Branching Strategies for Collaborative Development

- **"Git Flow"**

- A fixed branching model that defines different branches for features, releases, and hotfixes.

- Provides a structured workflow that is especially useful for larger teams and projects.


---
layout: image-right
image: /images/lecture-03/s02_img01.png
backgroundSize: contain
---

# Git Essentials
## Release Branching


- Branches are created for potential releases.

- Allows for specific features to be included or excluded from releases and for patching release-specific issues.

- “master” or “main” used for production releases.

---
layout: image-right
image: /images/lecture-03/s02_img01.png
backgroundSize: contain
---

# Git Essentials
## Feature Branching

- Each new feature or bugfix is developed in a separate branch derived from the **develop** branch.

- Keeps the develop branch more stable.

- Allows multiple features to be developed in parallel without interference.

---
layout: image-right
image: /images/lecture-03/s02_img01.png
backgroundSize: contain
---

# Git Essentials
## Trunk Based Development

- Developers work in short-lived branches derived from develop, ensuring that code is integrated frequently.

- Reduces merge conflict complexity by promoting regular merges.

- Long-lived branches can lead to complex, hard-to-resolve merge conflicts.

- Ensures that code in the develop branch is always production-ready.

---
layout: two-cols-header
---

# Git Essentials
## Writing Clear, Useful Commit Messages

::left::

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s05_img02.png" alt="lecture-03 slide 05 image 2" class="max-h-40 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-03/s05_img03.png" alt="lecture-03 slide 05 image 3" class="max-h-40 30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

::right::
<br><br>
- Using structured, meaningful commit messages to make history more readable and to allow for automated changelog generation.

---
layout: image-right
image: /images/lecture-03/s02_img01.png
backgroundSize: contain
---

# Git Essentials
## Pull/Merge Requests

- Before merging a feature branch into the develop, a pull (or merge) request is created.

- Allows team members to review code, ensuring quality and consistency.

- Pull requests should preferably be manageable in size (~400 lines of code max), and accompanied with unit tests (more following).

---
layout: image-right
image: /images/lecture-03/s07_img02.png
backgroundSize: contain
---

# Git Essentials
## Rebase vs Merge

- Instead of merging, use **rebasing** to apply feature branch changes on top of the main branch.

- Provides a cleaner, linear project history but requires a more cautious approach to avoid conflicts.

---

# Git Essentials
## Fork-Based PR Workflow (CLI)


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s08_img01.png" alt="lecture-03 slide 08 image 1" class="max-h-30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

What if you don’t have write access to a repository?
- Create **fork** in GitHub and clone the repository.
- Set upstream remote to help synchronize your fork with the original repository.
- Create a branch.
- Make changes to your branch.
- Sync with upstream, update any conflicts if they arise.
- Push changes to fork.
- Navigate to fork on GitHub, and click “New pull request”.

---

# Git Essentials
## Advanced Pull Requests


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s08_img01.png" alt="lecture-03 slide 08 image 1" class="max-h-30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->
<br>
<!-- code:start -->
```bash
git clone <repository_URL>
git remote add upstream <original_repository_URL>
git checkout -b <branch_name>
git add .
git commit -m "Describe the changes made"
git fetch upstream
git merge upstream/main
git push origin <branch_name>
```
<!-- code:end -->


---

# Git Essentials
## Resolving Conflicts


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s09_img01.png" alt="lecture-03 slide 09 image 1" class="max-h-30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- Git will notify you of ***merge conflicts*** when attempting to merge or rebase.
- Indicated by `<<<<<<<, =======, >>>>>>>` within files.
- The content between `<<<<<<<` and `=======` is your branch's changes, while the content between `=======` and `>>>>>>>` is from the branch you're trying to merge or rebase with.
- Edit the file to resolve the conflict. This might mean choosing one change over the other, combining both changes, or even making a new change altogether.
- Once resolved, remove the conflict markers (`<<<<<<<, =======, >>>>>>>`).

---
layout: image-right
image: /images/lecture-03/s10_img01.png
backgroundSize: contain
---

# Git Essentials
## Placing “Blame”

- `git blame` shows the last commit for each line.

- Use it to trace history, not assign fault.

- Check commit messages and PRs for context.

- GUI tools can make blame output easier to read.

---

# Git Essentials
## Event Driven Tests

- Run automated checks when repository events occur (push, pull request, release).

- Start with fast checks: linting and unit tests.

- Add project-specific checks: documentation build, coverage, and security scans.

- In this course, we implement these checks with GitHub Actions in Lecture 8.

---
layout: image-right
image: /images/lecture-03/s12_img01.png
backgroundSize: contain
---

# Git Essentials
## Issue Tracking


- GitHub provides integrated issue, branch, and PR tracking.

- Each issue assigned a number (#638) which can be used as a tag in commits, comments, etc.

- Can be designated with a label (e.g., low priority).

- Can be assigned to an individual.

- Linked PRs automatically

---
layout: image-right
image: /images/lecture-03/s13_img01.png
backgroundSize: contain
---

# Git Essentials
## Issue Creation

- *Title:* concise and descriptive.

- Expected behavior vs actual behavior.

- Steps to reproduce.

- Full traceback or error output.

- *Environment:* OS, Python, package versions.

- Relevant logs.

---
layout: image-right
image: /images/lecture-03/s14_img01.png
backgroundSize: contain
---

# Git Essentials
## Issue Creation: Helpful Additions

- Add screenshots or recordings when useful.

- Include severity and user impact.

- Provide workaround or minimal repro code.

- Add labels and regression details when relevant.

- Include extra context: frequency and scope.

---
layout: two-cols-header
---

# Git Essentials
## Issue Formatting

::left::

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s16_img01.png" alt="lecture-03 slide 16 image 1" class="max-h-50 w-auto object-contain rounded shadow" />
</div>
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s16_img02.png" alt="lecture-03 slide 16 image 2" class="max-h-30 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

::right:: 

- GitHub Issues support styling with Markdown.

- Can create checklists, headers, links, images, mention people/teams/issues/pull requests, quote code, create blocks, dropdowns, and more.

- [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

---

# Git Essentials
## Branch Linking


<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-03/s17_img01.png" alt="lecture-03 slide 17 image 1" class="max-h-50 w-auto object-contain rounded shadow" />
  <img src="/images/lecture-03/s17_img02.png" alt="lecture-03 slide 17 image 2" class="max-h-50 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- By creating a branch that is directly linked to the issue, all progress on that issue is tracked.

- When a PR is approved, the issue is automatically closed.

---

# Git Essentials
## Activity #6

- Make your own repo on GitHub

- Create a `pyproject.toml` file.

---
layout: center
class: text-center
---

# Lecture 4
## Organization and MVC

---

# Repository Organizational Strategies
## Fighting Entropy

- Organizing a GitHub repository for Python software in a structured and consistent manner is crucial for clarity, collaboration, and maintainability.
- Directory Structure:
  - Use a standard project layout. Common directories include:
  - src/: For the main source code.
  - tests/: For unit tests.
  - docs/: For documentation.
  - scripts/: For utility scripts and auxiliary code.
  - data/: For data files, if applicable.
---

# Repository Organizational Strategies
## Must-Have Repository Files

- README File - Always have a README.md at the root. It should include:
  - Project title and brief description.
  - Installation and usage instructions.
  - Contribution guidelines.
  - Licensing information.
- License - Include a LICENSE file that clearly states the licensing terms.
- Badges - Use badges in the README.md to quickly display project status, such as build status, test coverage, and package version.


---
layout: image-right
image: /images/lecture-04/t03_from_s03.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Must-Have Repository Structure

- `.gitignore` for generated and local-only files.
- `requirements.txt` or `pyproject.toml` for dependencies.
- `docs/` for documentation.
- `tests/` for automated validation.
- `src/` for application code.

---
layout: image-right
image: /images/lecture-04/t04_from_s04.png
backgroundSize: contain
---

# Repository Organizational Strategies
## Bonus Tools

- `CODE_OF_CONDUCT.md` for community expectations.
- `CONTRIBUTING.md` for contributor workflow.
- `CHANGELOG.md` for release history.
- Issue/PR templates for consistent submissions.
- Dependabot (or similar) for dependency security.

---

# Code Organizational Strategies
## Maintaining Structure as Projects Scale

- Organizing code in Python is crucial for maintainability, scalability, and clarity.

  - Modularity - Divide your code into modules and packages. Each module should have a specific responsibility aligned with the MVC pattern.
  - Naming Conventions - Use clear and descriptive naming conventions. For example:  `data_source.py`, `file_management.py`, `data_visualization.py`.
  - Code Reusability - Abstract out common functionalities into utility functions or base classes to avoid repetition and enhance reusability.
---

# Model-View-Controller Architecture
## A Guiding Framework

- The "Model" represents the data and logic, governing the rules and data manipulation.
- The "View" displays the data, handling the presentation and user interface elements.
- The "Controller" manages user input, interpreting it to update the model and view accordingly, acting as a bridge between the two.
- The Model-View-Controller (MVC) architecture is a design pattern that separates software applications into three interconnected components.
---

# Model-View-Controller Architecture
## The View: Responsibilities

- Tkinter:
  - The standard GUI library for Python, bundled with most Python installations.
  - Offers a simple way to create windows, dialogs, buttons, and other GUI elements.
- PyQt and PySide:
  - Bindings for the Qt application framework.
  - PyQt is available under GPL or commercial licenses, while PySide is available under LGPL.
  - Suitable for creating professional-looking applications with advanced features.
- wxPython:
  - A binding for the wxWidgets C++ library.
  - Provides native-looking GUI applications for Windows, macOS, and Linux.
- Python offers a variety of libraries and frameworks for creating Graphical User Interfaces (GUIs). Here are some of the most popular ones:
---

# Model-View-Controller Architecture
## The View

- User Interface - The View is responsible for displaying the user interface (UI) of the application. It defines how data is presented to the user and how the user interacts with it.
- Receives User Input - While the View primarily focuses on display, it also captures user input, such as button clicks, text input, or gestures, and forwards them to the Controller for processing.
- Stateless - Ideally, the View should be stateless, meaning it displays data without storing or processing it. Any data or logic-related tasks should be handled by the Model or Controller.
- Reactive to Model - The View reflects changes in the Model. When the data in the Model changes, the View updates automatically to display the latest information to the user.
- Decoupled from Model and Controller - To maintain the separation of concerns, the View should be decoupled from the Model and Controller. This means changes in the View shouldn't directly affect the Model's data or the Controller's logic, ensuring modularity and ease of maintenance.
---

# Model-View-Controller Architecture
## The Controller

- Mediator - The Controller acts as a mediator between the Model and the View. It receives user input from the View, processes it (possibly updating the Model), and then returns the display output to the View.
- Event Specification - It specifies which elements in the view should trigger events when selected.
- User Input Handling - One of the primary responsibilities of the Controller is to handle user input. Whether it's a button click, form submission, or any other interaction in the View, the Controller decides what should happen in response.
- Logic Execution - While the Model deals with data and the View deals with presentation, the Controller is where much of the application's business logic is executed. It determines how the application should respond to various user inputs and actions.
- State Management - The Controller often manages the flow of data and the state of the application. It can decide which View to display next, fetch data from the Model to update the View, or store data in the Model based on user input.
---

# Model-View-Controller Architecture
## The Model

- Data Representation - The Model represents the application's data and the rules that govern access to and updates of this data. It is the central component that holds the core functionality.
- Data Storage - Often, the Model is responsible for retrieving or storing data, which can be in a database, file, or any other storage mechanism.
- Data Notification - When data in the Model changes, it can notify the View so that the interface can be updated accordingly. This ensures that the user interface reflects the current state of the data.
- Logic - While the Controller handles user interactions, the Model contains the core logic that dictates how data can be created, stored, modified, and retrieved. It enforces rules, constraints, and validations related to the data.
---

# Organization and MVC
## Activity #7

- Upload individual files to GitHub
- Place code in appropriate organizational structure.

---
layout: center
class: text-center
---

# Lecture 5
## CI/CD Fundamentals

---

# What Is CI/CD?
## CI validates code changes; CD manages release automation

- Continuous Integration (CI): merge small changes frequently and run automated checks on every push or pull request.
- Continuous Delivery: keep the default branch releasable at all times.
- Continuous Deployment: automatically deploy after all quality gates pass.

---
layout: image-right
image: /images/lecture-05/t03_from_s03.png
backgroundSize: contain
---

# Vocabulary
## Core CI/CD Terminology

- Build: turn source code into an installable or runnable artifact.
- Test: verify expected behavior automatically.
- Release: version and publish an artifact for users.
- Deploy: promote a release to an environment (staging/production).
- Pipeline: ordered automation steps that enforce quality gates.
---
layout: image-right
image: /images/lecture-05/t04_from_s04.png
backgroundSize: contain
---

# How Do We Know This Function Works?
## Unit tests catch regressions early

```python
def square(x):
    """Return the square of a number."""
    return x * x

def test_square():
    """Ensure the square function works correctly."""
    assert square(2) == 4
    assert square(-3) == 9
```

- Run quickly with `pytest -q` locally and in CI.
- Common test levels:
  - Unit: isolated behavior in a function/module.
  - Integration: interaction between components.
  - System: end-to-end behavior in realistic conditions.
  - Regression: prevents previously fixed bugs from returning.
---

# Typical Pipeline Stages
## From commit to deploy in repeatable steps

- Lint and format checks (`ruff`, `black --check`)
- Unit/integration tests (`pytest`)
- Package build (`python -m build`)
- Optional checks (coverage, docs, security)
- Release/deploy only when required checks succeed

---
layout: image-right
image: /images/lecture-05/t11_from_s16.png
backgroundSize: contain
---

# Goal of CI/CD
## Keep changes close to `main` through frequent integration

- Prefer short-lived branches and small pull requests.
- Run checks on every pull request before merge.
- Block merge when required checks fail.
- Reduce late merge conflicts and release surprises.
---

# Why is CI/CD useful?
## Quality, reliability, and faster feedback cycles

- Makes failures visible within minutes, not days.
- Prevents broken code from reaching shared branches.
- Improves reproducibility for research code and analysis workflows.
- Increases confidence when multiple contributors are involved.
---

# Implementing CI/CD in Practice
## A minimum viable pipeline for this course

- Version control with pull requests (`git` + GitHub).
- Install dependencies from `pyproject.toml`.
- Run linting and tests (`ruff`, `pytest`) on push and pull request.
- Require passing checks before merging to `main`.
- Optional extension: publish docs and releases automatically.
---

# Additional CI/CD tools in the workflow
## Code quality, coverage, documentation, and security checks

- Coverage reporting (`pytest-cov`, Codecov)
- Documentation build validation (Sphinx)
- Dependency and static security scanning (Dependabot, CodeQL)
- Branch protection rules (required checks and review)
---

# Local CI/CD workflows
## Run checks locally before pushing to the repository

- Use `pre-commit` to run fast checks before each commit.
- Run the same commands locally that CI will run remotely.
- This reduces failed pipelines and review delays.

```bash
pre-commit run --all-files
ruff check .
pytest -q
```
---

# Running the CI/CD workflow
## Selecting a Continuous Integration Platform

- This course uses GitHub Actions because our repositories live on GitHub.
- Other platforms include Jenkins, GitLab CI, CircleCI, and cloud-native CI tools.
- Most CI systems define workflows as YAML files executed by hosted runners.

---
layout: image-right
image: /images/lecture-05/t17_from_s22.png
backgroundSize: contain
---

# GitHub Actions Dashboard
## Viewing workflow runs and statuses

- Check whether a run passed, failed, or was canceled.
- Open failed jobs to inspect logs and traceback output.
- Re-run failed jobs after fixing the issue.
---
layout: image-right
image: /images/lecture-05/t18_from_s23.png
backgroundSize: contain
---

# GitHub Actions Workflow Example
## Reading a basic workflow YAML file

- Core keys you will see: `name`, `on`, `jobs`, `runs-on`, `steps`.
- Each job runs in a clean environment unless artifacts/cache are restored.
- We will build one of these step-by-step in Lecture 8.
---
layout: center
class: text-center
---

# Lecture 6
## Code Quality and Linting

---

# Outline
## Defining Clean Code

- Techniques to Maintain Clean Code
  - Code formatters and linting
- Utilizing pre-commit hooks to enforce coding standards and maintain code with Github.
- Exercise
---

# What is Clean Code?
## Readable, maintainable code is easier to review and evolve

- Consistent formatting. Should follow PEP 8 standards for Python.
- Meaningful names - descriptive variable, function, and class names.
- Simple. Functions and classes should do one thing only, and do it well.
- Well-documented.
- Type hinted.
- Testable.
---

# PEP 8 Naming Conventions
## Classes - CamelCase (MyClass)

- Variable - snake_case and lowercase (first_name)
- functions - snake_case and lowercase (quick_sort())
- Constants - snake_case and uppercase (PI = 3.14159)
- Modules should have short, snake_case names and all lowercase (numpy)
- Single quotes and double quotes are treated the same (just pick one and be consistent)
- Triple quotes should always be “””Your text here””” not ‘’’Your text here’’’
---

# Variable Naming
## Use descriptive `snake_case` identifiers

- Use descriptive, lowercase names – Variables should be meaningful and easy to understand.
  - ✅ max_users = 100  ❌ mu = 100
- Use underscores for multi-word names (snake case) – Improves readability.
  - ✅ user_count = 10  ❌ userCount = 10 (CamelCase is for classes, not variables)
- Avoid single-letter names (except for short loops) – Be explicit.
  - ✅ temperature_celsius = 25.0  ❌ t = 25.0
- Constants should be uppercase with underscores – Used for values that don’t change.
  - ✅ MAX_RETRIES = 5  ❌ maxRetries = 5
- Private variables start with an underscore – Signals internal use.
  - ✅ _cache = {}   ❌ cache = {} (unless public)
- Avoid reserved keywords – Prevent conflicts with Python’s built-in functions.
  - ✅ class_name = "Intro to CI"    ❌ class = "Intro to CI" (conflicts with the class keyword)
---

# Function Naming
## Choose verb-based, descriptive function names

- Use lowercase with underscores – Improves readability and consistency.
  - ✅ def get_user_data():  ❌ def GetUserData(): (CamelCase is for classes)
- Use descriptive names – Functions should clearly indicate their purpose.
  - ✅ def calculate_total_price():    ❌ def calc():
- Use verbs for function names – Functions perform actions, so names should reflect that.
  - ✅ def fetch_records():    ❌ def records():
- Use a leading underscore for internal or private functions – Signals intended internal use.
  - ✅ def _connect_to_db():    ❌ def connect_to_db(): (if meant to be private)
- Avoid using built-in function names – Prevents accidental overrides.
  - ✅ def format_report():    ❌ def format(): (overrides Python’s built-in format function)
- Use double leading underscores only for name-mangling in classes – Rarely needed.
  - ✅ class Example:  def __private_method(self): Double underscore automatically renamed within a class…
---

# Class Naming
## Use `PascalCase` nouns for class names

- Use CapWords (PascalCase) – Each word starts with a capital letter, with no underscores.
  - ✅ class DataProcessor:   ❌ class data_processor:
- Class names should be nouns or noun phrases – Represents objects or entities.
  - ✅ class UserProfile:    ❌ class processUser(): (Functions use verbs, not classes)
- Avoid abbreviations – Use clear and meaningful names.
  - ✅ class AuthenticationManager:    ❌ class AuthMgr:
- Use leading underscores for internal classes – Signals that the class is for internal use only.
  - ✅ class _InternalHelper:    ❌ class InternalHelper: (if not meant for external use)
- Use metaclass naming convention – Append "Meta" if defining a metaclass.
  - ✅ class CustomMeta(type):    ❌ class CustomMetaclass:
- Exception classes should end with `Error` – Makes it clear they are exceptions.
  - ✅ class ValidationError(Exception):    ❌ class ValidationIssue:
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

- comments should be complete sentences
- comments should have a space after the # sign with the first word capitalized
- don’t litter commented code throughout your software.
---

# Documenting Code
## Write clear, structured docstrings

<!-- code:start -->
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
<!-- code:end -->

- def divide(a, b):
- """
- Divides two numbers.
- Parameters
- ----------
- a : float
- Numerator.
- b : float
- Denominator.
- Returns
- -------
- float
- Result of division.
- Raises
- ------
- ZeroDivisionError
- If b is zero.
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
## Pylint: Python Code Linter

- Flake8: Python Code Linter to identify style differences in code
- Black: code formatter
- Ruff: rust optimized code formatter and linter
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
---

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

- Many IDEs such as vscode or pycharm have built in linters that identify smaller coding errors and improve code formatting
- Possible to install Ruff into vscode
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
- Install pre-commit in conda environment using pip install pre-commit or integrate pre-commit dependence in pyproject.toml
- Add a pre-commit config file called .pre-commit-config.yaml to project
- In yaml file: add ruff repo
---

# Run Ruff Locally to Identify Errors
## Install Ruff and run an initial check

  - Pip install Ruff
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

  - pip install pre-commit
  - Add dependency in pyproject.toml (it should already be added)
- create .pre-commit-config.yaml file and add to repo
- In .pre-commit-config.yaml file
  - Add the following pre-commit information
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
---

layout: center
class: text-center
---

# Lecture 7
## Unit Testing and TDD

---

# Session Context
## Instructor and Course Context

- Conor McFadden
- Continuous Integration with Python Nanocourse 2023
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

# Writing a Unit Test
## Arrange, Act, Assert, and Cleanup

- Act: action that we would like to test, function or process.
- Assert: checking the result state to see if it matches expectations. Look at output and make judgment
- Cleanup: cleanup tests so other downstream tests aren’t influenced by results or attributes.


---
layout: image-right
image: /images/lecture-07/t07_from_s07.png
backgroundSize: contain
---

# Running Pytest
## Run tests from the command line with `pytest`

- Assert is True, the test passes!


---
layout: image-right
image: /images/lecture-07/t09_from_s09.png
backgroundSize: contain
---

# Pytest Test Discovery
## Pytest discovers functions prefixed with `test_`
---
layout: image-right
image: /images/lecture-07/t10_from_s10.png
backgroundSize: contain
---

# Test Parameterization
## Test multiple cases with `pytest.mark.parametrize`


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
layout: image-right
image: /images/lecture-07/t12_from_s13.png
backgroundSize: contain
---

# Fixtures in Pytest: Example in PyCalc
## Using shared setup in `conftest.py`
---
layout: image-right
image: /images/lecture-07/t13_from_s14.png
backgroundSize: contain
---

# Key Binding Test in PyCalc Exercise
## Shared test fixtures and setup

- test_controller.py
- Fixtures  conftest.py
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

# Exercise
## Add test dependencies and write initial unit tests

- pip install –e .[dev] or pip install –e “.[dev]” on Mac
- Write a unit test to test _calculateResult function in controller.py
- If time is remaining, parameterize the test for _calculateResult

---
layout: center
class: text-center
---

# Lecture 8
## GitHub Actions


---

# Creating a GitHub Workflow
## Follow the official GitHub Actions quickstart

- Goal: run automated checks whenever code is pushed or a PR is opened.
- Start with one simple workflow, then extend it iteratively.
- Keep commands in CI aligned with commands you run locally.

---
layout: image-right
image: /images/lecture-08/t05_from_s06.png
backgroundSize: contain
---

# Workflow File Location
## Store workflow files in `.github/workflows`

- Workflow files must live in `.github/workflows/`.
- Use descriptive names, for example: `ci.yml`, `tests.yml`, `docs.yml`.
- One repository can have multiple workflow files.

---
layout: image-right
image: /images/lecture-08/t06_from_s07.png
backgroundSize: contain
---

# The `github-actions-demo.yml` Workflow
## Workflow file structure and key sections

- [https://docs.github.com/en/actions/quickstart](https://docs.github.com/en/actions/quickstart)

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest -q
```
---
layout: image
image: /images/lecture-08/t07_from_s08-09.png
backgroundSize: contain
---

# What Do These Two Lines Do?
## Understanding core workflow declarations

- `name`: label displayed in the Actions UI.
- `on`: events that trigger this workflow.
- Example: `on: [push, pull_request]` catches both direct pushes and PR updates.
---

# What Is `${{ }}`?
## GitHub expressions evaluate runtime context values

- Expressions are evaluated by Actions at runtime.
- `${{ github.actor }}` resolves to the username that triggered the run.
- `${{ github.ref_name }}` resolves to the branch or tag name.
- Use expressions in `if:`, `env:`, `with:`, and step arguments.

---
layout: image-right
image: /images/lecture-08/t09_from_s11.png
backgroundSize: contain
---

# What Do These Entries Do?
## Workflow triggers define when jobs run

- Common trigger patterns:
  - push to specific branches (e.g., `main`)
  - pull request opened/synchronized
  - manual execution with `workflow_dispatch`
- Use branch filters to avoid unnecessary runs.
---

# Defining the jobs
## Understanding the `jobs` key

<!-- photos:start -->
<div class="mt-4 flex flex-wrap items-center justify-center gap-3">
  <img src="/images/lecture-08/t11_from_s13-14-15-16-17-18-19.png" alt="lecture-02 slide 13 image 1" class="max-h-80 w-auto object-contain rounded shadow" />
</div>
<!-- photos:end -->

- Each job has an ID (for example `test`, `lint`, `docs`).
- Jobs can run in parallel unless dependencies are declared with `needs:`.
- Keep job responsibilities narrow for clearer failures.

---

# Defining the jobs: Key fields
## A workflow can contain one or more named jobs

- `runs-on`: execution environment (for example `ubuntu-latest`).
- `steps`: ordered units of work inside the job.
- `uses`: run a reusable action.
- `run`: execute shell commands directly.

---
layout: image-right
image: /images/lecture-08/t12_from_s20-21.png
backgroundSize: contain
---

# The full Explore-GitHub-Actions job
## Combining runner settings, steps, and actions

- Read from top to bottom: setup, install, validate, report.
- Every step should have a clear purpose and deterministic output.
- Fail fast on setup errors to save runner time.
---

# Building a Useful Sequence of Steps
## We can copy commands that work locally into run: operations

- Good ordering:
  - checkout repository
  - setup Python
  - install dependencies
  - run lint/tests
  - upload artifacts or coverage
- Marketplace actions: https://github.com/marketplace?type=actions

---
layout: image-right
image: /images/lecture-08/t14_from_s23.png
backgroundSize: contain
---

# GitHub Marketplace
## Finding reusable actions for workflows

- Prefer well-maintained actions with clear documentation.
- Check update frequency, issue activity, and publisher trust.
---
layout: image-right
image: /images/lecture-08/t15_from_s24.png
backgroundSize: contain
---

# Search for Codecov
## Locating coverage-reporting actions

- Add coverage upload only after tests reliably run in CI.
- Coverage reports are useful for tracking testing gaps over time.
---
layout: image-right
image: /images/lecture-08/t16_from_s25.png
backgroundSize: contain
---

# Use the Latest Version
## Selecting the latest action reference

- Avoid unpinned `@main`.
- Prefer stable major tags (for example `@v4`) or pinned SHAs for stricter reproducibility.
---
layout: image-right
image: /images/lecture-08/t17_from_s26.png
backgroundSize: contain
---

# Copy the action as a step in your job
## Adding reusable actions under `steps`

```yaml
- name: Upload coverage
  uses: codecov/codecov-action@v5
```
---
layout: image-right
image: /images/lecture-08/t18_from_s27.png
backgroundSize: contain
---

# Actions for Common CI Tasks
## Reusable actions for testing, docs, and releases

- `actions/checkout` for repository checkout
- `actions/setup-python` for Python runtime
- `codecov/codecov-action` for coverage reporting
- `actions/upload-artifact` for logs/build outputs
---

# Exercise: Add a workflow to automatically run unit tests on git push to your repository
## Implement a workflow that runs `pytest`

- Minimum requirements:
  - trigger on `push` and `pull_request`
  - install dependencies from `pyproject.toml`
  - run `pytest -q`
- Stretch goals:
  - add a Python matrix (for example 3.10, 3.11, 3.12)
  - test on multiple OS runners (`ubuntu`, `macos`, `windows`)
- Reference: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

---
layout: center
class: text-center
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
