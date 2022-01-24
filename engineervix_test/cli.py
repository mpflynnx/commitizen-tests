"""Console script for engineervix_test."""
import argparse
import sys


def main(args=None):
    """Console script for engineervix_test."""
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="engineervix_test",
        description="This is a simple way to quickly get started with my python project.",
    )
    parser.add_argument('_', nargs='*')
    args = parser.parse_args(args)

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "engineervix_test.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
