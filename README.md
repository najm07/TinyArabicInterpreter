# TinyInterpreter - Arabic Programming Language Interpreter

A simple yet powerful interpreter for an Arabic programming language, built from scratch in Python. This project demonstrates the fundamentals of compiler design including lexical analysis, parsing, and interpretation.

## 🌟 Features

### **Arithmetic Operations**
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Parentheses for grouping: `(expression)`
- Negative numbers: `-5`, `-10`

### **Variables**
- Variable assignment: `variable = value`
- Variable referencing in expressions
- Dynamic typing
- Support for underscores in variable names

### **String Literals**
- Double quotes: `"مرحبا بالعالم"`
- Single quotes: `'هذا نص'`
- Full Unicode support for Arabic text
- String concatenation with mixed types

### **Comparison Operators**
- Equality: `==`
- Inequality: `!=`
- Greater than: `>`
- Less than: `<`
- Greater than or equal: `>=`
- Less than or equal: `<=`

### **Logical Operators (Arabic)**
- AND: `و` (Arabic "و")
- OR: `أو` (Arabic "أو")
- NOT: `لا` (Arabic "لا")

### **Control Flow**
- IF statements: `اذا condition statement`
- IF-ELSE statements: `اذا condition statement وإلا statement`
- Compound statements: `[ statement1 statement2 ... ]`
- WHILE loops: `بينما condition [ statements ]`
- FOR loops: `لكل variable في start حتى end [ statements ]`

### **Output**
- Print statements: `اكتب expression`

### **Error Handling**
- **Structured Error System**: Professional-grade error reporting
- **Position Tracking**: Exact line/column information for errors
- **Error Types**: LexicalError, ParseError, NameError, ZeroDivisionError, etc.
- **Visual Error Context**: Beautiful error display with pointers
- **Graceful Recovery**: Errors don't crash the interpreter

### **Interactive REPL**
- **Real-time execution**: Type code and see results immediately
- **Multi-line support**: Use square brackets `[]` for compound statements
- **Variable persistence**: Variables remain available across commands
- **Error handling**: Clear error messages with graceful recovery
- **Special commands**: Built-in utilities for debugging and navigation
- **Arabic commands**: Use Arabic keywords for REPL commands

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation
```bash
git clone https://github.com/najm07/TinyArabicInterpreter.git
cd TinyArabicInterpreter
```

### Interactive REPL

**Option 1: Terminal REPL**
```bash
python REPL.py
```

**Option 2: Web Interface (Recommended for Arabic RTL support)**
```bash
cd web
pip install -r requirements.txt
python app.py
```
Then open `http://localhost:5000` in your browser.

The REPL provides an interactive environment where you can:
- Type Arabic code line by line
- See results immediately
- Use special commands (`help`/`مساعدة`, `vars`/`متغيرات`, `clear`/`مسح`, `reset`/`إعادة`)
- Support for multi-line compound statements
- **Web interface**: Full RTL support for proper Arabic text display

### Programmatic Usage
```python
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

# Your Arabic code
code = """
x = 10
y = 5
اكتب x + y
اذا x > 5 اكتب "كبير"
اكتب x == 10 و y < 10

# Loops with compound statements
counter = 1
بينما counter <= 3 [
    اكتب counter
    counter = counter + 1
]

لكل i في 1 حتى 3 [
    اكتب "i ="
    اكتب i
]
"""

# Tokenize
lexer = Lexer(code)
tokens = lexer.tokenize()

# Parse and execute
parser = Parser(tokens)
interpreter = Interpreter()

while parser.current_token:
    node = parser.statement()
    interpreter.eval(node)
```

## 📝 Language Syntax

### **Basic Syntax**
```arabic
# Variable assignment
x = 10
y = "مرحبا"

# Arithmetic expressions
result = x + y * 2
اكتب result

# String literals
اكتب "مرحبا بالعالم"
اكتب 'هذا نص'
```

### **Comparison Operations**
```arabic
x = 10
y = 5

# Comparison operators
اكتب x > y        # True
اكتب x == 10      # True
اكتب x != y       # True
اكتب x >= 10      # True
اكتب y <= 5       # True
```

