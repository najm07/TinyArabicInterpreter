# TinyInterpreter Architecture

This document provides a detailed technical overview of the TinyInterpreter architecture, design decisions, and implementation details.

## 🏗️ Overall Architecture

TinyInterpreter follows a classic three-stage compiler architecture with modern design patterns:

```
Source Code → Lexer → Parser → AST → Interpreter → Output
     ↓           ↓        ↓      ↓         ↓
   Arabic    Tokens   Syntax  Tree    Execution
   Text     + Pos    Tree   + Pos     + Errors
```

### **Design Principles**
- **Separation of Concerns**: Each stage has a single responsibility
- **Visitor Pattern**: Clean separation between AST structure and operations
- **Error Handling**: Structured errors with position tracking
- **Extensibility**: Easy to add new features and visitors
- **Maintainability**: Clean, readable, and well-documented code

## 📁 File Structure

```
TinyInterpreter/
├── Lexer.py              # Lexical analysis with position tracking
├── Parser.py             # Syntax analysis and AST construction
├── ASTClasses.py         # AST node definitions + Visitor Pattern
├── Interpreter.py         # Clean interpreter interface
├── InterpreterVisitor.py # Evaluation logic implementation
├── Errors.py             # Structured error system
├── REPL.py               # Interactive Read-Eval-Print Loop
├── Test.py               # Comprehensive test suite
├── README.md             # User documentation
├── CONTRIBUTING.md       # Contribution guidelines
└── ARCHITECTURE.md       # This file
```

## 🔍 Lexical Analysis (`Lexer.py`)

### **Purpose**
Converts source code text into a stream of tokens with position information.

### **Key Components**

#### **Token Class**
```python
class Token:
    def __init__(self, type_, value, position=None):
        self.type = type_      # Token type (NUMBER, STRING, etc.)
        self.value = value     # Token value
        self.position = position  # Position information
```

#### **Position Tracking**
```python
class Position:
    def __init__(self, line=1, column=1, index=0):
        self.line = line       # Line number (1-based)
        self.column = column   # Column number (1-based)
        self.index = index     # Character index (0-based)
```

### **Token Types**
- **Literals**: `NUMBER`, `STRING`
- **Identifiers**: `IDENTIFIER`
- **Keywords**: `اكتب`, `اذا`, `وإلا`, `بينما`, `لكل`, `في`, `حتى`
- **Operators**: `PLUS`, `MINUS`, `STAR`, `SLASH`, `EQUAL`
- **Comparisons**: `EQUAL_EQUAL`, `NOT_EQUAL`, `GREATER`, `LESS`, `GREATER_EQUAL`, `LESS_EQUAL`
- **Logical**: `AND`, `OR`, `NOT`
- **Punctuation**: `LPAREN`, `RPAREN`, `LBRACKET`, `RBRACKET`
- **Special**: `EOF`

### **Features**
- **Unicode Support**: Full Arabic text processing
- **Negative Numbers**: Unary minus handling
- **String Literals**: Both single and double quotes
- **Position Tracking**: Every token includes line/column info
- **Error Handling**: Structured lexical errors

## 🌳 Syntax Analysis (`Parser.py`)

### **Purpose**
Builds an Abstract Syntax Tree (AST) from tokens using recursive descent parsing.

### **Grammar**
```
program     → statement*
statement   → block_statement
           | if_statement
           | while_statement
           | for_statement
           | print_statement
           | assignment
           | expression

block_statement → '[' statement* ']'
if_statement    → 'اذا' expression statement ('وإلا' statement)?
while_statement → 'بينما' expression statement
for_statement   → 'لكل' IDENTIFIER 'في' expression 'حتى' expression statement
print_statement → 'اكتب' expression
assignment      → IDENTIFIER '=' expression
expression      → logical_or

logical_or      → logical_and ('أو' logical_and)*
logical_and     → comparison ('و' comparison)*
comparison      → expr (('=='|'!='|'>'|'<'|'>='|'<=') expr)*
expr            → term (('+'|'-') term)*
term            → factor (('*'|'/') factor)*
factor          → NUMBER | STRING | IDENTIFIER | 'لا' factor | '(' expression ')'
```

### **Operator Precedence** (highest to lowest)
1. `لا` (NOT)
2. `*`, `/`
3. `+`, `-`
4. `==`, `!=`, `>`, `<`, `>=`, `<=`
5. `و` (AND)
6. `أو` (OR)

