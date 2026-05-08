import os
import re
import shutil
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 6:
        print("Usage: python3 project_init.py <NAME> <DESCRIPTION> <AUTHOR> <EMAIL> <GITHUB>")
        sys.exit(1)

    name = sys.argv[1]
    description = sys.argv[2]
    author = sys.argv[3]
    email = sys.argv[4]
    github = sys.argv[5]

    # Validate name to prevent directory traversal or other injection
    if not re.match(r"^[a-zA-Z0-9_-]+$", name):
        print(
            f"Error: Invalid project name '{name}'. Only alphanumeric characters, dashes, and underscores are allowed."
        )
        sys.exit(1)

    source = name.replace("-", "_").lower()

    print(f"Initializing project '{name}' (source: '{source}')...")

    # 1. Rename project directory
    if os.path.isdir("project"):
        shutil.move("project", source)
    elif not os.path.isdir(source):
        print(f"Error: Neither 'project' nor '{source}' directory found.")
        sys.exit(1)

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
            print(f"Warning: File {filepath} not found, skipping.")
            continue

        content = path.read_text()
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        path.write_text(new_content)
        print(f"Updated {filepath}")

    print("Project initialization complete.")


if __name__ == "__main__":
    main()
