""" `pox/lox_token.py`

The module containing `Token`, a class for representing Lox tokens.

It corresponds to the following sections from Chapter 4 ("Scanning")
in the Crafting Interpreters book:

- [4.2.3: Location information](https://craftinginterpreters.com/scanning.html#location-information)

This file is is equivalent to the `Token.java` file in Nystrom's original
jlox implementation. I renamed this file to `lox_token.py` because it 
conflicted with a module in Python's standard library. A link to the most 
recent version of that file can be found below, as well as a permalink to
the file as it existed when I began this project.

- [link to Token.java](https://github.com/munificent/craftinginterpreters/blob/master/java/com/craftinginterpreters/lox/Token.java)
- [permalink to Token.java](https://github.com/munificent/craftinginterpreters/blob/01e6f5b8f3e5dfa65674c2f9cf4700d73ab41cf8/java/com/craftinginterpreters/lox/Token.java)"""

from dataclasses import dataclass

from .lox_token_types import TokenType


# Corresponds to:
# - [4.2.3: Location information](https://craftinginterpreters.com/scanning.html#location-information)
@dataclass(frozen=True)
class Token:
    """A class for representing Lox lexical tokens."""

    type: TokenType
    """The `TokenType` of this token."""
    lexeme: str
    """The name of the token, or symbol associated with thte token."""
    literal: object
    """The value of the token, if it is a string or number literal."""
    line: int
    """The line of source code that this token was found on."""

    def __str__(self) -> str:
        """Implements `str(token)`."""
        return f"{self.type} {self.lexeme} {self.literal}"
