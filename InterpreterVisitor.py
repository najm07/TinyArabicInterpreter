# --- Interpreter Visitor: Implements Visitor Pattern for AST Evaluation ---

from ASTClasses import Visitor

class InterpreterVisitor(Visitor):
    """Visitor implementation for interpreting AST nodes."""
    
    def __init__(self):
        self.variables = {}  # memory (environment)
    
    def visit_num(self, node):
        """Visit a Num node."""
        return node.value
    
    def visit_string(self, node):
        """Visit a String node."""
        return node.value
    
    def visit_var(self, node):
        """Visit a Var node."""
        if node.name in self.variables:
            return self.variables[node.name]
        else:
            raise Exception(f"Undefined variable: {node.name}")
    
    def visit_binop(self, node):
        """Visit a BinOp node."""
        left = node.left.accept(self)
        right = node.right.accept(self)
        
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
    
    def visit_assign(self, node):
        """Visit an Assign node."""
        value = node.value.accept(self)
        self.variables[node.name] = value
        return value
    
    def visit_print(self, node):
        """Visit a Print node."""
        result = node.value.accept(self)
        print(result)
        return None
    
    def visit_comparison(self, node):
        """Visit a Comparison node."""
        left = node.left.accept(self)
        right = node.right.accept(self)
        
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
    
    def visit_logicalop(self, node):
        """Visit a LogicalOp node."""
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        if node.op == 'و':  # AND
            return left and right
        elif node.op == 'أو':  # OR
            return left or right
        else:
            raise Exception(f"Unknown logical operator: {node.op}")
    
    def visit_not(self, node):
        """Visit a Not node."""
        return not node.expr.accept(self)
    
    def visit_if(self, node):
        """Visit an If node."""
        condition = node.condition.accept(self)
        if condition:
            return node.then_branch.accept(self)
        elif node.else_branch:
            return node.else_branch.accept(self)
        return None
    
    def visit_while(self, node):
        """Visit a While node."""
        while node.condition.accept(self):
            node.body.accept(self)
        return None
    
    def visit_for(self, node):
        """Visit a For node."""
        start = node.start.accept(self)
        end = node.end.accept(self)
        for i in range(start, end + 1):
            self.variables[node.variable] = i
            node.body.accept(self)
        return None
    
    def visit_block(self, node):
        """Visit a Block node."""
        for statement in node.statements:
            statement.accept(self)
        return None
