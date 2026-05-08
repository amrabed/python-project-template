.DEFAULT_GOAL := help

NAME ?= project
DESCRIPTION ?= Python Project Template
AUTHOR ?= Amr Abed
EMAIL ?= amrabed
GITHUB ?= amrabed

.PHONY: help
help: # Show help
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: project
project: # Rename project (run once)
	@python3 project_init.py '$(subst ','\'',$(NAME))' '$(subst ','\'',$(DESCRIPTION))' '$(subst ','\'',$(AUTHOR))' '$(subst ','\'',$(EMAIL))' '$(subst ','\'',$(GITHUB))'

uv:  # Install uv
	pipx install -f uv

venv:  # Create and activate virtual environment and install dependencies
	uv sync

install: venv # Install dependencies and project

update: # Update dependencies
	uv lock --upgrade

precommit: # Install pre-commit hooks
	uv run pre-commit autoupdate
	uv run pre-commit install

pre-commit: precommit

lint: # Lint code
	uv run ruff check --fix
	uv run ruff format
	uv run pyright

coverage:
	uv run coverage run -m pytest .
	uv run coverage report -m
	uv run coverage xml

test: coverage

.PHONY: docs
docs: # Build and deploy documentation to GitHub pages
	uv run mkdocs gh-deploy --force

local: # Serve documentation on a local server
	uv run mkdocs serve

all: install lint test
