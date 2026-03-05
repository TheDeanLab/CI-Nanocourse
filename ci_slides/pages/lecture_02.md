
---
layout: center
class: text-center
---

# Lecture 2
## Environment Management

---

# Environment Management with Anaconda
## Creating Reproducible Development Environments


- An **environment** is like a sandbox, ensuring that the software setup for one project doesn't interfere with another and providing a stable and reproducible development space.

- **Version Inconsistencies:** Python libraries and tools are constantly evolving. Different projects might require different versions of the same library, leading to potential conflicts and unexpected behavior.

- **System-wide Installation Risks:** Installing libraries system-wide can lead to "dependency hell", where upgrades for one project break another.

- **Reproducibility:** Consistent environment setups ensure that peers can reproduce your published results regardless of their machine.

- **Ease of Sharing:** With a well-managed environment, developers can easily share their projects, ensuring that others can run their code.

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

### 1. Install **[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)**

### 2. Confirm `conda` is installed

Open a terminal and run:

```bash
conda --version
```

Expected output will look similar to: 

```text
conda 24.x.x
```

If this fails, restart your terminal and ensure Miniconda was added to your PATH during installation.

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

#### NOTE: You can run python in a one-liner using `-c` flag: `python -c "print('hello world')"`

#### Check version using `python --version`

---

# Environment Management with Anaconda
## What is a Package?

- **Software Collection:** A package in Anaconda is a bundled collection of software tools, libraries, and dependencies that function together to achieve a specific task or set of tasks.

- **Version Management:** Each package has specific versioning, allowing users to install, update, or rollback to particular versions as needed, ensuring compatibility and stability in projects.

- **Dependency Handling:** When a package is installed in Anaconda, the system automatically manages and installs any required dependencies, ensuring seamless functionality and reducing manual setup efforts.

---


# Environment Management with Anaconda
## Creating new Environment

There are multiple ways to create a new environment. These include: 
- From a text file (e.g. `requirements.txt`)
- From a YAML file (e.g. `environment.yml`)
- From a `pyproject.toml` file (e.g. `pyproject.toml`)

The most modern and recommended approach is to use a `pyproject.toml` file.

---
layout: image-right
image: /images/lecture-02/s10_img01.png
backgroundSize: contain
---

# Environment Management with Anaconda
## Creating an Environment from a Text File


- Each package, and all of its dependencies, explicitly imported from a package manager (pip, conda, etc.)

- Version Control (e.g. `pyserial==3.5`) and platform control (e.g. `sys_platform == “darwin”`)
- Install dependencies from a text file: `conda create --name <environment_name> --file requirements.txt`


---

# Environment Management with Anaconda
## What is a YAML File?

- `.yaml` or `.yml` --> Balance between structure and readability.

- **Human-Readable Format:** Designed to be easily readable by humans and is often used for configuration files.

- **Hierarchical Structure:** Uses indentation to represent hierarchical data structures, such as lists and dictionaries.

- **Key-Value Pairs:** Data is typically represented using key-value pairs, making it similar to Python dictionaries.

- **Multiline Strings:** Supports multiline strings, making it convenient to represent longer text.

- **Comments:** Supports comments using the # symbol, allowing for annotations within the file.

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


- Create a new environment from a YAML file
  - `conda create --name EnvironmentName file=package_contents.yml`
- Create a new environment from a text file
  - `conda create --name EnvironmentName file=package_contents.txt`
- Create a new environment from a pyproject.toml file
  - `conda create --name EnvironmentName`
  - `pip install -e .`

---

# Advanced Environment Management
## Activity #4

- Make sure `ci_nanocourse` (or whatever you called it) is *activated*

- Evaluate the .txt, .yaml, and .toml files in the repository.

- Try to import Numpy: `python -c "import numpy"`... What happens?

- Install the required dependencies for the CI-Nanocourse repository using the pyproject.toml file. <br> ***Make sure you are in the right directory!***

- Confirm that the installation is correct and that the dependencies can be imported upon launching python. <br> Can you `import numpy` now?

---

# Environment Management with Anaconda
## Environment Tips and Tricks


- Don’t mix and match Package Managers (`pip` vs `conda`).

- Be judicious with your dependencies.

- Be explicit with your dependencies.


---
# Advanced Environment Management
## Activity #5

- Add Seaborn to your `pyproject.toml` file - **https://pypi.org/project/seaborn/**

- Reinstall your local package

- Confirm that seaborn was included in the installation

- Launch python, import seaborn, and if time permits, plot something with seaborn.

- Install the docs optional dependencies.