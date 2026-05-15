import click


@click.command(context_settings={"help_option_names": ["-h", "--help"]}, help="Say hello to a user.")
@click.option(
    "-n",
    "--name",
    default="World",
    help="The name of the person to greet.",
    show_default=True,
)
@click.version_option()
def main(name: str = "World"):
    """
    Say hello to the given name.

    Args:
      name: the name to be greeted
    """
    click.secho(f"Hello {name}! 👋", fg="green", bold=True)


if __name__ == "__main__":
    main()
