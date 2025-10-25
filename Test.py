# --- Full test ---
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

text = """
ش = 5 + 2 * 3
ع = ش - 4
ص = (ش + ع) * 2
اكتب ص
اكتب ش + ع
اكتب "مرحبا بالعالم"
اكتب 'هذا نص'
x = 8
y = 5
اذا x > 5 اكتب "كبير"
اذا x == 10 اكتب "عشرة" إلا اكتب "ليس عشرة"
اكتب x > 5 و y < 10
اكتب لا (x < 5)
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