### **Logical Operations**
```arabic
x = 10
y = 5

# Logical operators
اكتب x > 5 و y < 10    # AND: True
اكتب x < 5 أو y > 10   # OR: False
اكتب لا (x < 5)        # NOT: True
```

### **Control Flow**
```arabic
x = 10

# IF statement
اذا x > 5 اكتب "كبير"

# IF-ELSE statement
اذا x == 10 اكتب "عشرة" إلا اكتب "ليس عشرة"

# IF with compound statements
اذا x > 3 [
    اكتب "x is greater than 3"
    اكتب "This is inside the if block"
]
```

### **Loops**
```arabic
# WHILE loop with compound statements
counter = 1
بينما counter <= 3 [
    اكتب counter
    counter = counter + 1
]

# FOR loop with compound statements
لكل i في 1 حتى 3 [
    اكتب "i ="
    اكتب i
]
```

## 🏗️ Architecture

The interpreter is built with a clean, modular architecture using the **Visitor Pattern** for separation of concerns:

### **1. Lexer (`Lexer.py`)**
- Tokenizes input text into tokens
- Handles Arabic keywords and Unicode text
- Supports string literals, numbers, and operators

### **2. Parser (`Parser.py`)**
- Builds Abstract Syntax Tree (AST) from tokens
- Implements operator precedence
- Handles control flow structures

### **3. AST Classes (`ASTClasses.py`)**
- Defines node types for the Abstract Syntax Tree
- Implements **Visitor Pattern** with `accept(visitor)` methods
- Includes: `Num`, `String`, `Var`, `BinOp`, `Comparison`, `LogicalOp`, `Not`, `If`, `While`, `For`, `Block`, `Assign`, `Print`
- Contains abstract `Visitor` base class

### **4. Interpreter (`Interpreter.py`)**
- Clean interface using visitor pattern
- Delegates evaluation to `InterpreterVisitor`
- No tight coupling with AST node internals

### **5. InterpreterVisitor (`InterpreterVisitor.py`)**
- Implements the `Visitor` interface
- Contains all evaluation logic
- Manages variable environment
- Executes program logic

### **🎯 Visitor Pattern Benefits**
- **Clean Architecture**: No tight coupling between interpreter and AST nodes
- **Single Responsibility**: Each visitor handles one specific concern
- **Easy Extension**: Add new visitors (type checker, optimizer, pretty printer) without modifying existing code
- **Better Testing**: Test each visitor independently
- **Maintainability**: Changes to evaluation logic don't affect AST structure

## 📁 Project Structure

```
TinyInterpreter/
├── Lexer.py              # Lexical analysis with position tracking
├── Parser.py             # Syntax analysis and parsing
├── ASTClasses.py         # Abstract Syntax Tree node definitions + Visitor Pattern
├── Interpreter.py         # Clean interpreter interface
├── InterpreterVisitor.py # Evaluation logic implementation
├── Errors.py             # Structured error system
├── REPL.py               # Interactive Read-Eval-Print Loop
├── Test.py               # Comprehensive test suite
├── README.md             # This file
├── CONTRIBUTING.md       # Contribution guidelines
└── ARCHITECTURE.md       # Technical architecture documentation
```

## 🧪 Example Programs

### **Calculator**
```arabic
a = 10
b = 5
اكتب a + b
اكتب a * b
اكتب a / b
```

### **Conditional Logic**
```arabic
age = 18
اذا age >= 18 اكتب "بالغ" إلا اكتب "قاصر"
```

### **String Operations**
```arabic
name = "أحمد"
اكتب "مرحبا " + name
اكتب 'أهلاً وسهلاً'
```

### **Compound Statements**
```arabic
# Use square brackets for multiple statements
x = 10
اذا x > 5 [
    اكتب "x is greater than 5"
    اكتب "This is a compound statement"
    اكتب "Multiple statements in one block"
]

# Works with all control structures
counter = 1
بينما counter <= 3 [
    اكتب "Counter:"
    اكتب counter
    counter = counter + 1
]
```

### **Complex Logic**
```arabic
x = 10
y = 5
z = 15

اذا x > 5 و y < 10 اكتب "الشرط الأول صحيح"
اذا x == 10 أو z > 20 اكتب "الشرط الثاني صحيح"
اكتب لا (x < 5)
```

