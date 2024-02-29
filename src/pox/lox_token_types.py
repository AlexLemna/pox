""" `pox/lox_token.py`

The module defining valid Lox tokens.

It corresponds to the following sections from Chapter 4 ("Scanning")
in the Crafting Interpreters book:

- [4.2.1: Token type](https://craftinginterpreters.com/scanning.html#token-type)

This file is is equivalent to the `TokenType.java` file in Nystrom's
original jlox implementation. I renamed this file to `lox_token_types.py`
because it conflicted with a module in Python's standard library.
A link to the most recent version of that file can be found below, as 
well as a permalink to the file as it existed when I began this project.

- [link to TokenType.java](https://github.com/munificent/craftinginterpreters/blob/master/java/com/craftinginterpreters/lox/TokenType.java)
- [permalinkto TokenType.java](https://github.com/munificent/craftinginterpreters/blob/01e6f5b8f3e5dfa65674c2f9cf4700d73ab41cf8/java/com/craftinginterpreters/lox/TokenType.java)"""

import enum


# Corresponds to:
# - [4.2.1: Token type](https://craftinginterpreters.com/scanning.html#token-type)
class TokenType(enum.Enum):
    """A class enumerating all types of valid Lox tokens."""

    # Single-character tokens.
    LEFT_PAREN = enum.auto()
    """A token for the `(` lexeme."""
    RIGHT_PAREN = enum.auto()
    """A token for the `)` lexeme."""
    LEFT_BRACE = enum.auto()
    """A token for the `{` lexeme."""
    RIGHT_BRACE = enum.auto()
    """A token for the `}` lexeme."""
    COMMA = enum.auto()
    """A token for the `,` lexeme."""
    DOT = enum.auto()
    """A token for the `.` lexeme."""
    MINUS = enum.auto()
    """A token for the `-` lexeme."""
    PLUS = enum.auto()
    """A token for the `+` lexeme."""
    SEMICOLON = enum.auto()
    """A token for the `;` lexeme."""
    SLASH = enum.auto()
    """A token for the `/` lexeme."""
    STAR = enum.auto()
    """A token for the `*` lexeme."""

    # One or two character tokens.
    BANG = enum.auto()
    """A token for the `!` lexeme."""
    BANG_EQUAL = enum.auto()
    """A token for the `!=` lexeme."""
    EQUAL = enum.auto()
    """A token for the `=` lexeme."""
    EQUAL_EQUAL = enum.auto()
    """A token for the `==` lexeme."""
    GREATER = enum.auto()
    """A token for the `>` lexeme."""
    GREATER_EQUAL = enum.auto()
    """A token for the `>=` lexeme."""
    LESS = enum.auto()
    """A token for the `<` lexeme."""
    LESS_EQUAL = enum.auto()
    """A token for the `<=` lexeme."""

    # Literals.
    IDENTIFIER = enum.auto()
    """A token for lexemes representing literal identifiers."""
    STRING = enum.auto()
    """A token for lexemes representing literal strings."""
    NUMBER = enum.auto()
    """A token for lexemes representing literal numbers."""

    # Keywords.
    AND = enum.auto()
    """A token for the `and` lexeme."""
    CLASS = enum.auto()
    """A token for the `class` lexeme."""
    ELSE = enum.auto()
    """A token for the `else` lexeme."""
    FALSE = enum.auto()
    """A token for the `false` lexeme."""
    FUN = enum.auto()
    """A token for the `fun` lexeme."""
    FOR = enum.auto()
    """A token for the `for` lexeme."""
    IF = enum.auto()
    """A token for the `if` lexeme."""
    NIL = enum.auto()
    """A token for the `nil` lexeme."""
    OR = enum.auto()
    """A token for the `or` lexeme."""
    PRINT = enum.auto()
    """A token for the `print` lexeme."""
    RETURN = enum.auto()
    """A token for the `return` lexeme."""
    SUPER = enum.auto()
    """A token for the `super` lexeme."""
    THIS = enum.auto()
    """A token for the `this` lexeme."""
    TRUE = enum.auto()
    """A token for the `true` lexeme."""
    VAR = enum.auto()
    """A token for the `var` lexeme."""
    WHILE = enum.auto()
    """A token for the `while` lexeme."""

    EOF = enum.auto()
    """An 'end-of-file' token, which the scanner will add to its
    list of tokens once it has reached the end of the file. Having
    this token allows some of the code in our Parser to be a little
    cleaner."""
