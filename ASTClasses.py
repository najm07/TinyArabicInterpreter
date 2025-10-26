# --- AST Node Classes ---

# Visitor Pattern Base Class
class Visitor:
    """Base visitor class for AST nodes."""
    def visit_num(self, node):
        raise NotImplementedError("visit_num must be implemented")
    
    def visit_string(self, node):
        raise NotImplementedError("visit_string must be implemented")
    
    def visit_var(self, node):
        raise NotImplementedError("visit_var must be implemented")
    
    def visit_binop(self, node):
        raise NotImplementedError("visit_binop must be implemented")
    
    def visit_assign(self, node):
        raise NotImplementedError("visit_assign must be implemented")
    
    def visit_print(self, node):
        raise NotImplementedError("visit_print must be implemented")
    
    def visit_comparison(self, node):
        raise NotImplementedError("visit_comparison must be implemented")
    
    def visit_logicalop(self, node):
        raise NotImplementedError("visit_logicalop must be implemented")
    
    def visit_not(self, node):
        raise NotImplementedError("visit_not must be implemented")
    
    def visit_if(self, node):
        raise NotImplementedError("visit_if must be implemented")
    
    def visit_while(self, node):
        raise NotImplementedError("visit_while must be implemented")
    
    def visit_for(self, node):
        raise NotImplementedError("visit_for must be implemented")
    
    def visit_block(self, node):
        raise NotImplementedError("visit_block must be implemented")

class Num:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Num({self.value})"
    def accept(self, visitor):
        return visitor.visit_num(self)

class String:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"String({self.value})"
    def accept(self, visitor):
        return visitor.visit_string(self)

class Var:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Var({self.name})"
    def accept(self, visitor):
        return visitor.visit_var(self)

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left}, {self.op}, {self.right})"
    def accept(self, visitor):
        return visitor.visit_binop(self)

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"Assign({self.name}, {self.value})"
    def accept(self, visitor):
        return visitor.visit_assign(self)

class Print:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Print({self.value})"
    def accept(self, visitor):
        return visitor.visit_print(self)

class Comparison:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"Comparison({self.left}, {self.op}, {self.right})"
    def accept(self, visitor):
        return visitor.visit_comparison(self)

class LogicalOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"LogicalOp({self.left}, {self.op}, {self.right})"
    def accept(self, visitor):
        return visitor.visit_logicalop(self)

class Not:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"Not({self.expr})"
    def accept(self, visitor):
        return visitor.visit_not(self)

class If:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        return f"If({self.condition}, {self.then_branch}, {self.else_branch})"
    def accept(self, visitor):
        return visitor.visit_if(self)

class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"While({self.condition}, {self.body})"
    def accept(self, visitor):
        return visitor.visit_while(self)

class For:
    def __init__(self, variable, start, end, body):
        self.variable = variable
        self.start = start
        self.end = end
        self.body = body
    def __repr__(self):
        return f"For({self.variable}, {self.start}, {self.end}, {self.body})"
    def accept(self, visitor):
        return visitor.visit_for(self)

class Block:
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"Block({self.statements})"
    def accept(self, visitor):
        return visitor.visit_block(self)