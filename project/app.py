from click import command, option, secho, version_option


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
    # Security: Limit input length to prevent DoS or log flooding
    if len(name) > 100:
        secho("Error: Name is too long (max 100 characters).", fg="red", err=True)
        return

    secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
