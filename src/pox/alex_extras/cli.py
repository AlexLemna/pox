""" `pox/alex_extras/cli.py`

A module containing a function, `main()`, that handles situations
where the user calls `pox` with flag arguments (like `--version`)."""

import sys

from pox.alex_extras.versioning import PoxVersion


def main():
    """Handles situations where the user calls `pox` with flag
    arguments (like `--version`)."""

    cli_args = sys.argv[1:]

    if cli_args[-1] == "--version":
        v = PoxVersion()
        print(v)
