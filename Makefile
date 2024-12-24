
NAME ?= project
DESCRIPTION ?= Python Project Template
AUTHOR ?= Amr Abed
EMAIL ?= amrabed
GITHUB ?= amrabed

rename: # Rename project (run once)
	@if [ -d project ]; then mv project ${NAME}; fi
	@sed -i '' 's/^source = \[.*\]/source = \["${NAME}"\]/' pyproject.toml
	@sed -i '' 's/^app = "project\.app:main"/app = "${NAME}\.app:main"/' pyproject.toml
	@sed -i '' 's/^name = ".*"/name = "${NAME}"/' pyproject.toml
	@sed -i '' 's/^description = ".*"/description = "${DESCRIPTION}"/' pyproject.toml
	@sed -i '' 's/^authors = \[.*\]/authors = \["${AUTHOR} <${EMAIL}>"\]/' pyproject.toml
	@sed -i '' 's/^# .*/# ${DESCRIPTION}/' README.md
	@sed -i '' 's/^github: \[.*\]/github: \[${GITHUB}\]/' .github/FUNDING.yml
	@sed -i '' 's/^patreon: .*/patreon: # Put your Patreon username here/' .github/FUNDING.yml

poetry:  # Install Poetry
	pipx install -f poetry

venv:
	poetry shell

install: # Install dependencies and project
	poetry install

update: # Update dependencies
	poetry update

precommit: # Install pre-commit hooks
	poetry run pre-commit autoupdate
	poetry run pre-commit install

pre-commit: precommit

lint:
	poetry run black .
	poetry run isort .
	poetry run pyright .
	poetry run flake8 .

coverage:
	poetry run coverage run -m pytest .
	poetry run coverage report -m
	poetry run coverage xml

test: coverage

all: poetry install precommit lint test venv