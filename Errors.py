# --- Error System for TinyInterpreter ---

class Position:
    """Represents a position in the source code."""
    
    def __init__(self, line=1, column=1, index=0):
        self.line = line
        self.column = column
        self.index = index
    
    def __repr__(self):
        return f"Position(line={self.line}, column={self.column})"
    
    def advance(self, char=None):
        """Advance position based on character."""
        self.index += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
    
    def copy(self):
        """Create a copy of this position."""
        return Position(self.line, self.column, self.index)

class ErrorRange:
    """Represents a range of positions in the source code."""
    
    def __init__(self, start, end=None):
        self.start = start
        self.end = end or start
    
    def __repr__(self):
        if self.start.line == self.end.line:
            return f"line {self.start.line}, columns {self.start.column}-{self.end.column}"
        else:
            return f"lines {self.start.line}-{self.end.line}"

class TinyInterpreterError(Exception):
    """Base class for all interpreter errors."""
    
    def __init__(self, message, position=None, range=None):
        super().__init__(message)
        self.message = message
        self.position = position
        self.range = range or (ErrorRange(position) if position else None)
    
    def __str__(self):
        if self.position:
            return f"{self.__class__.__name__} at {self.position}: {self.message}"
        return f"{self.__class__.__name__}: {self.message}"

class SyntaxError(TinyInterpreterError):
    """Syntax error in the source code."""
    pass

class LexicalError(SyntaxError):
    """Error during lexical analysis."""
    pass

class ParseError(SyntaxError):
    """Error during parsing."""
    pass

class RuntimeError(TinyInterpreterError):
    """Error during program execution."""
    pass

class NameError(RuntimeError):
    """Variable name not found."""
    pass

class TypeError(RuntimeError):
    """Type error during execution."""
    pass

class ZeroDivisionError(RuntimeError):
    """Division by zero error."""
    pass

class ValueError(RuntimeError):
    """Invalid value error."""
    pass

def create_error_context(text, position, context_lines=2):
    """Create error context with line numbers and pointer."""
    lines = text.split('\n')
    start_line = max(0, position.line - context_lines - 1)
    end_line = min(len(lines), position.line + context_lines)
    
    context = []
    for i in range(start_line, end_line):
        line_num = i + 1
        line_content = lines[i]
        context.append(f"{line_num:4d} | {line_content}")
        
        if line_num == position.line:
            # Add pointer to the error position
            pointer = " " * (6 + position.column - 1) + "^"
            context.append(pointer)
    
    return "\n".join(context)
