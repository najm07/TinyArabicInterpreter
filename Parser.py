from ASTClasses import *

# --- Tiny Interpreter: Parser Stage ---

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None

    def eat(self, token_type):
        """Check and consume the current token."""
        if self.current_token and self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
            else:
                self.current_token = None
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token}")

    # Grammar start: statement
    def parse(self):
        node = self.statement()
        return node

    def statement(self):
        # assignment
        if self.current_token.type == "PRINT":
            self.eat("PRINT")
            return Print(self.expr())
        else:
            if self.current_token.type == "IDENTIFIER":
                var_name = self.current_token.value
                self.eat("IDENTIFIER")

                if self.current_token and self.current_token.type == "EQUAL":
                    self.eat("EQUAL")
                    expr_node = self.expr()
                    return Assign(var_name, expr_node)
                else:
                    # if it's just a variable reference
                    return Var(var_name)
            else:
                return self.expr()

    def expr(self):
        """Handles + and -"""
        node = self.term()

        while self.current_token and self.current_token.type in ("PLUS", "MINUS"):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.term()
            node = BinOp(node, op, right)

        return node

    def term(self):
        """Handles * and /"""
        node = self.factor()

        while self.current_token and self.current_token.type in ("STAR", "SLASH"):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.factor()
            node = BinOp(node, op, right)

        return node

    def factor(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return Num(token.value)

        elif token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            return Var(token.value)

        elif token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

        raise Exception(f"Unexpected token: {token}")
