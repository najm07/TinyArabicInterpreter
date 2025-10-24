# --- Full test ---
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

text = """
ش = 5 + 2 * 3
ع = ش - 4
ص = (ش + ع) * 2
اكتب ص
اكتب ش + ع
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
