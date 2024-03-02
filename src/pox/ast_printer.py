from pox.expr import Binary, Expr, ExprVisitor, Grouping, Literal, Unary
from pox.lox_token import Token
from pox.lox_token_types import TokenType


class AstPrinter(ExprVisitor):
    def print(self, expr: Expr):
        return expr.accept(visitor=self)

    def visitBinaryExpr(self, expr: Binary):
        return self.__parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr: Grouping):
        return self.__parenthesize("group", expr.expression)

    def visitLiteralExpr(self, expr: Literal):
        if expr.value is None:
            return "nil"
        else:
            return str(expr.value)

    def visitUnaryExpr(self, expr: Unary):
        return self.__parenthesize(expr.operator.lexeme, expr.right)

    def __parenthesize(self, name: str, *exprs: Expr) -> str:
        builder = f"({name}"

        for expr in exprs:
            builder += f" {expr.accept(self)}"

        builder += ")"
        return builder


if __name__ == "__main__":
    expression = Binary(
        left=Unary(
            operator=Token(TokenType.MINUS, "-", None, 1),
            right=Literal(123),
        ),
        operator=Token(TokenType.STAR, "*", None, 1),
        right=Grouping(
            Literal(value=45.67),
        ),
    )

    print(AstPrinter().print(expression))
