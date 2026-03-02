<!-- lecture-01 -->
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
layout: center
class: text-center
---
# Intermission
