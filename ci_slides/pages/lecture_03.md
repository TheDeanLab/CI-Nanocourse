
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

---

# Git Essentials
## Activity #6

- Make your own repo on GitHub and clone it locally.

- Create a `pyproject.toml` file.

```bash
[project]
name = "ci-nanocourse-demo"
version = "0.1.0"
description = "Demo project for CI nanocourse"
authors = [{name = "Your Name"}]
requires-python = ">=3.9"
dependencies = []
```

- Push the file to GitHub.
```bash
git add pyproject.toml
git commit -m "Add project metadata"
git push
```