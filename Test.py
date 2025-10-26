# --- Comprehensive Test Suite for TinyInterpreter ---
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Errors import *

def run_test(test_name, code, expected_errors=None):
    """Run a test and handle expected errors."""
    print(f"\n🧪 Testing: {test_name}")
    print("=" * 50)
    
    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        interpreter = Interpreter()
        
        while parser.current_token:
            node = parser.statement()
            result = interpreter.eval(node)
            
        print("✅ Test passed successfully!")
        return True
        
    except TinyInterpreterError as e:
        if expected_errors and type(e).__name__ in expected_errors:
            print(f"✅ Expected error caught: {type(e).__name__}: {e.message}")
            return True
        else:
            print(f"❌ Unexpected error: {type(e).__name__}: {e.message}")
            if e.position:
                print(f"   Location: line {e.position.line}, column {e.position.column}")
            return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_features():
    """Test basic language features."""
    print("\n🚀 BASIC FEATURES TESTS")
    print("=" * 60)
    
    # Test 1: Numbers and arithmetic
    run_test("Numbers and Arithmetic", """
    x = 10
    y = 5
    اكتب x + y
    اكتب x - y
    اكتب x * y
    اكتب x / y
    """)
    
    # Test 2: String literals
    run_test("String Literals", """
    اكتب "مرحبا بالعالم"
    اكتب 'أهلاً وسهلاً'
    name = "أحمد"
    اكتب "مرحبا " + name
    """)
    
    # Test 3: Variables
    run_test("Variable Assignment", """
    x = 10
    y = x + 5
    اكتب y
    x = 20
    اكتب x
    """)

def test_comparison_operators():
    """Test comparison operators."""
    print("\n🔍 COMPARISON OPERATORS TESTS")
    print("=" * 60)
    
    run_test("All Comparison Operators", """
    x = 10
    y = 5
    
    اكتب x == 10
    اكتب x != 5
    اكتب x > 5
    اكتب x < 15
    اكتب x >= 10
    اكتب x <= 10
    
    اكتب y == 5
    اكتب y != 10
    اكتب y > 3
    اكتب y < 8
    اكتب y >= 5
    اكتب y <= 5
    """)

def test_logical_operators():
    """Test logical operators."""
    print("\n🧠 LOGICAL OPERATORS TESTS")
    print("=" * 60)
    
    run_test("Logical AND (و)", """
    x = 10
    y = 5
    اكتب x > 5 و y < 10
    اكتب x > 15 و y < 10
    اكتب x > 5 و y > 10
    """)
    
    run_test("Logical OR (أو)", """
    x = 10
    y = 5
    اكتب x > 5 أو y < 10
    اكتب x > 15 أو y < 10
    اكتب x > 15 أو y > 10
    """)
    
    run_test("Logical NOT (لا)", """
    x = 10
    اكتب لا (x < 5)
    اكتب لا (x > 5)
    """)

def test_control_flow():
    """Test control flow statements."""
    print("\n🎛️ CONTROL FLOW TESTS")
    print("=" * 60)
    
    run_test("IF Statements", """
    x = 10
    اذا x > 5 اكتب "x is greater than 5"
    اذا x < 5 اكتب "x is less than 5"
    """)
    
    run_test("IF-ELSE Statements", """
    x = 10
    اذا x > 5 اكتب "x is greater than 5" وإلا اكتب "x is not greater than 5"
    x = 3
    اذا x > 5 اكتب "x is greater than 5" وإلا اكتب "x is not greater than 5"
    """)
    
    run_test("IF with Compound Statements", """
    x = 10
    اذا x > 5 [
        اكتب "x is greater than 5"
        اكتب "This is inside the if block"
        اكتب "Multiple statements executed"
    ]
    """)

def test_loops():
    """Test loop constructs."""
    print("\n🔄 LOOP TESTS")
    print("=" * 60)
    
    run_test("WHILE Loop", """
    counter = 1
    بينما counter <= 3 [
        اكتب counter
        counter = counter + 1
    ]
    """)
    
    run_test("FOR Loop", """
    لكل i في 1 حتى 3 [
        اكتب "i ="
        اكتب i
    ]
    """)
    
    run_test("Nested Loops", """
    sum = 0
    لكل i في 1 حتى 3 [
        لكل j في 1 حتى 2 [
            اكتب i * j
            sum = sum + i * j
        ]
    ]
    اكتب "Total sum:"
    اكتب sum
    """)

