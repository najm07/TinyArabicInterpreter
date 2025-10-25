# --- Full test ---
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

text = """
اكتب "مرحبا بالعالم"
اكتب "بداية البرنامج"

اكتب "If statement test:"
x = 5
اذا x > 3 [
    اكتب "x is greater than 3"
    اكتب "This is inside the if block"
]

اكتب "For loop test:"
لكل i في 1 حتى 3 [
    اكتب "i ="
    اكتب i
]

اكتب "While loop test:"
counter = 1
بينما counter <= 3 [
    اكتب counter
    counter = counter + 1
]

اكتب "نهاية البرنامج"
"""

lexer = Lexer(text)
tokens = lexer.tokenize()

# Parse one statement at a time
parser = Parser(tokens)
interpreter = Interpreter()

while parser.current_token:
    node = parser.statement()
    result = interpreter.eval(node)

print("Variables:", interpreter.variables)
