# Python Project Template 
A Python project template that comes out of the box with configuration for:
- Packaging and dependency management using [Poetry](https://python-poetry.org)
- Testing using [pytest](https://pytest.org)
- Code coverage using [coverage](https://coverage.readthedocs.io)
- Fomatting using [black](https://black.readthedocs.io) 
- Import sorting using [isort](https://pycqa.github.io/isort)
- Linting usig [flake8](https://flake8.pycqa.org)
- Pre-commit validations using [pre-commit](https://pre-commit.com)
- Workflow automation using [GitHub Actions](https://github.com/features/actions)

## How to use
Click this button to create a new repository for your project, then clone the new repository. Enjoy!

[![Use this template]( https://img.shields.io/badge/Use%20this%20template-238636?style=for-the-badge)](https://github.com/amrabed/python/generate)


## Prerequisites
- Python 3.12+ (You can update the [`pyproject.toml`](pyproject.toml#L35) for lower versions)
- Pipx (*optional* - used to install Poetry if not already installed)

## Make commands

### Install Poetry
To install poetry if not installed (requires pipx), run:
```bash
make poetry
```

### Install dependencies
To install the project dependencies defined in the [pyproject.toml](pyproject.toml) file, run:
```bash
make install
```

### Install pre-commit hooks
To install the pre-commit hooks for the project to format and lint your code automatically before commiting, run: 
```bash
make precommit
```

### Format and Lint code
To format and lint project code, run:
```bash
make lint
```

### Run tests with coverage
To run the unit tests defined under the [tests](tests) folder and show coverage report, run:
```bash
make test
```

### Run main script
To run the main `app` script (defined in the [pyproject.toml](pyproject.toml#L32) file to run the main function as a shell script), run:
```bash
make run
```


## Project Structure

```
├── .github                  # Github files
│   ├── FUNDING.md           # GitHub funding
│   └── workflows            # Github Actions Workflows
│       └── check.yml        # Workflow to validate code on push
├── .gitignore               # Git-ignored file list
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