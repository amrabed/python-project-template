import os
import re
import shutil
from pathlib import Path

from click import ClickException, UsageError, command, echo, option


@command()
@option("--name", required=True, help="Project new name")
@option("--description", required=True, help="Project short description")
@option("--author", required=True, help="Author name")
@option("--email", required=True, help="Author email")
@option("--github", required=True, help="GitHub username")
def main(name: str, description: str, author: str, email: str, github: str):
    # Validate name to prevent directory traversal or other injection
    if not re.match(r"^[a-zA-Z0-9_-]+$", name):
        raise UsageError(
            f"Invalid project name '{name}'. Only alphanumeric characters, dashes, and underscores are allowed."
        )

    source = name.replace("-", "_").lower()

    echo(f"Initializing project '{name}' (source: '{source}')...")

    # 1. Rename project directory
    if os.path.isdir("project"):
        shutil.move("project", source)
    elif not os.path.isdir(source):
        raise ClickException(f"Error: Neither 'project' nor '{source}' directory found.")

    # 2. File modifications
    replacements = [
        ("docs/reference/app.md", r"^::: project\.app", f"::: {source}.app"),
        ("mkdocs.yml", r"^repo_name: .*", f"repo_name: {github}/{name}"),
        ("mkdocs.yml", r"^repo_url: .*", f"repo_url: https://github.com/{github}/{name}"),
        ("pyproject.toml", r"^source = \[.*\]", f'source = ["{source}"]'),
        ("pyproject.toml", r'^app = "project\.app:main"', f'app = "{source}.app:main"'),
        ("pyproject.toml", r'^name = ".*"', f'name = "{source}"'),
        ("pyproject.toml", r'^description = ".*"', f'description = "{description}"'),
        ("pyproject.toml", r"^authors = \[.*\]", f'authors = ["{author} <{email}>"]'),
        ("docs/README.md", r"^# .*", f"# {description}"),
        (".github/CODEOWNERS", r"@.*", f"@{github}"),
        (".github/FUNDING.yml", r"^github: \[.*\]", f"github: [{github}]"),
    ]

    for filepath, pattern, replacement in replacements:
        path = Path(filepath)
        if not path.exists():
            echo(f"Warning: File {filepath} not found, skipping.")
            continue

        content = path.read_text()
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        path.write_text(new_content)
        echo(f"Updated {filepath}")

    echo("Project initialization complete.")


if __name__ == "__main__":
    main()
