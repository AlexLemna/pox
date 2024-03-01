""" `pox/__main__.py`

A module that acts as an entrypoint to the `pox` package."""

from .lox import Lox


def run_pox():
    """Runs the Lox interpreter."""

    try:
        # TODO: explain this
        Lox().main()

    except FileNotFoundError as e:  # TODO: explain this
        import pox.alex_extras.cli

        if e.filename == "--version":
            pox.alex_extras.cli.main()
        else:
            raise e