### **Features**
- **Recursive Descent**: Clean, readable parsing logic
- **Error Recovery**: Graceful handling of syntax errors
- **Position Tracking**: AST nodes carry position information
- **Left Associativity**: Proper operator associativity

## 🌲 Abstract Syntax Tree (`ASTClasses.py`)

### **Purpose**
Defines the structure of the AST and implements the Visitor Pattern.

### **AST Node Types**

#### **Expression Nodes**
```python
class Num:           # Number literals
class String:        # String literals
class Var:           # Variable references
class BinOp:         # Binary operations (+, -, *, /)
class Comparison:    # Comparison operations (==, !=, >, <, >=, <=)
class LogicalOp:     # Logical operations (و, أو)
class Not:           # Logical NOT (لا)
```

#### **Statement Nodes**
```python
class Assign:        # Variable assignment
class Print:         # Print statements
class If:            # Conditional statements
class While:         # While loops
class For:           # For loops
class Block:         # Compound statements
```

### **Visitor Pattern Implementation**

#### **Base Visitor Class**
```python
class Visitor:
    def visit_num(self, node): raise NotImplementedError()
    def visit_string(self, node): raise NotImplementedError()
    # ... other visit methods
```

#### **Node Acceptance**
```python
class Num:
    def accept(self, visitor):
        return visitor.visit_num(self)
```

### **Benefits of Visitor Pattern**
- **Separation of Concerns**: AST structure separate from operations
- **Extensibility**: Easy to add new visitors (type checker, optimizer, etc.)
- **Maintainability**: Each visitor focuses on one responsibility
- **Testability**: Can test visitors independently

## ⚡ Interpretation (`Interpreter.py` + `InterpreterVisitor.py`)

### **Purpose**
Evaluates AST nodes to produce program output.

### **Architecture**
- **Interpreter**: Clean interface using visitor pattern
- **InterpreterVisitor**: Contains all evaluation logic

### **Evaluation Logic**

#### **Expression Evaluation**
```python
def visit_binop(self, node):
    left = node.left.accept(self)
    right = node.right.accept(self)
    
    if node.op == '+':
        # Handle string concatenation
        if isinstance(left, str) or isinstance(right, str):
            return str(left) + str(right)
        return left + right
    # ... other operators
```

#### **Control Flow**
```python
def visit_if(self, node):
    condition = node.condition.accept(self)
    if condition:
        return node.then_branch.accept(self)
    elif node.else_branch:
        return node.else_branch.accept(self)
    return None
```

#### **Loops**
```python
def visit_while(self, node):
    while node.condition.accept(self):
        node.body.accept(self)
    return None

def visit_for(self, node):
    start = node.start.accept(self)
    end = node.end.accept(self)
    for i in range(start, end + 1):
        self.variables[node.variable] = i
        node.body.accept(self)
    return None
```

### **Features**
- **Variable Environment**: Dictionary-based variable storage
- **Dynamic Typing**: Variables can hold any type
- **String Concatenation**: Automatic type conversion for strings
- **Error Handling**: Structured runtime errors

## ❌ Error System (`Errors.py`)

### **Purpose**
Provides structured error handling with position tracking and visual context.

### **Error Hierarchy**
```python
TinyInterpreterError (base)
├── SyntaxError
│   ├── LexicalError
│   └── ParseError
└── RuntimeError
    ├── NameError
    ├── TypeError
    ├── ZeroDivisionError
    └── ValueError
```

### **Position Tracking**
```python
class Position:
    def __init__(self, line=1, column=1, index=0):
        self.line = line
        self.column = column
        self.index = index
    
    def advance(self, char=None):
        # Update position based on character
```

### **Error Context**
```python
def create_error_context(text, position, context_lines=2):
    # Creates visual error context with line numbers and pointers
    # Example:
    #    1 | x = @
    #          ^
```

### **Features**
- **Structured Errors**: Specific error types for different situations
- **Position Information**: Exact line/column for all errors
- **Visual Context**: Beautiful error display with code context
- **Graceful Recovery**: Errors don't crash the interpreter

## 🖥️ Interactive REPL (`REPL.py`)

### **Purpose**
Provides an interactive environment for testing and experimentation.

### **Key Features**

#### **Multi-line Support**
- Detects block start/end with square brackets
- Maintains state across multiple lines
- Handles compound statements

