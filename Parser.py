from ASTClasses import *
from Errors import ParseError

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
            expected = token_type
            got = self.current_token.type if self.current_token else "EOF"
            position = self.current_token.position if self.current_token else None
            raise ParseError(f"Expected {expected}, got {got}", position)

    # Grammar start: statement
    def parse(self):
        node = self.statement()
        return node

    def statement(self):
        if not self.current_token:
            raise ParseError("Unexpected end of input", None)
            
        # Block statement (brackets)
        if self.current_token.type == "LBRACKET":
            return self.block_statement()
        
        # IF statement
        if self.current_token.type == "IF":
            self.eat("IF")
            condition = self.logical_or()
            then_branch = self.statement()
            else_branch = None
            if self.current_token and self.current_token.type == "ELSE":
                self.eat("ELSE")
                else_branch = self.statement()
            return If(condition, then_branch, else_branch)
        
        # WHILE statement
        elif self.current_token.type == "WHILE":
            self.eat("WHILE")
            condition = self.logical_or()
            body = self.statement()  # This will handle INDENT/DEDENT
            return While(condition, body)
        
        # FOR statement
        elif self.current_token.type == "FOR":
            self.eat("FOR")
            var_name = self.current_token.value
            self.eat("IDENTIFIER")
            self.eat("IN")
            start = self.logical_or()
            self.eat("UNTIL")  # Using UNTIL as the range separator
            end = self.logical_or()
            body = self.statement()
            return For(var_name, start, end, body)
        
        # PRINT statement
        elif self.current_token.type == "PRINT":
            self.eat("PRINT")
            return Print(self.logical_or())
        else:
            if self.current_token.type == "IDENTIFIER":
                var_name = self.current_token.value
                self.eat("IDENTIFIER")

                if self.current_token and self.current_token.type == "EQUAL":
                    self.eat("EQUAL")
                    expr_node = self.logical_or()
                    return Assign(var_name, expr_node)
                else:
                    # if it's just a variable reference
                    return Var(var_name)
            else:
                return self.logical_or()

    def logical_or(self):
        """Handles OR operator (lowest precedence)"""
        node = self.logical_and()

        while self.current_token and self.current_token.type == "OR":
            op = self.current_token.value
            self.eat("OR")
            right = self.logical_and()
            node = LogicalOp(node, op, right)

        return node

    def logical_and(self):
        """Handles AND operator"""
        node = self.comparison()

        while self.current_token and self.current_token.type == "AND":
            op = self.current_token.value
            self.eat("AND")
            right = self.comparison()
            node = LogicalOp(node, op, right)

        return node

    def comparison(self):
        """Handles comparison operators (==, !=, >, <, >=, <=)"""
        node = self.expr()

        while self.current_token and self.current_token.type in ("EQUAL_EQUAL", "NOT_EQUAL", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL"):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.expr()
            node = Comparison(node, op, right)

        return node

    def expr(self):
        """Handles + and -"""
        node = self.term()

        while self.current_token and self.current_token.type in ("PLUS", "MINUS"):
            op = self.current_token.value
            op_pos = self.current_token.position
            self.eat(self.current_token.type)
            right = self.term()
            node = BinOp(node, op, right, op_pos)

        return node

    def term(self):
        """Handles * and /"""
        node = self.factor()

        while self.current_token and self.current_token.type in ("STAR", "SLASH"):
            op = self.current_token.value
            op_pos = self.current_token.position
            self.eat(self.current_token.type)
            right = self.factor()
            node = BinOp(node, op, right, op_pos)

        return node

    def factor(self):
        token = self.current_token
        
        if not token:
            raise ParseError("Unexpected end of input", None)

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return Num(token.value, token.position)

        elif token.type == "STRING":
            self.eat("STRING")
            return String(token.value, token.position)

        elif token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            return Var(token.value, token.position)

        elif token.type == "NOT":
            self.eat("NOT")
            return Not(self.factor())

        elif token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.logical_or()
            self.eat("RPAREN")
            return node

        raise Exception(f"Unexpected token: {token}")


    def block_statement(self):
        """Parse a block statement: [ statement1 statement2 ... ]"""
        self.eat("LBRACKET")
        statements = []
        
        while self.current_token and self.current_token.type != "RBRACKET":
            statements.append(self.statement())
        
        self.eat("RBRACKET")
        return Block(statements)
