# Python Project Template 
A Python project template that comes out of the box with configuration for:
- Packaging and dependency management using [Poetry](https://python-poetry.org)
- Command Line Interface (CLI) using [click](https://click.palletsprojects.com)
- Testing using [pytest](https://pytest.org)
- Code coverage using [coverage](https://coverage.readthedocs.io)
- Fomatting using [black](https://black.readthedocs.io) 
- Import sorting using [isort](https://pycqa.github.io/isort)
- Linting usig [flake8](https://flake8.pycqa.org)
- Pre-commit validations using [pre-commit](https://pre-commit.com)
- Workflow automation using [GitHub Actions](https://github.com/features/actions)
- Automated dependency update using [Dependabot](https://docs.github.com/en/code-security/dependabot)
- Dockerized development environment using [Dev containers](https://code.visualstudio.com/docs/devcontainers/containers)

## How to use
Click this button to create a new repository for your project, then clone the new repository. Enjoy!

[![Use this template]( https://img.shields.io/badge/Use%20this%20template-238636?style=for-the-badge)](https://github.com/amrabed/python/generate)

### Rename the project
After cloning the repository, rename the project by running:
```bash
make rename NAME="" DESCRIPTION="" AUTHOR="" EMAIL="" GITHUB=""
```
Pass the following parameters:

Parameter | Description
--- | ---
`NAME` | Project new name
`DESCRIPTION` | Project short description
`AUTHOR` | Author name
`EMAIL`| Author email 
`GITHUB`| GitHub username (for GitHub funding)


## Prerequisites
### Dev container
- Docker

### Local environment
- Python 3.12+ (You can update the [`pyproject.toml`](pyproject.toml#L35) for lower versions)
- Pipx (*optional* - used to install Poetry if not already installed)

## Setup

### Install Poetry
To install poetry, if not installed (requires pipx), run:
```bash
make poetry
```

### Install / Update dependencies
To install the project dependencies defined in the [pyproject.toml](pyproject.toml) file, run:
```bash
make install
```

To update the project dependencies, run:
```bash
make update
```

### Install pre-commit hooks
To install the pre-commit hooks for the project to format and lint your code automatically before commiting, run: 
```bash
make precommit
```

### Activate virtual environemnt
To activate the virtual environment, run:
```bash
make venv
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

## Running the project
A Poetry script, with the name `app`, is defined in the [pyproject.toml](pyproject.toml#L32) file, to let you to run the project as a shell command.

> Make sre to activate the virtual environment using `make venv` to be able to run `app` without `poetry run`

Try running `app -h` or `app --help` to get the help message of your app:
```bash
Usage: app [OPTIONS]

  Say hello

Options:
  -n, --name TEXT  Name  [default: World]
  -h, --help       Show this message and exit.
```


## Project Structure

```
├── .devcontainer            # Dev container files
│   ├── devcontainer.json    # Dev container confgiuration
│   └── Dockerfile           # Dev container Dockerfile
├── .github                  # Github files
│   ├── dependabot.yaml      # Dependabot configuration
│   ├── FUNDING.md           # GitHub funding
│   └── workflows            # Github Actions Workflows
│       └── check.yml        # Workflow to validate code on push
├── .gitignore               # Git-ignored file list
├── .pre-commit-config.yaml  # Pre-commit configuration file
├── .flake8                  # flake8 configuration file
├── .vscode                  # VS code files
│   └── settings.json        # VS code settings
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