.DEFAULT_GOAL := help

NAME ?= project
DESCRIPTION ?= Python Project Template
AUTHOR ?= Amr Abed
EMAIL ?= amrabed
GITHUB ?= amrabed
SOURCE ?= $(shell echo ${NAME} | tr '-' '_' | tr '[:upper:]' '[:lower:]')

.PHONY: help
help: # Show help
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: project
project: # Rename project (run once)
	@if [ -d project ]; then mv project ${SOURCE}; fi
	@sed -i '' 's/^::: project\.app/::: ${SOURCE}\.app/' docs/reference/app.md
	@sed -i '' 's/^repo_name: .*/repo_name: ${GITHUB}\/${NAME}/' mkdocs.yml
	@sed -i '' 's/^repo_url: .*/repo_url: https:\/\/github.com\/${GITHUB}\/${NAME}/' mkdocs.yml
	@sed -i '' 's/^source = \[.*\]/source = \["${SOURCE}"\]/' pyproject.toml
	@sed -i '' 's/^app = "project\.app:main"/app = "${SOURCE}\.app:main"/' pyproject.toml
	@sed -i '' 's/^name = ".*"/name = "${SOURCE}"/' pyproject.toml
	@sed -i '' 's/^description = ".*"/description = "${DESCRIPTION}"/' pyproject.toml
	@sed -i '' 's/^authors = \[.*\]/authors = \["${AUTHOR} <${EMAIL}>"\]/' pyproject.toml
	@sed -i '' 's/^# .*/# ${DESCRIPTION}/' docs/README.md
	@sed -i '' 's/@.*/@${GITHUB}/' .github/CODEOWNERS
	@sed -i '' 's/^github: \[.*\]/github: \[${GITHUB}\]/' .github/FUNDING.yml

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
