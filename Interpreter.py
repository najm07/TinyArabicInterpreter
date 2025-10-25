# --- Tiny Interpreter: Evaluator Stage ---

from ASTClasses import *

class Interpreter:
    def __init__(self):
        self.variables = {}  # memory (environment)

    def eval(self, node):
        """Evaluate a node in the AST."""
        if isinstance(node, Print):
            print(self.eval(node.value))
            return None

        elif isinstance(node, Num):
            return node.value

        elif isinstance(node, String):
            return node.value

        elif isinstance(node, Var):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                raise Exception(f"Undefined variable: {node.name}")

        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)

            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
            else:
                raise Exception(f"Unknown operator: {node.op}")

        elif isinstance(node, Comparison):
            left = self.eval(node.left)
            right = self.eval(node.right)

            if node.op == '==':
                return left == right
            elif node.op == '!=':
                return left != right
            elif node.op == '>':
                return left > right
            elif node.op == '<':
                return left < right
            elif node.op == '>=':
                return left >= right
            elif node.op == '<=':
                return left <= right
            else:
                raise Exception(f"Unknown comparison operator: {node.op}")

        elif isinstance(node, LogicalOp):
            left = self.eval(node.left)
            right = self.eval(node.right)

            if node.op == 'و':  # AND
                return left and right
            elif node.op == 'أو':  # OR
                return left or right
            else:
                raise Exception(f"Unknown logical operator: {node.op}")

        elif isinstance(node, Not):
            return not self.eval(node.expr)

        elif isinstance(node, If):
            condition = self.eval(node.condition)
            if condition:
                return self.eval(node.then_branch)
            elif node.else_branch:
                return self.eval(node.else_branch)
            return None

        elif isinstance(node, While):
            while self.eval(node.condition):
                self.eval(node.body)
            return None

        elif isinstance(node, For):
            start = self.eval(node.start)
            end = self.eval(node.end)
            for i in range(start, end + 1):
                self.variables[node.variable] = i
                self.eval(node.body)
            return None

        elif isinstance(node, Assign):
            value = self.eval(node.value)
            self.variables[node.name] = value
            return value

        elif isinstance(node, Block):
            for statement in node.statements:
                self.eval(statement)
            return None

        else:
            raise Exception(f"Unknown node type: {node}")
