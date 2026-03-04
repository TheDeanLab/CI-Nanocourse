
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

# Verifying Your Git Installation
## Confirm Git is working on your system

- Open a **terminal** (or **Git Bash** on Windows).

- Check that Git is installed:

```bash
git --version
```

- Expected output will look something like: `git version 2.43.0`

- If the command returns a version number, Git is correctly installed. 
- If the command returns “git: command not found” (or similar): 
  - Git is not installed or not on your system PATH. 
  - Reinstall Git or restart your terminal after installation.
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

- **Branch:** Lightweight movable pointer that points to a specific commit. It represents an independent line of development, allowing you to isolate work on different features, bug fixes, or experiments without affecting the main or other branches.

- **Parallel development**: multiple features or fixes can be developed simultaneously in isolation.

- **Main Branch:** By default, every Git repository starts with a branch called "master" or "main". This is the primary branch where stable, production-ready code resides.

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

- [https://git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch)

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
## GitHub Desktop


- GUI is easier for Git beginners.

- Visual history and branch view.

- Click-based merge conflict support.

- Simple staging and commit workflow.

- **[https://desktop.github.com/](https://desktop.github.com/)**

---

# Basic Git Workflows
## Activity #1

- Create a GitHub account

- Download GitHub Desktop

- Clone the class repo: **https://github.com/TheDeanLab/CI-Nanocourse**

- *Using Git command-line:* create a branch, and switch between main and the branch you created.

- Do the same with *GitHub Desktop*
