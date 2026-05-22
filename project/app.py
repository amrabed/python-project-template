from click import UsageError, command, option, secho, version_option


@command(context_settings={"help_option_names": ["-h", "--help"]}, help="Say hello to a user.")
@option(
    "-n",
    "--name",
    default="World",
    help="The name of the person to greet.",
    show_default=True,
)
@version_option()
def main(name: str = "World") -> None:
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    name = name.strip()
    if not name:
        name = "World"

    if len(name) > 100:
        raise UsageError("Name cannot exceed 100 characters.")

    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
