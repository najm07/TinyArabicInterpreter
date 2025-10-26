# --- REPL (Read-Eval-Print Loop) for TinyInterpreter ---

import sys
import io
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

class REPL:
    """Interactive Read-Eval-Print Loop for the Arabic interpreter."""
    
    def __init__(self):
        # Set UTF-8 encoding for stdout and stdin
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
        self.interpreter = Interpreter()
        self.buffer = ""  # For multi-line input
        self.in_block = False  # Track if we're inside a block
        
    def print_welcome(self):
        """Print welcome message and instructions."""
        print("=" * 60)
        print("🎉 مرحبا بك في مترجم اللغة العربية التفاعلي")
        print("🎉 Welcome to the Arabic Language Interpreter REPL")
        print("=" * 60)
        print("📝 Type Arabic code and press Enter to execute")
        print("📝 Type 'help' or 'مساعدة' for commands, 'quit' or 'خروج' to exit")
        print("📝 Use square brackets [] for compound statements")
        print("=" * 60)
        print()
    
    def print_help(self):
        """Print help information."""
        print("\n📚 Available Commands / الأوامر المتاحة:")
        print("  help / مساعدة     - Show this help message")
        print("  quit / خروج       - Exit the REPL")
        print("  clear / مسح       - Clear the screen")
        print("  vars / متغيرات     - Show all variables")
        print("  reset / إعادة     - Reset interpreter state")
        print("\n📝 Language Syntax / صيغة اللغة:")
        print("  اكتب expression     - Print expression")
        print("  variable = value     - Assign variable")
        print("  اذا condition statement - If statement")
        print("  بينما condition [ statements ] - While loop")
        print("  لكل var في start حتى end [ statements ] - For loop")
        print("\n📝 Examples / أمثلة:")
        print("  x = 10")
        print("  اكتب x + 5")
        print("  اذا x > 5 اكتب 'كبير'")
        print()
    
    def clear_screen(self):
        """Clear the screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_variables(self):
        """Show all current variables."""
        if not self.interpreter.variables:
            print("📭 No variables defined")
        else:
            print("📊 Current Variables:")
            for name, value in self.interpreter.variables.items():
                print(f"  {name} = {value}")
        print()
    
    def reset_interpreter(self):
        """Reset the interpreter state."""
        self.interpreter = Interpreter()
        self.buffer = ""
        self.in_block = False
        print("🔄 Interpreter reset successfully")
        print()
    
    def is_special_command(self, line):
        """Check if the line is a special REPL command."""
        line = line.strip().lower()
        # Support both English and Arabic commands
        english_commands = ['help', 'quit', 'exit', 'clear', 'vars', 'reset']
        arabic_commands = ['مساعدة', 'خروج', 'مسح', 'متغيرات', 'إعادة']
        
        return line in english_commands or line in arabic_commands
    
    def handle_special_command(self, line):
        """Handle special REPL commands."""
        command = line.strip().lower()
        
        # Quit/Exit commands
        if command in ['quit', 'exit', 'خروج']:
            print("👋 وداعاً! Goodbye!")
            return True
        # Help command
        elif command in ['help', 'مساعدة']:
            self.print_help()
        # Clear command
        elif command in ['clear', 'مسح']:
            self.clear_screen()
        # Variables command
        elif command in ['vars', 'متغيرات']:
            self.show_variables()
        # Reset command
        elif command in ['reset', 'إعادة']:
            self.reset_interpreter()
        
        return False
    
    def is_block_start(self, line):
        """Check if line starts a block (contains '[')."""
        return '[' in line and ']' not in line
    
    def is_block_end(self, line):
        """Check if line ends a block (contains ']')."""
        return ']' in line
    
    def process_input(self, line):
        """Process a single line of input."""
        line = line.strip()
        
        # Handle empty lines
        if not line:
            return
        
        # Handle special commands
        if self.is_special_command(line):
            return self.handle_special_command(line)
        
        # Add to buffer
        self.buffer += line + "\n"
        
        # Check if we're starting a block
        if self.is_block_start(line):
            self.in_block = True
            return False
        
        # Check if we're ending a block
        if self.is_block_end(line):
            self.in_block = False
        
        # If not in a block, execute immediately
        if not self.in_block:
            return self.execute_buffer()
        
        return False
    
    def execute_buffer(self):
        """Execute the current buffer."""
        if not self.buffer.strip():
            return False
        
        try:
            # Tokenize
            lexer = Lexer(self.buffer)
            tokens = lexer.tokenize()
            
            # Parse and execute
            parser = Parser(tokens)
            
            while parser.current_token:
                node = parser.statement()
                result = self.interpreter.eval(node)
                
                # Print result if it's not None and not a print statement
                from ASTClasses import Print
                if result is not None and not isinstance(node, Print):
                    print(f"📤 {result}")
            
            # Clear buffer after successful execution
            self.buffer = ""
            return False
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.buffer = ""  # Clear buffer on error
            return False
    
    def run(self):
        """Run the REPL."""
        self.print_welcome()
        
        try:
            while True:
                try:
                    # Show prompt
                    if self.in_block:
                        prompt = "  ... "
                    else:
                        prompt = ">>> "
                    
                    # Get input
                    line = input(prompt)
                    
                    # Process input
                    should_exit = self.process_input(line)
                    if should_exit:
                        break
                        
                except KeyboardInterrupt:
                    print("\n👋 Use 'quit' to exit")
                    self.buffer = ""
                    self.in_block = False
                except EOFError:
                    print("\n👋 Goodbye!")
                    break
                    
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def main():
    """Main function to start the REPL."""
    repl = REPL()
    repl.run()

if __name__ == "__main__":
    main()
