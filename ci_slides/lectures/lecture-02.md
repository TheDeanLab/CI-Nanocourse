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
