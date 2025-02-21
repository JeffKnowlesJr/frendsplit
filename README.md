# FrendSplit - Expense Sharing App

FrendSplit helps groups of friends manage shared expenses, track balances, and settle payments efficiently. This application is built using Django and aims to provide a user-friendly experience for managing shared finances.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4.  [Project Structure](#project-structure)
5.  [Data Models](#data-models)
6.  [Development](#development)
    - [Current Focus](#current-focus)
    - [Future Enhancements](#future-enhancements)
7.  [Contributing](#contributing)
8.  [License](#license)
9.  [Development Log](#development-log)
10. [Contact](#contact)

## Introduction

A Django application for splitting expenses among friends. FrendSplit is a Django-based application designed to streamline expense sharing among friends. It offers features for group management, detailed expense tracking with multiple splitting options, and a settlement system to efficiently manage payments. The application is currently in early development, focusing on core functionality such as user authentication, group management, and settlement calculations. Future enhancements include support for multiple currencies, a user-friendly web interface, and mobile app development. The project is open for internal contributions, following the guidelines outlined in the documentation.

## Features

- **Group Management**
  - Create and manage expense-sharing groups.
  - Add/remove group members.
  - Track group-specific expenses and settlements.
- **Expense Tracking**
  - Record expenses with multiple splitting options:
    - Equal split
    - Exact amounts
    - Percentage-based split
  - Track who paid and who owes.
  - Maintain expense history.
- **Settlement System**
  - Calculate optimal settlement paths.
  - Track pending and completed settlements.
  - View settlement history.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd FrendSplit
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    - Windows: `venv\Scripts\activate`
    - Unix/MacOS: `source venv/bin/activate`
4.  Install dependencies:
    ```bash
    pip install django
    ```
5.  Run migrations:
    ```bash
    python manage.py migrate
    ```
6.  Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7.  Start the development server:

    ```bash
    python manage.py runserver
    ```

    You can then access the application in your web browser at `http://127.0.0.1:8000/`.

## Project Structure

FrendSplit/
├── mysite/ # Main project configuration
│ ├── settings.py # Django settings
│ ├── urls.py # Main URL routing
│ └── wsgi.py # WSGI configuration
├── frendsplitapp/ # Main application code
│ ├── models.py # Database models
│ ├── views.py # View logic
│ ├── admin.py # Django admin interface customization
│ └── urls.py # Application URL routing
├── venv/ # Virtual environment (not tracked in Git)
├── manage.py # Django management script
└── README.md # Project documentation

- `mysite/` - Main project configuration
  - Contains Django settings, main URL routing, and WSGI/ASGI configurations.
- `frendsplitapp/` - Main application code
  - `models.py` - Database models for groups, expenses, and settlements.
  - `views.py` - View logic and request handling.
  - `admin.py` - Django admin interface customization.
  - `urls.py` - Application URL routing.

## Data Models

### Group

- Represents a collection of friends who share expenses.
- Tracks group members and creation details.

  ```python
  class Group(models.Model):
      name = models.CharField(max_length=200)
      members = models.ManyToManyField(User, related_name='frendsplit_groups')
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.name
  ```

### Expense

- Records individual expenses within groups.
- Supports multiple splitting methods (equal, exact, percentage).
- Links to detailed split information.

  ```python
  class Expense(models.Model):
      group = models.ForeignKey(Group, on_delete=models.CASCADE)
      payer = models.ForeignKey(User, on_delete=models.CASCADE)
      description = models.CharField(max_length=200)
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.description
  ```

### ExpenseSplit

- Tracks individual shares of expenses.
- Records payment status for each participant.

  ```python
  class ExpenseSplit(models.Model):
      expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      paid = models.BooleanField(default=False)

      def __str__(self):
          return f"{self.user.username} - {self.expense.description}"
  ```

### Settlement

- Manages payment settlements between users.
- Tracks completed and pending settlements.

  ```python
  class Settlement(models.Model):
      payer = models.ForeignKey(User, related_name='settlements_paid', on_delete=models.CASCADE)
      receiver = models.ForeignKey(User, related_name='settlements_received', on_delete=models.CASCADE)
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      completed = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return f"{self.payer.username} -> {self.receiver.username}: {self.amount}"
  ```

## Development

### Current Focus

- Core expense tracking functionality.
- User authentication and authorization.
- Group management features.
- Settlement calculation algorithms.

### Future Enhancements

- Implement more sophisticated settlement algorithms to minimize the number of transactions.
- Add support for different currencies.
- Develop a user-friendly web interface using modern front-end frameworks.
- Implement email notifications for new expenses and settlements.
- Explore mobile app development using React Native or other cross-platform frameworks.

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear, concise commit messages.
4.  Submit a pull request with a detailed description of your changes.

## License

MIT License

## Development Log

### 2024-03-17

- Fix URL and model conflicts
  - Remove duplicate admin URL from `frendsplitapp/urls.py` to resolve namespace conflict
  - Change `Group.members` `related_name` from 'groups' to 'frendsplit_groups' to avoid collision with Django's built-in `User.groups` field

### 2024-03-18

- Model Updates
  - Add `created_by` field to Group model
  - Update model documentation in README
  - Add list filters to admin interface for better data management
- Documentation
  - Update project structure documentation to include all files
  - Sync model documentation with actual implementation

## Contact

For questions, suggestions, or contributions, please contact the project maintainers:

- Frensplit LLC
- hello@frensplit.link
