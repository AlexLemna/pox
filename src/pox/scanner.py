""" `pox/scanner.py`

The module containing the `Scanner` class for our Lox interpreter, as well as
the `ScannerError` class for any errors that the scanner throws.

It corresponds to the following sections from Chapter 4 ("Scanning") in the 
Crafting Interpreters book:

- [4.4: The Scanner Class](http://www.craftinginterpreters.com/scanning.html#the-scanner-class)
- [4.5: Recognizing Lexemes](http://www.craftinginterpreters.com/scanning.html#recognizing-lexemes)
- [4.6: Longer Lexemes](http://www.craftinginterpreters.com/scanning.html#longer-lexemes)
- [4.7: Reserved Words and Identifiers](http://www.craftinginterpreters.com/scanning.html#reserved-words-and-identifiers)

This file is is equivalent to the `Scanner.java` file in Nystrom's original
jlox implementation. A link to the most recent version of that file can be 
found below, as well as a permalink to the file as it existed when I began
this project.

- [link to Scanner.java](https://github.com/munificent/craftinginterpreters/blob/master/java/com/craftinginterpreters/lox/Scanner.java)
- [permalink](https://github.com/munificent/craftinginterpreters/blob/01e6f5b8f3e5dfa65674c2f9cf4700d73ab41cf8/java/com/craftinginterpreters/lox/Scanner.java)"""

from .lox_token import Token
from .lox_token_types import TokenType


class ScannerError(Exception):
    """A class for all errors thrown by the Scanner class,
    such as unterminated strings and unrecognized
    characters."""

    def __init__(self, line: int, message: str) -> None:
        """Initializes the ScannerError."""
        super().__init__(message)
        self.line = line
        self.message = message


