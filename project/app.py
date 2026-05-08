from argparse import ArgumentParser


def main(argv: list[str] | None = None):
    """
    Say hello to the given name.

    Args:
      argv: list of command line arguments
    """
    parser = ArgumentParser(prog="app", description="Say hello", add_help=False)
    parser.add_argument("-n", "--name", default="World", help="Name (default: World)")
    parser.add_argument("-h", "--help", action="help", help="Show this message and exit.")
    args = parser.parse_args(argv)
    print(f"Hello {args.name}!")


if __name__ == "__main__":
    main()
