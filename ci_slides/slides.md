---
theme: default
title: CI Nanocourse
info: Lectures 1-9 converted from Keynote/PPTX source material.
mdc: true
---

---
layout: cover
class: text-center
---
# CI Nanocourse
## Lectures 1-9 (Slidev Conversion Draft)

---
layout: center
class: text-center
---
# Lecture 1
## Introduction to Collaborative Software Development

---
layout: cover
class: text-center
---
# Introduction to Python Software Development on GitHub
---

# Introduction
## About Us

- Conor McFadden
- M.S. Medical Physics
- B.S. Applied Physics
- Kevin Dean
- Ph.D. Biochemistry
- B.A. Chemistry
- [https://www.dean-lab.org/](https://www.dean-lab.org/)
- [https://github.com/TheDeanLab](https://github.com/TheDeanLab)
---

# Course Structure
## Day 1

- Introduction to Collaborative Software Development
- Environment Management & Git Essentials
- Organizational Strategies, and Collaborative Development Workflows
- Pre-Commit Hooks, Linters, Code Formatters
---

# Course Structure
## Day 2

- Unit Testing and Test-Driven Development (TDD)
- Setting up Continuous Integration Pipelines on GitHub
- Public-Facing Documentation
- Stable Releases
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

# The Importance of Collaboration
## Teamwork is Dreamwork

- Diverse Skill Sets: No single developer possesses expertise in every aspect of software development. Collaborative efforts ensure that a team with varied skills can address different facets of a project, from front-end design to back-end logic, ensuring comprehensive development.
- Accelerated Problem-Solving: Challenges are inevitable in software development. A collaborative team can brainstorm, debate, and ideate solutions faster than an individual. This collective problem-solving often leads to more innovative and efficient solutions.
- Continuous Feedback Loop: Collaboration fosters a culture of continuous feedback. Regular code reviews, paired programming, and open discussions ensure that errors are caught early, and best practices are consistently upheld.
- Shared Responsibility: A collaborative environment distributes the responsibility of the project. This not only reduces the pressure on individual team members but also ensures accountability and commitment towards the project's success.
- Adaptability & Flexibility: In a collaborative setting, teams are better equipped to adapt to changes, be it in project requirements, technologies, or methodologies. The collective knowledge ensures a smoother transition and quicker adaptation.
- Knowledge Transfer & Skill Enhancement: Collaboration is a learning experience. Developers can share knowledge, introduce peers to new tools or methodologies, and elevate the overall skill set of the team.
---

# Overview of Version Control Systems
## Git, Subversion, …

- What is VCS?
  - A tool that tracks changes in files, often used in codebases.
- Significance of VCS:
  - History: Records every modification, allowing rollbacks.
  - Collaboration: Enables multiple developers to work simultaneously.
  - Accountability: Tracks who made what change and when.
  - Backup: Safeguards code against accidental deletions or errors.
  - Branching: Allows development of features in isolation.
- VCS is foundational for collaborative, error-free, and efficient software development.
---

# An Introduction to Git
## And its role in facilitating team-based development.

- What is Git?
  - A distributed version control system widely used in software development.
  - Enables software to be developed locally (on a developer's machine) or remote (on a server or hosted platforms like GitHub), facilitating collaboration and version control for projects of any size.
  - Provides control over contributors to code.
---

# An Introduction to Git
## Installing Git

- Visit the official Git website at git-scm.com
- Windows
  - Download the latest version for Windows
  - Run the downloaded .exe file and follow the installation prompts with default settings.
- macOS
  - Installed by default with Xcode. Otherwise, requires Homebrew or MacPorts.
- Linux
  - Installed using Linux distribution package manager. If on BioHPC, available as a module (module load git/v2.5.3)
---

# Basic Git Commands and Workflows

- Git Up, Git Out, and Git Something
- Repository
- Definition: A repository, often abbreviated as "repo", is a storage location where all the files and revision history of a project reside.
- It acts as the central hub for a project's codebase, allowing developers to clone, pull, and push changes to and from it.
- A repository contains the information that Git uses to track the progression of a project.
---

# Basic Git Commands and Workflows
## Cloning a Repo

- Cloning: Downloads a repository onto your machine locally with all necessary information for tracking code development.
- git clone - Clones a repository into a newly created directory, and creates remote-tracking branches for each branch in the cloned repository.
- [https://git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone)
---

# Basic Git Commands and Workflows
## Isolating Development

- Branch
- Definition: A branch is a lightweight movable pointer that points to a specific commit.
- It represents an independent line of development, allowing you to isolate work on different features, bug fixes, or experiments without affecting the main or other branches.
- This facilitates parallel development, where multiple features or fixes can be developed simultaneously without interfering with each other.
- Main Branch: By default, every Git repository starts with a branch called "master" or, more recently, "main". This is the primary branch where stable, production-ready code resides.
---

# Basic Git Commands and Workflows

- Creation: Creating a new branch does not create a new copy of the repository. Instead, it's a lightweight pointer to a commit. This makes branching in Git very fast and efficient.
- git branch - List, create, or delete branches.
- Creating a New Branch
- [https://git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch)
---

# Basic Git Commands and Workflows
## Switching to a Branch

- Switching: You can easily switch between branches using the git checkout command (or git switch in newer versions of Git).
- git checkout - Switch branches.
- [https://git-scm.com/docs/git-checkout](https://git-scm.com/docs/git-checkout)
---

# Basic Git Commands and Workflows
## Merging a Branch

- Merging: Once work on a branch is complete, it can be "merged" back into another branch, usually the main branch. This integrates the changes made in the branch into the main line of development.
- git merge - Join two or more development histories together.
- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
---

# Basic Git Commands and Workflows
## Challenges with Git

- Complex Commands: Git's command-line interface can be intimidating, especially for beginners. Remembering and correctly executing multiple commands can lead to errors.
- Merge Conflicts: Resolving conflicts when multiple developers make changes to the same section of code can be tedious and confusing.
- Visualizing History: The command-line doesn't provide an intuitive way to visualize the commit history, branches, and their relationships.
- Staging Changes: Deciding what changes to stage for a commit can be cumbersome, especially in large codebases.
- Switching Context: Frequent switching between branches and keeping track of which branch you're on can be error-prone.
---

# Basic Git Commands and Workflows
## Cheat to Compete with GitHub Desktop

- User-Friendly Interface: GitHub Desktop provides a graphical user interface, making it more intuitive and accessible for those not comfortable with the command-line.
- Easy Conflict Resolution: The tool visually presents merge conflicts and offers guidance on resolving them, streamlining the process.
- Visual History: Users can easily see the commit history, changes made, and the structure of branches, aiding understanding and navigation.
- Drag-and-Drop Staging: Users can quickly select changes for staging by dragging and dropping, making the process efficient.
- Branch Management: Switching between branches, creating new branches, and merging becomes a couple-of-clicks operation, reducing the chances of errors.
- [https://desktop.github.com/](https://desktop.github.com/)
---

# Basic Git and Workflows
## Activity #1

- Install Git
- Create a GitHub account.
- Download GitHub Desktop
- Clone the class repo: https://github.com/TheDeanLab/CI-Nanocourse
- Using command-line and the GitHub Desktop, create a branch, and switch between main and the branch you created.
---
---
layout: center
class: text-center
---
# Intermission

---
layout: center
class: text-center
---
# Lecture 2
## Environment Management

# Environment Management with Anaconda
## Creating Reproducible Development Environments

- An environment is like a sandbox or petri dish, ensuring that the software setup for one project doesn't interfere with another.
- This enables a stable and reproducible development space.
- Version Inconsistencies: Python libraries and tools are constantly evolving. Different projects might require different versions of the same library, leading to potential conflicts and unexpected behavior.
- System-wide Installation Risks: Installing libraries system-wide can lead to "dependency hell", where upgrades for one project break another.
- Reproducibility: For scientific computing and data analysis tasks, it's crucial to reproduce results. This is impossible without consistent environment setups, especially when sharing work with peers or publishing results.
- Ease of Sharing: With a well-managed environment, developers can easily share their projects, ensuring that others can run their code without stumbling upon missing dependencies or version issues.
- Isolation: Keeping project environments separate ensures that specific dependencies or version requirements of one project don't interfere with another, leading to cleaner and more stable development.
---

# Environment Management with Anaconda
## Miniconda vs Anaconda

- Size and Content: Anaconda is a large distribution that comes pre-loaded with over 1500 packages tailored for scientific computing, data science, and machine learning. Miniconda, on the other hand, is a minimalistic distribution, containing only the package manager (conda) and a minimal set of dependencies.
- Flexibility vs. Convenience: While Anaconda provides an out-of-the-box solution with a wide array of pre-installed packages, Miniconda offers flexibility by allowing users to install only the packages they need, helping to keep the environment lightweight.
- Installation Size: Due to its bundled packages, Anaconda requires more disk space upon installation compared to Miniconda.
- Use Cases:
  - Miniconda is ideal for users who are conscious about disk space, or who prefer to have more control over their environment setup.
  - Anaconda is suited for those who want a comprehensive package suite without the need to manually install popular data science tools.
---

# Advanced Environment Management
## Activity #2

- Install Miniconda
---

# Environment Management with Anaconda
## Activating Your New Environment

- List all Environments:
  - conda env list
- Create new environment:
- conda create -n name_of_environment python=3.9.7
- Activate an Environment:
  - conda activate name_of_environment
- List Environment Packages:
  - conda list
---

# Advanced Environment Management
## Activity #3

- Create an Anaconda environment named ci_nanocourse with Python 3.9.7 or newer.
- Activate the environment, list its installed packages.
- Launch python, and run a basic print statement.
---

# Environment Management with Anaconda
## What is a Package?

- Software Collection: A package in Anaconda is a bundled collection of software tools, libraries, and dependencies that function together to achieve a specific task or set of tasks.
- Version Management: Each package has specific versioning, allowing users to install, update, or rollback to particular versions as needed, ensuring compatibility and stability in projects.
- Dependency Handling: When a package is installed in Anaconda, the system automatically manages and installs any required dependencies, ensuring seamless functionality and reducing manual setup efforts.
---

# Environment Management with Anaconda
## Creating a New Environment from a Text File

- Each package, and all of its dependencies, explicitly imported from a package manager (pip, conda, etc.)*
- Version Control
- (e.g., pyserial==3.5)
- Platform Control
- (e.g., sys_platform == “darwin”)
- *Note: Do not mix package managers. Environment can become unstable.
---

# Environment Management with Anaconda
## What is a YAML File?

- YAML files, typically with the .yaml or .yml extension, provide a balance between structure and readability, making them a popular choice for various configuration and data representation tasks.
- Human-Readable Format: Designed to be easily readable by humans and is often used for configuration files.
- Hierarchical Structure: Uses indentation to represent hierarchical data structures, such as lists and dictionaries.
- Key-Value Pairs: Data is typically represented using key-value pairs, making it similar to Python dictionaries.
- Multiline Strings: Supports multiline strings, making it convenient to represent longer text.
- Comments: Supports comments using the # symbol, allowing for annotations within the file.
- Widespread Usage: It's commonly used in various applications, including configuration for CI/CD tools, Kubernetes configurations, and defining infrastructure as code.
---

# Environment Management with Anaconda
## Creating a New Environment from a YAML File
---

# Advanced Environment Management
## Creating a New Environment from a pyproject.toml File

- Standardization: PEP 518 introduced pyproject.toml as a standardized configuration file for Python packaging, aiming to provide a single source of truth for package configurations. This unified approach reduces fragmentation in the packaging ecosystem.
- Extensibility: pyproject.toml is designed to be extensible. It can accommodate configurations for various tools like setuptools, black, mypy, and more, all in one place. This centralized configuration avoids the proliferation of various config files in a project's root directory.
- Build System Specifications: pyproject.toml allows package maintainers to specify which build system should be used and what the build dependencies are. This ensures that the right tools and versions are used during the build process.
- Clear Dependency Specification: While requirements.txt or YAML files list dependencies, pyproject.toml allows for a more detailed specification, including build dependencies, which are essential for reproducibility and consistent builds.
- Modern Tooling Compatibility: Modern packaging and build tools like poetry and flit natively use pyproject.toml, showcasing a move towards this standard in the Python community.
- Improved Isolation: With pyproject.toml, build dependencies can be isolated from the project's dependencies, ensuring that the build process doesn't affect the project's environment or vice versa.
---

# Environment Management with Anaconda
## Creating a New Environment

- Create a new environment from a YAML or text file
  - conda create --name EnvironmentName file=package_contents.yml
  - conda create --name EnvironmentName file=package_contents.txt
  - These approaches still occur, but are considered obsolete.
- Create a new environment from a pyproject.toml file
  - conda create --name EnvironmentName
  - pip install -e .
---

# Advanced Environment Management
## Activity #4

- Evaluate the .txt, .yaml, and .toml files in the repository.
- Install the required dependencies for the CI-Nanocourse repository using the pyproject.toml file.
- Confirm that the installation is correct and that the dependencies can be imported upon launching python.
---

# Environment Management with Anaconda
## Environment Tips and Tricks

- Don’t mix and match Package Managers.
- Be judicious with your dependencies.
- Be explicit with your dependencies.
---

# Advanced Environment Management
## What Approach is Best?

- Large number of package managers creates a fragmented ecosystem.
- To standardize Python packaging, the pyproject.toml file was created.
- Significant step forward in the standardization and enhancement of Python packaging tools.
- It offers several benefits over text and YAML files
---

# Advanced Environment Management
## Activity #5

- Add Seaborn to your pyproject.toml file - https://pypi.org/project/seaborn/
- Reinstall your local package
- Confirm that seaborn was included in the install
- Launch python, import seaborn, and if time permits, plot something with seaborn.
- Install the docs optional dependencies.
---
---
layout: center
class: text-center
---
# Intermission

---
layout: center
class: text-center
---
# Lecture 3
## Git Essentials

# Git Essentials
## When git push comes to shove

- Git Flow
- A fixed branching model that defines different branches for features, releases, and hotfixes.
- Provides a structured workflow that is especially useful for larger teams and projects.
---

# Git Essentials
## Release Branching

- Branches are created for potential releases.
- Allows for specific features to be included or excluded from releases and for patching release-specific issues.
- “master” or “main” used for production releases.
---

# Git Essentials
## Feature Branching

- Each new feature or bugfix is developed in a separate branch derived from the develop branch.
- Keeps the develop branch more stable.
- Allows multiple features to be developed in parallel without interference.
---

# Git Essentials
## Trunk Based Development

- Developers work in short-lived branches derived from develop, ensuring that code is integrated frequently.
- Reduces merge conflict complexity by promoting regular merges.
- Long-lived branches can lead to complex, hard-to-resolve merge conflicts.
- Ensures that code in the develop branch is always production-ready.
---

# Git Essentials
## Fear of Commitment.

- Using structured, meaningful commit messages to make history more readable and to allow for automated changelog generation.
---

# Git Essentials
## Pull/Merge Requests

- Before merging a feature branch into the develop, a pull (or merge) request is created.
- Allows team members to review code, ensuring quality and consistency.
- Pull requests should preferably be manageable in size (~400 lines of code max), and accompanied with unit tests (more following).
---

# Git Essentials
## Rebase vs Merge

- Instead of merging, use rebasing to apply feature branch changes on top of the main branch.
- Provides a cleaner, linear project history but requires a more cautious approach to avoid conflicts.
---

# Git Essentials
## Advanced Pull Requests

- What if you don’t have write access to a repository?
- Create fork in GitHub and clone the repository.
- Set upstream remote to help synchronize your fork with the original repository.
- Create a branch.
- Make changes to your branch.
- Sync with upstream, update any conflicts if they arise.
- Push changes to fork.
- Navigate to fork on GitHub, and click “New pull request”.
- [https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- git clone <repository_URL>
- 2. git remote add upstream <original_repository_URL>
- 3. git checkout -b <branch_name>
- 4A. git add .
- 4B. git commit -m "Describe the changes made"
- 5A. git fetch upstream
- 5B. git merge upstream/main
- 6. git push origin <branch_name>
---

# Git Essentials
## Resolving Conflicts

- Git will notify you of "merge conflicts" when attempting to merge or rebase.
- Within the conflicted files, Git uses conflict markers (<<<<<<<, =======, >>>>>>>) to indicate the conflicting sections.
- The content between <<<<<<< and ======= is your branch's changes, while the content between ======= and >>>>>>> is from the branch you're trying to merge or rebase with.
- Edit the file to resolve the conflict. This might mean choosing one change over the other, combining both changes, or even making a new change altogether.
- Once resolved, remove the conflict markers (<<<<<<<, =======, >>>>>>>).
---

# Git Essentials
## Placing “Blame”

- git blame is a tool to trace changes in a file back to the commit that introduced them. Use it as a diagnostic tool to understand the history of specific lines of code, not to assign fault.
- When examining the output, consider the broader context of changes. A developer might have moved or reformatted code, so they appear as the "blamer," even if they didn't originally write the logic. Dive deeper into the commit message and associated discussions for a full understanding.
- Integrate with Tools and GUIs - While the command-line version of git blame is powerful, several graphical user interfaces and tools offer more intuitive visualizations, helping to quickly pinpoint when and why changes were made.
---

# Git Essentials
## Event Driven Tests

- Automatically building, testing, and deploying changes to ensure new commits don't break existing functionality and meet quality standards.
- Often triggered upon generation of a pull request.
- Actions can be multi-faceted, and include code reformatting, testing, documentation generation, etc.
- More to follow…
---

# Git Essentials
## Issue Tracking

- GitHub provides integrated issue, branch, and PR tracking.
- Each issue assigned a number (#638) which can be used as a tag in commits, comments, etc.
- Can be designated with a label (e.g., low priority).
- Can be assigned to an individual.
- Linked PRs automatically
---

# Git Essentials
## Issue Creation

- Title - A concise and descriptive title that summarizes the issue.
- Description - A clear and detailed description of the issue. Explain what you expected to happen and what actually happened.
- Steps to Reproduce - Step-by-step guide on how to reproduce the issue. This helps maintainers replicate the problem on their end.
- Traceback - Detailed output from the console/terminal stating what the problem is.
- Environment Information - Python version (e.g., Python 3.8.5), Operating System and version (e.g., Ubuntu 20.04, Windows 10), version of the software or library causing the issue, any other relevant libraries or tools and their versions.
- Error Messages/Logs - Include any error messages, stack traces, or logs that are displayed when the issue occurs. Use code blocks or attach files if the logs are extensive.
---

# Git Essentials
## Issue Creation

- Screenshots or Screen Recordings - Visual aids can be extremely helpful in understanding the nature of the problem, especially for UI/UX related issues.
- Severity and Impact - Indicate how critical the issue is (e.g., blocking, critical, minor) and its impact on the software's functionality.
- Possible Solutions or Workarounds - If you're aware of any solutions or temporary workarounds for the issue, share them. This can be helpful for both maintainers and other users facing the same problem.
- Code Samples - If applicable, provide minimal code samples that can help in reproducing the issue. Use proper formatting or link to a gist or repo.
- Additional Context - Any other information that might be relevant, such as how often the issue occurs, whether it's sporadic or consistent, any patterns noticed, etc.
- Labels and Tags - If the repository has predefined labels (e.g., "bug", "enhancement", "documentation"), apply the relevant ones to your issue.
- Regression Information - Mention if the issue is a regression, i.e., a feature that used to work in a previous version but is broken in the current one. Indicate the last working version, if known.
- Providing comprehensive information when creating an issue not only helps maintainers diagnose and fix problems faster but also fosters a collaborative environment where community members can assist each other more effectively.
---

# Git Essentials
## Issue Formatting

- GitHub Issues support styling with Markdown.
- Can create checklists, headers, links, images, mention people/teams/issues/pull requests, quote code, create blocks, dropdowns, and more.
- [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
---

# Git Essentials
## Branch Linking

- By creating a branch that is directly linked to the issue, all progress on that issue is tracked.
- When a PR is approved, the issue is automatically closed.
---

# Git Essentials
## Activity #6

- Make your own repo on GitHub
- Create a pyproject.toml file.
---
---
layout: center
class: text-center
---
# Intermission

---
layout: center
class: text-center
---
# Lecture 4
## Organization and MVC

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
## Must Haves

- README File - Always have a README.md at the root. It should include:
  - Project title and brief description.
  - Installation and usage instructions.
  - Contribution guidelines.
  - Licensing information.
- License - Include a LICENSE file that clearly states the licensing terms.
- Badges - Use badges in the README.md to quickly display project status, such as build status, test coverage, and package version.
---

# Repository Organizational Strategies
## Must Haves

- Include a .gitignore - List files and directories that should be excluded from version control, such as compiled bytecode (*.pyc), virtual environment directories, IDE configuration files, etc.
- Requirements File - Use requirements.txt for specifying dependencies or consider using a pyproject.toml for more modern dependency management.
- docs - Use tools like Sphinx to generate documentation. Host it on platforms like Read the Docs for easy access.
- test - Write unit tests and possibly integrate coverage tools like coverage.py to ensure code quality.
- src - Code location.
---

# Repository Organizational Strategies
## Bonus Tools

- Code of Conduct - Include a CODE_OF_CONDUCT.md to set community standards and ensure a welcoming and inclusive environment.
- Changelog - Maintain a CHANGELOG.md to track and document all the changes made in the software over time.
- Issue and PR Templates - Use issue and PR templates to ensure consistency and completeness in submissions. This can be done with .github/ISSUE_TEMPLATE and .github/PULL_REQUEST_TEMPLATE directories.
- Security - Use tools like Dependabot to automatically check for vulnerabilities in dependencies and suggest updates.
- Contribution Guidelines - A CONTRIBUTING.md file detailing how others can contribute, the process for submitting pull requests, and any coding standards.
---

# Code Organizational Strategies
## Fighting Entropy

- Organizing code in Python is crucial for maintainability, scalability, and clarity.
---

# Code Organizational Strategies
## A Sisyphean Task

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
## The View

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

# Git Essentials
## Activity #7

- Upload individual files to GitHub
- Place code in appropriate organizational structure.
---
---
layout: center
class: text-center
---
# Intermission

---
layout: center
class: text-center
---
# Lecture 5
## CI/CD Fundamentals

# CI/CD Fundamentals
## Introduction to Python Software Development on GitHub

- Lyda Hill Department of Bioinformatics
- UT Southwestern Medical Center
- [https://about.codecov.io/blog/common-steps-in-a-complete-continuous-integration-workflow/](https://about.codecov.io/blog/common-steps-in-a-complete-continuous-integration-workflow/)
---

# What does CI/CD stand for?
## Continuous Integration

- Continuous Delivery
- Continuous Deployment
---


- [https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
---


- [https://deploybot.com/blog/continuous-development](https://deploybot.com/blog/continuous-development)
---

# Vocabulary
## Build
---

# Vocabulary
## Build – Convert source code files into a standalone software that anyone can run on their machine.

- Test
- Test – Evaluate and verify software can do what it is supposed to do.
---

# How do we know this function works?
---

# We check it with a unit test
---

# Test subgroups

- Acceptance test – A group of unit tests that ensure the software meets specifications e.g. of a contract.
- Smoke test – A group of unit tests that act as a sanity check for severe failures. If you run the software, does smoke come out of the computer?
---

# Vocabulary
## Build – Convert source code files into a standalone software that anyone can run on their machine.

- Test – Evaluate and verify software can do what it is supposed to do.
- Release
- Release – A build that is a new or upgraded version of the software.
- Deploy
- Deploy – Make the software available for use.
---

# The goal of CI/CD is to ensure developments do not stray far from the main branch

- [https://www.nobledesktop.com/learn/git/git-branches](https://www.nobledesktop.com/learn/git/git-branches)
- Main
- New Feature
- Bugfix
- v0
- v1
- v1.1
---

# Why is CI/CD useful?

- Ensures disparate parts of the code base work together throughout development, preventing integration challenges.
- Protects against release of broken software.
- Allows for fast feedback from users and fast fixes from developers.
---

# How do we implement CI/CD in practice?
## Version control (git)

- Automatic testing (pytest)
- Automatic building (setuptools, pyproject.toml)
- Automatic deployment (twine, PyPI)
---

# Additional CI/CD tools in the workflow
## Code quality (linter such as ruff, code formatter such as black)

- Test coverage check (codecov)
- Documentation (sphinx, numpydoc)
- Security checks (CodeQL)
---

# Local CI/CD workflows
## Can run some tools, such as the linter and code formatter, before pushing code to the repository

- Can automatically run some actions using pre-commit
---

# Running the CI/CD workflow
## Need a continuous integration tool

  - Bitbucket (https://bitbucket.org/product/features/pipelines)
  - Jenkins (https://jenkins.io)
  - AWS CodePipeline (https://aws.amazon.com/codepipeline)
  - CircleCI (https://circleci.com)
  - Azure (https://azure.microsoft.com/)
  - Gitlab (https://about.gitlab.com/)
  - GitHub (https://github.com/)
  - Etc.
- These tools use a YAML file (or similar) to describe a series of actions that make up a workflow.
---

# GitHub Actions Dashboard
---

# GitHub Actions Workflow Example

---
layout: center
class: text-center
---
# Lecture 6
## Code Quality and Linting

# Code Quality, Code Formatting, and Linting
---

# Outline
## Defining Clean Code

- Techniques to Maintain Clean Code
  - Code formatters and linting
- Utilizing pre-commit hooks to enforce coding standards and maintain code with Github.
- Exercise
---

# What is Clean Code?
## Readable - Code is read more often than it is written. It should be easy to understand.

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
## - Use descriptive, lowercase names – Variables should be meaningful and easy to understand.

  - ✅ max_users = 100  ❌ mu = 100
- - Use underscores for multi-word names (snake case) – Improves readability.
  - ✅ user_count = 10  ❌ userCount = 10 (CamelCase is for classes, not variables)
- - Avoid single-letter names (except for short loops) – Be explicit.
  - ✅ temperature_celsius = 25.0  ❌ t = 25.0
- - Constants should be uppercase with underscores – Used for values that don’t change.
  - ✅ MAX_RETRIES = 5  ❌ maxRetries = 5
- - Private variables start with an underscore – Signals internal use.
  - ✅ _cache = {}   ❌ cache = {} (unless public)
- - Avoid reserved keywords – Prevent conflicts with Python’s built-in functions.
  - ✅ class_name = "Intro to CI"    ❌ class = "Intro to CI" (conflicts with the class keyword)
---

# Functions Naming
## - Use lowercase with underscores – Improves readability and consistency.

  - ✅ def get_user_data():  ❌ def GetUserData(): (CamelCase is for classes)
- - Use descriptive names – Functions should clearly indicate their purpose.
  - ✅ def calculate_total_price():    ❌ def calc():
- - Use verbs for function names – Functions perform actions, so names should reflect that.
  - ✅ def fetch_records():    ❌ def records():
- - Use a leading underscore for internal or private functions – Signals intended internal use.
  - ✅ def _connect_to_db():    ❌ def connect_to_db(): (if meant to be private)
- - Avoid using built-in function names – Prevents accidental overrides.
  - ✅ def format_report():    ❌ def format(): (overrides Python’s built-in format function)
- - Use double leading underscores only for name-mangling in classes – Rarely needed.
  - ✅ class Example:  def __private_method(self): Double underscore automatically renamed within a class…
  - ❌ def __method(): (not necessary outside classes)
---

# Class Naming
## Use CapWords (PascalCase) – Each word starts with a capital letter, with no underscores.

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

- def process_large_dataset(data):
- """Processes a dataset and returns useful statistics."""
- Lines should not exceed 79 characters – Improves readability, especially in side-by-side comparisons.
- def process_large_dataset_with_very_long_name(data, additional_parameters, more_params):
- """This line is way too long and hard to read."""
---

# Line Formatting
## import os

- import sys
- x = 5
- y = 10
- print(x + y)
- Avoid multiple statements or imports on the same line
- Use separate lines for clarity.
- import os, sys  # Harder to modify later
- x = 5; y = 10; print(x + y)  # Harder to read
---

# In-line Comments
## comments should not contradict the code

- comments should be complete sentences
- comments should have a space after the # sign with the first word capitalized
- don’t litter commented code throughout your software.
---

# Documenting Code

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

- Define inner function inside function to call instead of defining inner function in each function call
- Improves modularity
---

# Methods to Improve Code Formatting
## Context Managers

- Manage how to interact with external databases and files.
- Automatically opens and closes files, avoiding complications when errors occur.
---

# Methods to Improve Code Formatting
## Iterators

- Use functions to iterate through variables
---

# Linting and Code Formatting

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

# Black: Automated Code formatting
## Black is an automated code formatter that is able to automatically format code to PEP8 standards
---

# Ruff: Automated Code Linting
## Identify unused variables and imports for removal.

- Style guides for code and whitespace organization
- 700 different rules
---

# Ruff: Automated Code Linting
## Removing unused variables and imports.
---

# Configuring Ruff
## 700 different rules

  - Naming
  - Pydocstyles
  - Pyupgrade
  - Flake8 rules
- Rules can be configured to specific styles or ignored to match the needs of your project
- [https://docs.astral.sh/ruff/configuration/](https://docs.astral.sh/ruff/configuration/)
---

# Configuring Ruff in IDE such as VSCODE

- Many IDEs such as vscode or pycharm have built in linters that identify smaller coding errors and improve code formatting
- Possible to install Ruff into vscode
- Linting is run when files are opened or saved
---

# Integrate Ruff or Black into github using pre-commit hooks
## A good way to format code is when committing code into Github

- Linters and formatters such as Ruff and Black can be integrated into Github
- Install pre-commit in conda environment using pip install pre-commit or integrate pre-commit dependence in pyproject.toml
- Add a pre-commit config file called .pre-commit-config.yaml to project
- In yaml file: add ruff repo
---

# Conclusions
## Code formatting and organizing is an important part coding

- Code formatters and linters such as ruff can be used to automatically format and detects formatting errors in code
- Linting can be implemented as a precommit hook and can be part of IDEs such as vscode or pycharm
- Clean code will lead to more understandable, reliable, and reproducible code.
---

# Exercise
## Set up Ruff locally in your environment.

- Set up a pre-commit hook to run Ruff and black and install it in pyproject.toml to format calculator codebase.
---

# Further Reading
## Ruff documentation: https://docs.astral.sh/ruff/

- Black documentation: https://black.readthedocs.io/en/stable/
- Linting in vscode: https://code.visualstudio.com/docs/python/linting
- Pre-commit documentation: https://pre-commit.com
---

# First Run Ruff Locally to identify errors
## Installing Ruff in your environment using

  - Pip install Ruff
- Once installed, go to folder where repo is located
- Go to src folder
- Type “ruff check .” In command line
---

# Setting up a Pre-commit
## First Install Pre-commit

  - pip install pre-commit
  - Add dependency in pyproject.toml (it should already be added)
- create .pre-commit-config.yaml file and add to repo
- In .pre-commit-config.yaml file
  - Add the following pre-commit information
---

# Editing .pre-commit-config.yaml file
## Configure .pre-commit-config.yaml file to use ruff

- Add ruff pre-commit to pre-commit.yaml file to include ruff
- Find information for other packages for pre-commits here:
  - [https://pre-commit.com/](https://pre-commit.com/)
  - [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html)
  - Push yaml file to repo on github
---

# Using pre-commit
## To install pre-commit hooks from configuration yaml file

  - pre-commit install
  - This install pre-commit hooks for each upcoming commit
- To run pre-commit hooks on current files, go to specific directory and run
  - Pre-commit run --all-files
- This will identify all errors
  - We can autofix errors by specifying autofix.

---
layout: center
class: text-center
---
# Lecture 7
## Unit Testing and TDD

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

---
layout: center
class: text-center
---
# Lecture 8
## GitHub Actions

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

---
layout: center
class: text-center
---
# Lecture 9
## Public-Facing Documentation

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
