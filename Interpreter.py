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

        if isinstance(node, Num):
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

        elif isinstance(node, Assign):
            value = self.eval(node.value)
            self.variables[node.name] = value
            return value

        else:
            raise Exception(f"Unknown node type: {node}")
