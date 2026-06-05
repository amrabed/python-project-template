from click import command, option, secho, version_option


@command(
    name="app",
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
@version_option(None, "-V", "--version")
def main(name: str = "World"):
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
