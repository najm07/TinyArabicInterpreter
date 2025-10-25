# TinyInterpreter - Arabic Programming Language Interpreter

A simple yet powerful interpreter for an Arabic programming language, built from scratch in Python. This project demonstrates the fundamentals of compiler design including lexical analysis, parsing, and interpretation.

## 🌟 Features

### **Arithmetic Operations**
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Parentheses for grouping: `(expression)`

### **Variables**
- Variable assignment: `variable = value`
- Variable referencing in expressions
- Dynamic typing

### **String Literals**
- Double quotes: `"مرحبا بالعالم"`
- Single quotes: `'هذا نص'`
- Full Unicode support for Arabic text

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

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation
```bash
git clone https://github.com/najm07/TinyArabicInterpreter.git
cd TinyArabicInterpreter
```

### Usage
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

The interpreter is built with a classic three-stage architecture:

### **1. Lexer (`Lexer.py`)**
- Tokenizes input text into tokens
- Handles Arabic keywords and Unicode text
- Supports string literals, numbers, and operators

### **2. Parser (`Parser.py`)**
- Builds Abstract Syntax Tree (AST) from tokens
- Implements operator precedence
- Handles control flow structures

### **3. Interpreter (`Interpreter.py`)**
- Evaluates AST nodes
- Manages variable environment
- Executes program logic

### **4. AST Classes (`ASTClasses.py`)**
- Defines node types for the Abstract Syntax Tree
- Includes: `Num`, `String`, `Var`, `BinOp`, `Comparison`, `LogicalOp`, `Not`, `If`, `While`, `For`, `Block`, `Assign`, `Print`

## 📁 Project Structure

```
TinyInterpreter/
├── Lexer.py          # Lexical analysis
├── Parser.py         # Syntax analysis and parsing
├── ASTClasses.py     # Abstract Syntax Tree node definitions
├── Interpreter.py    # Program evaluation and execution
├── Test.py           # Example usage and testing
└── README.md         # This file
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
3. **AST**: Create new AST node classes
4. **Interpreter**: Add evaluation logic in `eval()` method

### **Testing**
```bash
python Test.py
```

## 📚 Educational Value

This project demonstrates:
- **Compiler Design**: Lexical analysis, parsing, and interpretation
- **Language Design**: Syntax design and operator precedence
- **AST Implementation**: Tree-based program representation
- **Unicode Handling**: Arabic text processing
- **Object-Oriented Design**: Modular architecture

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Najm** - [GitHub](https://github.com/najm07)

---

*Built with ❤️ for learning compiler design and Arabic programming languages*