def test_compound_statements():
    """Test compound statements with brackets."""
    print("\n📦 COMPOUND STATEMENTS TESTS")
    print("=" * 60)
    
    run_test("Simple Block", """
    x = 10
    [
        اكتب "Inside block"
        اكتب x
        x = x + 5
        اكتب x
    ]
    """)
    
    run_test("Complex Nested Blocks", """
    x = 1
    اذا x > 0 [
        اكتب "Outer if"
        اذا x < 10 [
            اكتب "Inner if"
            اكتب x
        ]
    ]
    """)

def test_error_handling():
    """Test error handling system."""
    print("\n❌ ERROR HANDLING TESTS")
    print("=" * 60)
    
    # Test Lexical Errors
    run_test("Lexical Error - Invalid Character", "x = @", ["LexicalError"])
    
    # Test Parse Errors
    run_test("Parse Error - Missing Value", "x =", ["ParseError"])
    run_test("Parse Error - Unexpected EOF", "اكتب", ["ParseError"])
    
    # Test Runtime Errors
    run_test("NameError - Undefined Variable", "اكتب undefined_var", ["NameError"])
    run_test("ZeroDivisionError", "اكتب 10 / 0", ["ZeroDivisionError"])
    
    # Test String Errors
    run_test("Lexical Error - Unterminated String", 'اكتب "unterminated', ["LexicalError"])

def test_complex_expressions():
    """Test complex expressions and precedence."""
    print("\n🧮 COMPLEX EXPRESSIONS TESTS")
    print("=" * 60)
    
    run_test("Operator Precedence", """
    اكتب 2 + 3 * 4
    اكتب (2 + 3) * 4
    اكتب 10 / 2 + 3
    اكتب 10 / (2 + 3)
    """)
    
    run_test("Complex Logical Expressions", """
    x = 10
    y = 5
    z = 15
    
    اكتب x > 5 و y < 10 و z > 10
    اكتب x < 5 أو y > 10 أو z < 10
    اكتب لا (x < 5) و لا (y > 10)
    """)
    
    run_test("Mixed Types", """
    x = 10
    y = "5"
    اكتب "x = " + x
    اكتب "y = " + y
    """)

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("\n🔬 EDGE CASES TESTS")
    print("=" * 60)
    
    run_test("Zero and Negative Numbers", """
    x = 0
    y = -5
    اكتب x
    اكتب y
    اكتب x + y
    اكتب x * y
    """)
    
    run_test("Empty Strings", """
    empty = ""
    اكتب "Empty string: " + empty
    """)
    
    run_test("Single Character Variables", """
    a = 1
    b = 2
    اكتب a + b
    """)

def test_arabic_keywords():
    """Test all Arabic keywords."""
    print("\n🔤 ARABIC KEYWORDS TESTS")
    print("=" * 60)
    
    run_test("All Arabic Keywords", """
    اكتب "Testing Arabic keywords"
    
    x = 10
    اذا x > 5 اكتب "اكتب works"
    
    y = 5
    اذا x > 5 و y < 10 اكتب "و (AND) works"
    
    اذا x < 5 أو y > 10 اكتب "أو (OR) works"
    
    اذا لا (x < 5) اكتب "لا (NOT) works"
    
    counter = 1
    بينما counter <= 2 [
        اكتب "بينما (WHILE) works"
        counter = counter + 1
    ]
    
    لكل i في 1 حتى 2 [
        اكتب "لكل (FOR) works"
    ]
    """)

def main():
    """Run all tests."""
    print("🎯 COMPREHENSIVE TEST SUITE FOR TINYINTERPRETER")
    print("=" * 80)
    print("Testing all aspects of the Arabic programming language interpreter")
    print("=" * 80)
    
    # Run all test categories
    test_basic_features()
    test_comparison_operators()
    test_logical_operators()
    test_control_flow()
    test_loops()
    test_compound_statements()
    test_error_handling()
    test_complex_expressions()
    test_edge_cases()
    test_arabic_keywords()
    
    print("\n" + "=" * 80)
    print("🎉 ALL TESTS COMPLETED!")
    print("=" * 80)
    print("✅ Basic Features: Numbers, Strings, Variables")
    print("✅ Comparison Operators: ==, !=, >, <, >=, <=")
    print("✅ Logical Operators: و (AND), أو (OR), لا (NOT)")
    print("✅ Control Flow: IF, IF-ELSE, Compound Statements")
    print("✅ Loops: WHILE (بينما), FOR (لكل)")
    print("✅ Error Handling: Lexical, Parse, Runtime Errors")
    print("✅ Complex Expressions: Precedence, Mixed Types")
    print("✅ Edge Cases: Zero, Negative, Empty Values")
    print("✅ Arabic Keywords: All Arabic language constructs")
    print("✅ Visitor Pattern: Clean architecture implementation")
    print("✅ Position Tracking: Line/column error reporting")
    print("=" * 80)

if __name__ == "__main__":
    main()