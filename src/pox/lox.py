""" `pox/lox.py`

The module containing the Lox interpreter, a class named `Lox`.

It corresponds to the following sections from Chapter 4 ("Scanning")
in the Crafting Interpreters book:

- [4.1: The Interpreter Framework](https://craftinginterpreters.com/scanning.html#the-interpreter-framework)
- [4.1.1: Error handling](https://craftinginterpreters.com/scanning.html#error-handling)

This file is is equivalent to the `Lox.java` file in Nystrom's original
jlox implementation. A link to the most recent version of that file can be 
found below, as well as a permalink to the file as it existed when I began
this project.

- [link to Lox.java](https://github.com/munificent/craftinginterpreters/blob/master/java/com/craftinginterpreters/lox/Lox.java)
- [permalink to Lox.java](https://github.com/munificent/craftinginterpreters/blob/01e6f5b8f3e5dfa65674c2f9cf4700d73ab41cf8/java/com/craftinginterpreters/lox/Lox.java)"""

import sys

from .lox_token import Token
from .scanner import Scanner, ScannerError


class Lox:
    """The Lox interpreter."""

    # Corresponds to:
    # - [Section 4.1.1](http://www.craftinginterpreters.com/scanning.html#error-handling)
    hadError: bool = False
    """We use this to avoid executing code that has a known error. We also use it to
    exit with a non-zero exit code when necessary."""

    # Corresponds to:
    # - [Section 4.1](http://www.craftinginterpreters.com/scanning.html#the-interpreter-framework)
    def main(self, args: list[str] = sys.argv[1:]):
        """The first bit of code we write, this method serves as the 'entry point'
        to our Lox interpreter. It's the bit of code that lets us call our program
        by typing

        ```shell
            $ pox
        ```
        or
        ```shell
            $ pox somefile.lox
        ```

        If we call our program with no arguments (just `pox`), it launches the REPL
        prompt. If we call our program with one argument (`pox somefile.lox`), it
        assumes that argument is the name of a Lox script. If we call our program
        with more than one argument, it exits with an error.
        """

        number_of_args = len(args)

        if number_of_args > 1:
            print("Usage: my_python_lox [script]")
            sys.exit(64)

        elif number_of_args == 1:
            self.__run_file(args[0])

        else:
            self.__run_prompt()

    #
    # MAIN INTERNAL FUNCTIONS
    # -----------------------
    #

    # Corresponds to:
    # - [Section 4.1](http://www.craftinginterpreters.com/scanning.html#the-interpreter-framework)
    def __run_file(self, target: str):
        """A wrapper around `Lox().__run()` which adds some code to enable
        running Lox source file."""

        with open(target, mode="r", encoding="utf-8") as f:
            source_code = f.read()

        self.__run(source_code)

        if self.hadError:
            sys.exit(65)

    # Corresponds to:
    # - [Section 4.1](http://www.craftinginterpreters.com/scanning.html#the-interpreter-framework)
    def __run_prompt(self):
        """A wrapper around `Lox().__run()` which adds some code to enable
        running Lox from a REPL."""

        try:
            while True:
                line = input("> ")
                self.__run(line)
                self.hadError = False  # Instead of checking self.hadError to
                # see if we need to exit (like we do in run_file), we reset
                # hadError here because we want the REPL session to continue.
        except (KeyboardInterrupt, EOFError):
            sys.exit(64)

    # Corresponds to:
    # - [Section 4.1](http://www.craftinginterpreters.com/scanning.html#the-interpreter-framework)
    def __run(self, code: str):
        """The core function of our Lox interpreter. For now, it just prints
        out tokens it recieves from the `Scanner`."""

        try:
            scanner = Scanner(code)
            tokens: list[Token] = scanner.scanTokens()
        except ScannerError as e:
            self.error(e.line, e.message)
        else:
            for token in tokens:
                print(token)

    #
    # ERROR HANDLING
    # --------------
    #

    # Corresponds to:
    # - [Section 4.1.1](http://www.craftinginterpreters.com/scanning.html#error-handling)
    def error(self, line: int, message: str):
        """Handles all errors the interpreter might encounter."""

        self.__report(line, "", message)

    # Corresponds to:
    # - [Section 4.1.1](http://www.craftinginterpreters.com/scanning.html#error-handling)
    def __report(self, line: int, where: str, message: str):
        """Prints an error message for the user."""

        msg = f"[line {line}] Error{where}: {message}"
        print(msg)
        self.hadError = True