### **Loop Examples**
```arabic
# Countdown with while loop
count = 5
بينما count > 0 [
    اكتب "العد التنازلي:"
    اكتب count
    count = count - 1
]

# Sum numbers with for loop
sum = 0
لكل i في 1 حتى 5 [
    اكتب "إضافة"
    اكتب i
    sum = sum + i
]
اكتب "المجموع:"
اكتب sum
```

## 🔧 Development

### **Adding New Features**
1. **Lexer**: Add token recognition in `get_next_token()`
2. **Parser**: Add grammar rules in appropriate precedence level
3. **AST**: Create new AST node classes with `accept(visitor)` method
4. **Visitor**: Add visit method to `Visitor` base class
5. **InterpreterVisitor**: Implement evaluation logic in appropriate visit method

### **Adding New Visitors**
The Visitor Pattern makes it easy to add new functionality:

```python
# Example: Type Checker Visitor
class TypeCheckerVisitor(Visitor):
    def visit_num(self, node):
        return "number"
    
    def visit_string(self, node):
        return "string"
    
    # ... implement other visit methods

# Usage
type_checker = TypeCheckerVisitor()
node_type = ast_node.accept(type_checker)
```

### **Benefits of Visitor Pattern**
- **Separation of Concerns**: Evaluation logic separate from AST structure
- **Extensibility**: Easy to add new visitors (pretty printer, optimizer, type checker)
- **Maintainability**: Each visitor focuses on one responsibility
- **Testability**: Can test visitors independently

### **Testing**
```bash
# Run comprehensive test suite
python Test.py

# Start interactive REPL
python REPL.py
```

### **Comprehensive Test Suite**
The test suite covers all aspects of the interpreter:
- ✅ **Basic Features**: Numbers, Strings, Variables
- ✅ **Comparison Operators**: All comparison operations
- ✅ **Logical Operators**: Arabic AND, OR, NOT
- ✅ **Control Flow**: IF, IF-ELSE, Compound Statements
- ✅ **Loops**: WHILE and FOR loops with nesting
- ✅ **Error Handling**: All error types with position tracking
- ✅ **Complex Expressions**: Operator precedence, mixed types
- ✅ **Edge Cases**: Zero, negative numbers, empty values
- ✅ **Arabic Keywords**: All Arabic language constructs
- ✅ **Visitor Pattern**: Clean architecture validation

### **Error System**
The interpreter features a professional-grade error system:
- **Structured Errors**: Specific error types (LexicalError, ParseError, NameError, etc.)
- **Position Tracking**: Exact line and column information for all errors
- **Visual Context**: Beautiful error display with code context and pointers
- **Graceful Recovery**: Errors don't crash the interpreter or REPL

**Example Error Display:**
```
❌ LexicalError: Unexpected character: @
📍 Location: line 1, column 5

📝 Context:
   1 | x = @
          ^
```

### **REPL Features**
The interactive REPL provides:
- **Real-time execution**: Type code and see results immediately
- **Multi-line support**: Use square brackets `[]` for compound statements
- **Variable persistence**: Variables remain available across commands
- **Error handling**: Clear error messages with graceful recovery
- **Special commands**: Built-in utilities for debugging and navigation

### **REPL Commands**
- `help` / `مساعدة` - Show help and syntax examples
- `quit` / `خروج` - Exit the REPL
- `clear` / `مسح` - Clear the screen
- `vars` / `متغيرات` - Show all current variables
- `reset` / `إعادة` - Reset interpreter state

### **REPL Example Session**
```bash
>>> x = 10
>>> اكتب x
10
>>> اكتب x + 5
15
>>> اذا x > 5 اكتب "كبير"
كبير
>>> متغيرات
📊 Current Variables:
  x = 10
>>> خروج
👋 وداعاً! Goodbye!
```

## 📚 Educational Value

This project demonstrates:
- **Compiler Design**: Lexical analysis, parsing, and interpretation
- **Language Design**: Syntax design and operator precedence
- **AST Implementation**: Tree-based program representation
- **Visitor Pattern**: Clean separation of concerns and extensibility
- **Unicode Handling**: Arabic text processing
- **Object-Oriented Design**: Modular architecture with design patterns

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Najm** - [GitHub](https://github.com/najm07)

---

*Built with ❤️ for learning compiler design and Arabic programming languages*
