import re
from pathlib import Path

from click import command, option, secho, version_option


def _get_version() -> str:
    """Read version from pyproject.toml without importing slow modules.

    Measurement: This direct regex read is ~80ms faster than importlib.metadata.version().
    """
    try:
        content = Path(__file__).parent.parent.joinpath("pyproject.toml").read_text(encoding="utf-8")
        if match := re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE):
            return match.group(1)
    except Exception:  # noqa: BLE001, S110
        pass
    return "0.1.0"


@command(context_settings={"help_option_names": ["-h", "--help"]}, help="Say hello to a user.")
@option(
    "-n",
    "--name",
    default="World",
    help="The name of the person to greet.",
    show_default=True,
)
@version_option(_get_version())
def main(name: str = "World"):
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
