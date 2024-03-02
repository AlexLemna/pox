from abc import ABC, abstractmethod
from dataclasses import dataclass

from pox.lox_token import Token

# NOTE: We can define the type of visitor as "ExprVisitor" even
# though ExprVisitor is only defined later in this file. This is
# called a forward declaration. For more info, see:
# - [A useful explanation from StackOverflow](https://stackoverflow.com/a/36286947)
# - [PEP 563, "Postponed Evaluation of Annotations"](https://peps.python.org/pep-0563/)


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: "ExprVisitor"): ...


@dataclass(frozen=True)
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitBinaryExpr(self)


@dataclass(frozen=True)
class Grouping(Expr):
    expression: Expr

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitGroupingExpr(self)


@dataclass(frozen=True)
class Literal(Expr):
    value: object

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitLiteralExpr(self)


@dataclass(frozen=True)
class Unary(Expr):
    operator: Token
    right: Expr

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitUnaryExpr(self)


class ExprVisitor(ABC):
    @abstractmethod
    def visitBinaryExpr(self, expr: Binary): ...
    @abstractmethod
    def visitGroupingExpr(self, expr: Grouping): ...
    @abstractmethod
    def visitLiteralExpr(self, expr: Literal): ...
    @abstractmethod
    def visitUnaryExpr(self, expr: Unary): ...
