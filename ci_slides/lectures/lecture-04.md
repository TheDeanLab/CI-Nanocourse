---
layout: image-right
image: /images/lecture-04/t01_from_s01.png
backgroundSize: contain
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
---
layout: image-right
image: /images/lecture-04/t02_from_s02.png
backgroundSize: contain
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
---
layout: image-right
image: /images/lecture-04/t03_from_s03.png
backgroundSize: contain
---
# Repository Organizational Strategies
## Must Haves

- Include a .gitignore - List files and directories that should be excluded from version control, such as compiled bytecode (*.pyc), virtual environment directories, IDE configuration files, etc.
- Requirements File - Use requirements.txt for specifying dependencies or consider using a pyproject.toml for more modern dependency management.
- docs - Use tools like Sphinx to generate documentation. Host it on platforms like Read the Docs for easy access.
- test - Write unit tests and possibly integrate coverage tools like coverage.py to ensure code quality.
- src - Code location.
---
---
layout: image-right
image: /images/lecture-04/t04_from_s04.png
backgroundSize: contain
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
