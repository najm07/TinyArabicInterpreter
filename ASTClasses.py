# --- AST Node Classes ---

class Num:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Num({self.value})"

class String:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"String({self.value})"

class Var:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Var({self.name})"

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left}, {self.op}, {self.right})"

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"Assign({self.name}, {self.value})"

class Print:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Print({self.value})"

class Comparison:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"Comparison({self.left}, {self.op}, {self.right})"

class LogicalOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"LogicalOp({self.left}, {self.op}, {self.right})"

class Not:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"Not({self.expr})"

class If:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        return f"If({self.condition}, {self.then_branch}, {self.else_branch})"