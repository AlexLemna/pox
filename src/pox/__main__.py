""" `pox/__main__.py`

A module that acts as an entrypoint to the `pox` package."""

from .lox import Lox


def run_pox():
    """Runs the Lox interpreter."""
    Lox().main()
