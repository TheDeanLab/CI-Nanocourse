<!-- lecture-03 -->
---
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
layout: center
class: text-center
---
# Intermission
