
SOURCE ?= project

poetry:  # Install Poetry
	pipx install -qf poetry

install: # Install dependencies and project
	poetry install

update: # Update dependencies
	poetry update

precommit: # Install pre-commit hooks
	poetry run pre-commit autoupdate
	poetry run pre-commit install

lint:
	poetry run black .
	poetry run isort .
	poetry run flake8 .

coverage:
	poetry run coverage run -m pytest .
	poetry run coverage report -m
	poetry run coverage xml

test: coverage

run:
	poetry run app