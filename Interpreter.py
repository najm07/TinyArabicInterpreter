# --- Tiny Interpreter: Evaluator Stage ---

from InterpreterVisitor import InterpreterVisitor

class Interpreter:
    """Interpreter using the Visitor Pattern for clean separation of concerns."""
    
    def __init__(self):
        self.visitor = InterpreterVisitor()

    def eval(self, node):
        """Evaluate a node in the AST using the visitor pattern."""
        return node.accept(self.visitor)
    
    @property
    def variables(self):
        """Access to variables for debugging purposes."""
        return self.visitor.variables
