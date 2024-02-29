from pathlib import Path

from pox.lox_token import Token
from pox.lox_token_types import TokenType
from pox.scanner import Scanner

THIS_DIR = Path(__file__).parent


def test_scanning_identifiers():

    with (THIS_DIR / "identifiers.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.IDENTIFIER, lexeme="andy", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="formless", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="fo", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="_", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="_123", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="_abc", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="ab123", literal=None, line=1),
        Token(
            TokenType.IDENTIFIER,
            lexeme="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_",
            literal=None,
            line=2,
        ),
        Token(TokenType.EOF, lexeme="", literal=None, line=12),
    ]

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


def test_scanning_keywords():
    with (THIS_DIR / "keywords.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.AND, lexeme="and", literal=None, line=1),
        Token(TokenType.CLASS, lexeme="class", literal=None, line=1),
        Token(TokenType.ELSE, lexeme="else", literal=None, line=1),
        Token(TokenType.FALSE, lexeme="false", literal=None, line=1),
        Token(TokenType.FOR, lexeme="for", literal=None, line=1),
        Token(TokenType.FUN, lexeme="fun", literal=None, line=1),
        Token(TokenType.IF, lexeme="if", literal=None, line=1),
        Token(TokenType.NIL, lexeme="nil", literal=None, line=1),
        Token(TokenType.OR, lexeme="or", literal=None, line=1),
        Token(TokenType.RETURN, lexeme="return", literal=None, line=1),
        Token(TokenType.SUPER, lexeme="super", literal=None, line=1),
        Token(TokenType.THIS, lexeme="this", literal=None, line=1),
        Token(TokenType.TRUE, lexeme="true", literal=None, line=1),
        Token(TokenType.VAR, lexeme="var", literal=None, line=1),
        Token(TokenType.WHILE, lexeme="while", literal=None, line=1),
        Token(TokenType.EOF, lexeme="", literal=None, line=18),
    ]

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


def test_scanning_numbers():
    with (THIS_DIR / "numbers.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.NUMBER, lexeme="123", literal=123.0, line=1),
        Token(TokenType.NUMBER, lexeme="123.456", literal=123.456, line=2),
        Token(TokenType.DOT, lexeme=".", literal=None, line=3),
        Token(TokenType.NUMBER, lexeme="456", literal=456.0, line=3),
        Token(TokenType.NUMBER, lexeme="123", literal=123.0, line=4),
        Token(TokenType.DOT, lexeme=".", literal=None, line=4),
        Token(TokenType.EOF, lexeme="", literal=None, line=12),
    ]

    # TODO: explain why not just assert tokens == expected

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


def test_scanning_punctuators():
    with (THIS_DIR / "punctuators.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.LEFT_PAREN, lexeme="(", literal=None, line=1),
        Token(TokenType.RIGHT_PAREN, lexeme=")", literal=None, line=1),
        Token(TokenType.LEFT_BRACE, lexeme="{", literal=None, line=1),
        Token(TokenType.RIGHT_BRACE, lexeme="}", literal=None, line=1),
        Token(TokenType.SEMICOLON, lexeme=";", literal=None, line=1),
        Token(TokenType.COMMA, lexeme=",", literal=None, line=1),
        Token(TokenType.PLUS, lexeme="+", literal=None, line=1),
        Token(TokenType.MINUS, lexeme="-", literal=None, line=1),
        Token(TokenType.STAR, lexeme="*", literal=None, line=1),
        Token(TokenType.BANG_EQUAL, lexeme="!=", literal=None, line=1),
        Token(TokenType.EQUAL_EQUAL, lexeme="==", literal=None, line=1),
        Token(TokenType.LESS_EQUAL, lexeme="<=", literal=None, line=1),
        Token(TokenType.GREATER_EQUAL, lexeme=">=", literal=None, line=1),
        Token(TokenType.BANG_EQUAL, lexeme="!=", literal=None, line=1),
        Token(TokenType.LESS, lexeme="<", literal=None, line=1),
        Token(TokenType.GREATER, lexeme=">", literal=None, line=1),
        Token(TokenType.SLASH, lexeme="/", literal=None, line=1),
        Token(TokenType.DOT, lexeme=".", literal=None, line=1),
        Token(TokenType.EOF, lexeme="", literal=None, line=21),
    ]

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


def test_scanning_strings():
    with (THIS_DIR / "strings.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.STRING, lexeme='""', literal="", line=1),
        Token(TokenType.STRING, lexeme='"string"', literal="string", line=2),
        Token(TokenType.EOF, lexeme="", literal=None, line=6),
    ]

    # TODO: explain why not just assert tokens == expected

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


def test_scanning_whitespace():
    with (THIS_DIR / "whitespace.lox").open(mode="r", encoding="utf-8") as f:
        source_code = f.read()

    scanner = Scanner(source_code)
    tokens = scanner.scanTokens()

    # from pprint import pprint
    # pprint(tokens)

    expected = [
        Token(TokenType.IDENTIFIER, lexeme="space", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="tabs", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="newlines", literal=None, line=1),
        Token(TokenType.IDENTIFIER, lexeme="end", literal=None, line=6),
        Token(TokenType.EOF, lexeme="", literal=None, line=12),
    ]

    # TODO: explain why not just assert tokens == expected

    assert len(tokens) == len(expected)

    for n in range(0, len(tokens)):
        token_found, token_expected = tokens[n], expected[n]
        assert token_found == token_expected


if __name__ == "__main__":
    test_scanning_identifiers()
    test_scanning_keywords()
    test_scanning_numbers()
    test_scanning_punctuators()
    test_scanning_strings()
    test_scanning_whitespace()
