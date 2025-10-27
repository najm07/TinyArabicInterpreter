# --- Flask Backend for Web REPL ---
import sys
import io
import os

# Add parent directory to path to import interpreter modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import unicodedata

# Import the interpreter components
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Errors import TinyInterpreterError

app = Flask(__name__)
CORS(app)  # Enable CORS for web requests

# Global interpreter instance for REPL state
interpreter = Interpreter()
input_buffer = ""
in_block = False

def normalize_arabic_text(text):
    """Normalize Unicode for Arabic text."""
    # Normalize to NFC (Canonical Composition)
    normalized = unicodedata.normalize('NFC', text)
    return normalized

@app.route('/')
def index():
    """Serve the main REPL interface."""
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    """Execute code and return result."""
    global interpreter, input_buffer, in_block
    
    try:
        data = request.json
        code = data.get('code', '')
        
        if not code:
            return jsonify({
                'success': False,
                'error': 'No code provided'
            })
        
        # Normalize Arabic text
        code = normalize_arabic_text(code)
        
        # Handle special commands
        code_lower = code.strip().lower()
        if code_lower in ['reset', 'إعادة']:
            interpreter = Interpreter()
            input_buffer = ""
            in_block = False
            return jsonify({
                'success': True,
                'output': '🔄 Interpreter reset successfully',
                'result': None
            })
        elif code_lower in ['vars', 'متغيرات']:
            if not interpreter.variables:
                return jsonify({
                    'success': True,
                    'output': '📭 No variables defined',
                    'result': None
                })
            else:
                vars_str = '\n'.join([f"{name} = {value}" for name, value in interpreter.variables.items()])
                return jsonify({
                    'success': True,
                    'output': f'📊 Current Variables:\n{vars_str}',
                    'result': None
                })
        
        # Add to buffer for multi-line support
        input_buffer += code + "\n"
        
        # Check for block start/end
        if '[' in code and ']' not in code:
            in_block = True
            return jsonify({
                'success': True,
                'output': '',
                'result': None,
                'continuing': True
            })
        
        if ']' in code:
            in_block = False
        
        # If not in a block, execute immediately
        if not in_block:
            result = execute_code(input_buffer)
            input_buffer = ""
            return result
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        })

def execute_code(code):
    """Execute code and return result."""
    global interpreter
    
    try:
        # Set UTF-8 encoding for output
        sys.stdout = io.StringIO()
        
        # Tokenize
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Parse and execute
        parser = Parser(tokens)
        output_lines = []
        
        while parser.current_token:
            node = parser.statement()
            result = interpreter.eval(node)
            # Capture any print output
            output = sys.stdout.getvalue()
            if output:
                output_lines.append(output.strip())
                sys.stdout = io.StringIO()  # Reset for next statement
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        return jsonify({
            'success': True,
            'output': '\n'.join(output_lines) if output_lines else '',
            'result': None
        })
    
    except TinyInterpreterError as e:
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        error_info = {
            'type': type(e).__name__,
            'message': e.message,
            'position': None
        }
        
        if e.position:
            error_info['position'] = {
                'line': e.position.line,
                'column': e.position.column
            }
        
        return jsonify({
            'success': False,
            'error': error_info
        })
    
    except Exception as e:
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        return jsonify({
            'success': False,
            'error': {
                'type': 'RuntimeError',
                'message': str(e),
                'position': None
            }
        })

@app.route('/variables', methods=['GET'])
def get_variables():
    """Get current variables."""
    global interpreter
    return jsonify({
        'success': True,
        'variables': interpreter.variables
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
