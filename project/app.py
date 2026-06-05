from click import UsageError, command, option, secho, version_option


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
@version_option()
def main(name: str = "World"):
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    if len(name) > 100:
        raise UsageError("Invalid name: maximum length is 100 characters.")
    if any(c < " " for c in name):
        raise UsageError("Invalid name: control characters are not allowed.")

    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
