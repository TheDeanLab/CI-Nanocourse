# **Collaborative Git & GitHub Activity: Organizing and Packaging PyCalc**

## **📝 Overview**

In this activity, students will collaborate in groups of four to practice using **Git, GitHub, pull requests, bug fixing, and Python packaging**. Each group will work on a **central GitHub repository** to properly organize and package the **PyCalc** project, ensuring it can be installed using `pip install -e .`.

This activity will simulate a real-world software development workflow, where multiple developers work on the same project using version control and pull requests.

---

## **🎯 Learning Objectives**

By the end of this activity, students will:

- Understand how to **clone** a repository and work in a **collaborative Git workflow**.
- Learn how to **add and commit files**, **push to GitHub**, and **merge contributions via pull requests**.
- Properly **structure a Python project** to work with `pyproject.toml` and `setuptools`.
- Successfully **install and run** the `pycalc` package using `pip install -e .`.

---

## **🛠️ Activity Setup**

### **1️⃣ Student 1 Creates the Central GitHub Repository**

- Assemble into groups of 4.
- Student 1 [creates a new Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) for the group called **Calculator Exercise.**

### **2️⃣ Students 2-3 Clone the Repository Using GitHub Desktop**

1. Open **GitHub Desktop**.
2. Click **File > Clone Repository**.
3. Select the repository from the list or enter its URL.
4. Choose a local path and click **Clone**.

---

## **📂 File Distribution & Aggregation**

Each student downloads their **ZIP** file from: 🔗 [Files for Students](https://github.com/TheDeanLab/CI2023/tree/main/calculator-exercise/Files%20for%20Students)

Unzip the files somewhere locally on your machine.

The idea is that each of you has some portion of the project completed locally and you are going to push it to the project Repo.

Each student should:

1. **Download and move** their assigned files into the cloned Repo. You can put them in the same folder as the **README.md** that you are reading here.
2. **Create a new branch** in GitHub Desktop:
   - Click **Current Branch > New Branch**.
   - Name the branch based on the feature (e.g., `push-files`).
3. **Commit and push changes**:
   - Click **Changes**, add a descriptive commit message, and commit.
   - Click **Push Origin** to upload the branch to GitHub.
4. **Open a pull request (PR) on GitHub** to merge their files into `main`.

---

## **📦 Restructuring the Project for Packaging**

After all files are in the central repo, students must individually attempt to restructure the package **without modifying the source code**.

### **🔄 Steps for Restructuring the Repository**

1. **Each student creates their own restructuring attempt** by making a new branch in GitHub Desktop:
   - Click **Current Branch > New Branch**.
   - Name it `restructure-<studentname>` (e.g., `restructure-alex`).
2. Each student should organize the files in a way that ensures `pycalc` can be installed using `pip install -e .`.
3. **Commit and push their restructuring attempt** in GitHub Desktop:
   - Click **Changes**, add a descriptive commit message, and commit.
   - Click **Push Origin**.
4. **One student will switch between the restructuring branches** in GitHub Desktop and attempt to install `pycalc` on each version:
   - Click **Current Branch**, select a `restructure-<studentname>` branch.
   - Run:
     ```sh
     pip install -e .[dev]
     ```
5. If a student's structure successfully installs the package, the group will choose that version to merge into `main`.
6. Open a pull request for the selected structure and merge it into `main`.

---

## **⚙️ Installing & Testing the Package**

Once the repository is correctly structured and merged into `main`:

1. **Install the package in editable mode:**
   ```sh
   pip install -e .[dev]
   ```
2. **Verify installation:**
   ```sh
   python -c "import pycalc; print(pycalc)"
   ```
3. **Run tests using **``:
   ```sh
   pytest
   ```

---

## **🔍 Debugging & Bug Fixing**

If any issues arise, students should:

1. Use **GitHub Desktop > History** to check commit history.
2. Use **GitHub Pull Requests** to track changes before merging.
3. Open an **Issue on GitHub** and assign team members to debug.
4. If an error occurs (e.g., `ModuleNotFoundError`), reinstall:
   ```sh
   pip uninstall pycalc
   pip install -e .[dev]
   ```

---

## **📌 Submission & Reflection**

### **Final Deliverables:**

✅ The fully structured GitHub repository with all files correctly organized.\
✅ A working installation of `pycalc` using `pip install -e .`.\
✅ Successful test execution with `pytest`.

Each group should submit their **GitHub repository link** and a brief **reflection** answering:

1. What challenges did you encounter during collaboration?
2. What did you learn about GitHub workflows?
3. How did restructuring the package impact the ability to install and test the project?

---

## **🎉 Conclusion**

This activity reinforces real-world GitHub workflows, collaborative version control, and Python packaging concepts. By working together to structure and package PyCalc, students gain hands-on experience with:

- **Cloning, branching, committing, and pushing code using GitHub Desktop**.
- **Pull requests and merging collaborative contributions**.
- **Debugging issues related to Python packaging and imports**.
- **Testing code using **``** in a structured Python project**.

🚀 **Great work! Now you have experience working on a real-world collaborative software project!**

