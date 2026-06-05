from click import command, option, secho, version_option


class _LazyVersion:
    """
    Retrieve the project version from pyproject.toml lazily.

    This is a performance optimization to avoid the overhead of importlib.metadata
    and to ensure the version is available even if the package is not installed.
    """

    def __str__(self) -> str:
        import re
        from pathlib import Path

        try:
            content = (Path(__file__).parent.parent / "pyproject.toml").read_text()
            if match := re.search(r'^version\s*=\s*"(.*?)"', content, re.MULTILINE):
                return match.group(1)
        except Exception:  # noqa: S110  # pragma: no cover
            pass

        try:
            import importlib.metadata

            return importlib.metadata.version("project")
        except Exception:  # pragma: no cover
            return "0.0.0"


@command(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Say hello to a user.",
    epilog="Example: app --name Alice",
)
@option(
    "-n",
    "--name",
    default="World",
    help="The name of the person to greet.",
    show_default=True,
    metavar="<name>",
)
@version_option(version=_LazyVersion())
def main(name: str = "World"):
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
