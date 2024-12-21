# Python Project Template
A Python Project template that comes out of the box with configuration for:
- Packaging and dependency management using [Poetry](https://python-poetry.org)
- Testing using [pytest](https://pytest.org)
- Code coverage using [coverage](https://coverage.readthedocs.io)
- Fomatting using [black](https://black.readthedocs.io) 
- Import sorting using [isort](https://pycqa.github.io/isort)
- Linting usig [flake8](https://flake8.pycqa.org)
- Pre-commit validations using [pre-commit](https://pre-commit.com)
- Workflow automation using [GitHub Actions](https://github.com/features/actions)

## Prerquisites
- Python 3.12+ (You can update the [`pyproject.toml`](pyproject.toml#L17) for lower versions)
- Pipx (*optional* - used to install Poetry if not already installed)

## Usage
- Click the **Use the template** button to use this template to create your Python project
- Clone your newly created project to your local

### Install Poetry
Run `make poetry` to install poetry if not installed (requires pipx)

### Install dependencies
Run `make install` to install the project dependencies defined in the [pyproject.toml](pyproject.toml) file

### Install pre-commit hook
Run `make precommit` to install the pre-commit hook for the project to format and lint your code automatically before commiting to GitHub

### Format and Lint code
Run `make lint` to format and lint project code

### Run tests with coverage
Run `make test` to run the tests defined under the [tests](tests) folder and show coverage report

### Run main script
A script with the name `app` is defined in the [pyproject.toml](pyproject.toml#L14) file to run the main function as a shell script. 
Run `make run` to run the main script

## Project Structure

```
├── .github                  # Github files
│   ├── FUNDING.md           # GitHub funding
│   └── workflows            # Github Actions Workflows
│       └── check.yml        # Workflow to validate code on push
├── .gitignore               # Git-ignored file list (duh)
├── .pre-commit-config.yaml  # Pre-commit configuration file
├── LICENSE                  # Project license
├── Makefile                 # Make commands
├── README.md                # Read-me file
├── pyproject.toml           # Configuration file for different tools
├── project                  # Main project folder
│   ├── __init__.py          # Init file of the main package
│   └── app.py               # Main Python file of the project
└── tests                    # Unit tests for the project
    ├── conftest.py          # Pytest configuration, and fixtures, and hooks
    ├── __init__.py          # Init file fo the test package
    └── test_app.py          # Sample test file
```