
poetry:  # Install Poetry
	pipx install -qf poetry

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
	poetry run flake8 .

coverage:
	poetry run coverage run -m pytest .
	poetry run coverage report -m
	poetry run coverage xml

test: coverage

all: poetry venv install precommit lint test