class Scanner:
    """A Scanner, as outlined in \
    [Chapter 4](http://www.craftinginterpreters.com/scanning.html)\
    of Crafting Interpreters."""

    KEYWORDS = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE,
    }

    def __init__(self, code: str) -> None:
        """Initializes the Scanner."""

        # We store the raw source code as a simple string,
        # and we have a list ready to fill with tokens
        # we’re going to generate.
        self.source = code
        self.tokens = []

        # The start and current fields are offsets that
        # index into the string. The start field points to
        # the first character in the lexeme being scanned,
        # and current points at the character currently
        # being considered. The line field tracks what
        # source line current is on so we can produce
        # tokens that know their location.
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1

    # Corresponds to:
    # - [Section 4.4](https://craftinginterpreters.com/scanning.html#the-scanner-class)
    def scanTokens(self) -> list[Token]:
        """This function iterates through the input source code until it
        reaches the end, scanning each lexeme encountered and appending the
        corresponding `Token` object to the list of tokens. If the end of
        the input is reached, a `Token` representing the end of file (EOF)
        is appended to the list before returning."""

        while not self.__isAtEnd():  # we are at beginning of next lexeme
            self.start = self.current
            self.__scanToken()
        else:
            self.tokens.append(
                Token(
                    type=TokenType.EOF,
                    lexeme="",
                    literal=None,
                    line=self.line,
                )
            )
            return self.tokens

    # Corresponds to:
    # - [Section 4.5](https://craftinginterpreters.com/scanning.html#recognizing-lexemes)
    # - [Section 4.6](https://craftinginterpreters.com/scanning.html#longer-lexemes)
    # - [Section 4.7](https://craftinginterpreters.com/scanning.html#reserved-words-and-identifiers)
    def __scanToken(self):
        """Scans the current position in the source code and identifies
        the token at that position.

        This method examines the character at the current position in the
        source code and determines the corresponding token type. Depending
        on the character, it may identify single-character tokens or
        potentially multi-character tokens. It also handles comments,
        whitespace, newlines, string literals, number literals, and
        identifiers.

        Raises:
            ScannerError: If the character at the current position does
            not match any expected token type, indicating an unexpected
            character."""

        c = self.__advance()
        match c:
            # Unambiguously single-character tokens
            case "(":
                self.__addToken(TokenType.LEFT_PAREN)
            case ")":
                self.__addToken(TokenType.RIGHT_PAREN)
            case "{":
                self.__addToken(TokenType.LEFT_BRACE)
            case "}":
                self.__addToken(TokenType.RIGHT_BRACE)
            case ",":
                self.__addToken(TokenType.COMMA)
            case ".":
                self.__addToken(TokenType.DOT)
            case "-":
                self.__addToken(TokenType.MINUS)
            case "+":
                self.__addToken(TokenType.PLUS)
            case ";":
                self.__addToken(TokenType.SEMICOLON)
            case "*":
                self.__addToken(TokenType.STAR)

            # Potentially multi-character tokens
            case "!":
                self.__addToken(
                    TokenType.BANG_EQUAL
                    if self.__match("=")
                    else TokenType.BANG
                )
            case "=":
                self.__addToken(
                    TokenType.EQUAL_EQUAL
                    if self.__match("=")
                    else TokenType.EQUAL
                )
            case "<":
                self.__addToken(
                    TokenType.LESS_EQUAL
                    if self.__match("=")
                    else TokenType.LESS
                )
            case ">":
                self.__addToken(
                    TokenType.GREATER_EQUAL
                    if self.__match("=")
                    else TokenType.GREATER
                )

            # and the particularly fancy case of comments, which can go until
            # the end of the line...
            case "/":
                if self.__match("/"):
                    while self.__peek() != "\n" and not self.__isAtEnd():
                        self.__advance()
                else:
                    self.__addToken(TokenType.SLASH)

            # Whitespace...
            case " " | "\r" | "\t":
                pass
            # ...and newlines...
            case "\n":
                self.line += 1

            # String literals
            case '"':
                self.__string()

            # Number literals
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                self.__number()

            # Identifiers
            case _ if c.isalpha() or c == "_":
                self.__identifier()

            # and, if all else fails...
            case _:
                # This code corresponds to section 4.5.1 in Crafting Interpreters.
                # Link: http://www.craftinginterpreters.com/scanning.html#lexical-errors

                # I modified the error message slightly to include the offending
                # character.
                raise ScannerError(
                    self.line,
                    f"Unexpected character: {c}",
                )

    # Corresponds to:
    # - [Section 4.7](https://craftinginterpreters.com/scanning.html#reserved-words-and-identifiers)
    def __identifier(self):
        """A special function to handle literal identifier tokens or
        literal keyword tokens."""

        while (c := self.__peek()).isalpha() or c.isdigit() or c == "_":
            self.__advance()

        text = self.source[self.start : self.current]

        try:
            token_type = self.KEYWORDS[text]
        except KeyError:
            token_type = TokenType.IDENTIFIER

        # BUG: Should be __addToken(token_type, text)?
        self.__addToken(token_type)

    # Corresponds to:
    # - [Section 4.6.2](https://craftinginterpreters.com/scanning.html#number-literals)
    def __number(self):
        """A special function to handle literal string tokens."""

        while self.__peek().isdigit():
            self.__advance()

        if self.__peek() == "." and self.__peekNext().isdigit():
            self.__advance()
            while self.__peek().isdigit():
                self.__advance()

        value: float = float(self.source[self.start : self.current])
        self.__addToken(TokenType.NUMBER, literal=value)

    # Corresponds to:
    # - [Section 4.6.1](https://craftinginterpreters.com/scanning.html#string-literals)
    def __string(self):
        """A special function to handle literal string tokens."""

        while self.__peek() != '"' and not self.__isAtEnd():
            if self.__peek() == "\n":
                self.line += 1
            self.__advance()

        if self.__isAtEnd():
            raise ScannerError(
                self.line,
                f"Unterminated string at end of file.",
            )

        # if closing '"'
        self.__advance()

        value: str = self.source[self.start + 1 : self.current - 1]
        self.__addToken(TokenType.STRING, literal=value)

    # Corresponds to:
    # - [Section 4.5.2](http://www.craftinginterpreters.com/scanning.html#operators)
    def __match(self, expected: str) -> bool:
        """Checks to see if the character at the current index of the source
        string matches an expected string. If it matches, the current index
        is advanced by 1 and this function returns `True`. Otherwise, the
        current index is unchanged and this function returns `False`.

        Practically, you can use this function like a conditional `advance()`
        which returns `True` if it advanced and `False` otherwise."""

        if self.__isAtEnd():
            return False
        elif self.source[self.current] != expected:
            return False
        else:
            self.current += 1
            return True

    # Corresponds to:
    # - [Section 4.6](https://craftinginterpreters.com/scanning.html#longer-lexemes)
    def __peek(self) -> str:
        """Returns the character at the current index, or `'\\0'` if the
        current index is at or beyond the end of the source string."""

        return "\0" if self.__isAtEnd() else self.source[self.current]

    # Corresponds to:
    # - [Section 4.6.2](https://craftinginterpreters.com/scanning.html#number-literals)
    def __peekNext(self) -> str:
        """Returns the character at the current index + 1, or `'\\0'` if
        that character would be at or beyond the end of the source string.
        """
        return (
            "\0"
            if self.current + 1 >= len(self.source)
            else self.source[self.current + 1]
        )

    # Corresponds to:
    # - [Section 4.7](https://craftinginterpreters.com/scanning.html#reserved-words-and-identifiers)
    def __isAlpha(self, c):
        """This method is not implemented because the functionality
        is already available via built-in Python.
            >>> c = "a"
            >>> c.isalpha()
            True
        """
        raise NotImplementedError

    # Corresponds to:
    # - [Section 4.7](https://craftinginterpreters.com/scanning.html#reserved-words-and-identifiers)
    def __isAlphaNumeric(self, c):
        """This method is not implemented because the functionality
        is already available via built-in Python.
            >>> c = "a1"
            >>> c.isalpha()
            True
        """
        raise NotImplementedError

    # Corresponds to:
    # - [Section 4.6.2](https://craftinginterpreters.com/scanning.html#number-literals)
    def __isDigit(self, c):
        """This method is not implemented because the functionality
        is already available via built-in Python.
            >>> c = "1"
            >>> c.isdigit()
            True
        """
        raise NotImplementedError

    # Corresponds to:
    # - [Section 4.4](https://craftinginterpreters.com/scanning.html#the-scanner-class)
    def __isAtEnd(self) -> bool:
        """Returns `True` if the current scanner position is at or beyond
        the end of the source code string."""
        return True if self.current >= len(self.source) else False

    # Corresponds to:
    # - [Section 4.5](http://www.craftinginterpreters.com/scanning.html#recognizing-lexemes)
    def __advance(self) -> str:
        """Returns whatever character is in the Scanner's `self.source`
        string at index `self.current`, then increments `self.current`
        by 1."""

        # IMPLEMENTATION NOTE: Nystrom's original Java code for this method is
        #
        #   private char advance() {
        #       return source.charAt(current++);
        #   }
        #
        # In Java, the `++` operator after the variable `current` increments
        # the value of `current` by 1 and returns the value of `current` before
        # it was incremented.
        #
        # This kind of "return, then increment" operation isn't available in
        # Python, as far as I know. So, we take a few extra lines to get the
        # same effect.

        c = self.source[self.current]
        self.current += 1
        return c

    # Corresponds to:
    # - [Section 4.5](http://www.craftinginterpreters.com/scanning.html#recognizing-lexemes)
    def __addToken(self, tokentype: TokenType, literal: object = None):
        """Grabs the text of the current lexeme and creates a new token for
        it, then adds the new token to the Scanner's `self.tokens`."""

        text = self.source[self.start : self.current]
        self.tokens.append(
            Token(
                type=tokentype,
                lexeme=text,
                literal=literal,
                line=self.line,
            )
        )


#
#
#

#!todo-finder: end


class AuldScanner:
    # TODO: If I could, I'd prefer to implement this scanner with some
    # slightly adjusted methods.
    #
    #   .advance() -> increment the current index by 1.
    #   .read_current() -> return whatever character is in the source
    #                      string at the current index.
    #   .read_next() -> return whatever character is in the source string
    #                   at the "current + 1" index.
    #   .read_current_and_advance() -> save whatever character is in the
    #                          source string at the current index as 'c',
    #                          then advance the current index by 1, then
    #                          return c.

    # Instead of defining Lox's keywords a second time, we can just reuse
    # the definitions we created for the original Scanner above.
    KEYWORDS = Scanner.KEYWORDS

    class cursor:
        def advance(self): ...
        def read_current(self) -> str: ...
        def read_ahead(self, ahead_by: int = 1) -> str: ...
        def read_current_and_advance(self) -> str: ...

    class handle_long_token:
        def comment(self): ...
        def identifier(self): ...  # TODO: Rename to 'identifier_or_keyword'?
        def number(self): ...
        def string(self): ...