#### **Special Commands**
- `help` / `مساعدة`: Show help
- `quit` / `خروج`: Exit REPL
- `clear` / `مسح`: Clear screen
- `vars` / `متغيرات`: Show variables
- `reset` / `إعادة`: Reset state

#### **Error Handling**
- Structured error display with context
- Graceful error recovery
- Clear error messages

#### **Arabic Support**
- Bilingual commands (English/Arabic)
- UTF-8 encoding handling
- Arabic text processing

### **Architecture**
```python
class REPL:
    def __init__(self):
        self.interpreter = Interpreter()
        self.buffer = ""
        self.in_block = False
    
    def process_input(self, line):
        # Handle special commands
        # Process multi-line input
        # Execute code
```

## 🧪 Testing (`Test.py`)

### **Purpose**
Comprehensive test suite covering all interpreter functionality.

### **Test Categories**
1. **Basic Features**: Numbers, strings, variables
2. **Comparison Operators**: All comparison operations
3. **Logical Operators**: Arabic AND, OR, NOT
4. **Control Flow**: IF, IF-ELSE, compound statements
5. **Loops**: WHILE and FOR loops
6. **Error Handling**: All error types
7. **Complex Expressions**: Operator precedence, mixed types
8. **Edge Cases**: Zero, negative numbers, empty values
9. **Arabic Keywords**: All Arabic constructs

### **Test Framework**
```python
def run_test(test_name, code, expected_errors=None):
    try:
        # Execute code
        # Check for expected errors
        return True
    except TinyInterpreterError as e:
        # Handle structured errors
        return False
```

## 🔧 Design Decisions

### **Why Visitor Pattern?**
- **Separation of Concerns**: AST structure separate from operations
- **Extensibility**: Easy to add new visitors (type checker, optimizer, etc.)
- **Maintainability**: Each visitor has a single responsibility
- **Testability**: Can test visitors independently

### **Why Position Tracking?**
- **Better Error Messages**: Exact location of errors
- **Debugging**: Easier to find and fix issues
- **User Experience**: Professional-grade error reporting
- **Tooling**: Enables IDE-like features

### **Why Structured Errors?**
- **Specific Error Types**: Different handling for different errors
- **Programmatic Handling**: Can catch specific error types
- **Better UX**: Clear, actionable error messages
- **Debugging**: Easier to understand what went wrong

### **Why Arabic Keywords?**
- **Cultural Relevance**: Makes programming accessible to Arabic speakers
- **Educational Value**: Demonstrates internationalization
- **Uniqueness**: Sets the project apart
- **Learning**: Shows how to handle Unicode in compilers

## 🚀 Performance Considerations

### **Current Performance**
- **Lexical Analysis**: O(n) where n is input length
- **Parsing**: O(n) recursive descent parsing
- **Interpretation**: O(n) tree traversal
- **Memory**: O(n) for AST storage

### **Optimization Opportunities**
- **Token Caching**: Cache frequently used tokens
- **AST Optimization**: Constant folding, dead code elimination
- **Bytecode Compilation**: Compile to bytecode for faster execution
- **JIT Compilation**: Just-in-time compilation for hot paths

## 🔮 Future Enhancements

### **Language Features**
- **Functions**: Function definitions and calls
- **Data Structures**: Arrays, dictionaries, objects
- **Modules**: Import/export functionality
- **Classes**: Object-oriented programming

### **Tooling**
- **Syntax Highlighting**: Editor support
- **Code Formatter**: Automatic code formatting
- **Debugger**: Step-through debugging
- **Profiler**: Performance analysis

### **Architecture Improvements**
- **Bytecode Compiler**: Compile to bytecode
- **Optimizer**: AST optimization passes
- **Type System**: Static type checking
- **Memory Management**: Garbage collection

## 📚 References

### **Compiler Design**
- "Crafting Interpreters" by Robert Nystrom
- "Compilers: Principles, Techniques, and Tools" (Dragon Book)
- "Modern Compiler Implementation" by Andrew Appel

### **Design Patterns**
- "Design Patterns" by Gang of Four
- "Clean Architecture" by Robert Martin
- "Refactoring" by Martin Fowler

### **Python Best Practices**
- PEP 8 Style Guide
- Python Design Patterns
- Testing with Python

---

This architecture document provides a comprehensive overview of TinyInterpreter's design and implementation. For specific implementation details, refer to the source code and inline documentation.
