# --- Tiny Interpreter: Lexer Stage ---

from Errors import Position, LexicalError, create_error_context

class Token:
    def __init__(self, type_, value, position=None):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, {self.position})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None
        self.position = Position()  # Track line/column position

    def advance(self):
        """Move to the next character."""
        if self.current_char:
            self.position.advance(self.current_char)
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None  # End of input

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    

    def number(self):
        """Return a full number token (handles multi-digit)."""
        start_pos = self.position.copy()
        num_str = ""
        while self.current_char and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token("NUMBER", int(num_str), start_pos)

    def string(self):
        """Return string literals like 'hello' or "world"."""
        start_pos = self.position.copy()
        quote_char = self.current_char  # Save the quote character (' or ")
        self.advance()  # Skip the opening quote
        
        result = ""
        while self.current_char and self.current_char != quote_char:
            result += self.current_char
            self.advance()
        
        if self.current_char == quote_char:
            self.advance()  # Skip the closing quote
        else:
            raise LexicalError(f"Unterminated string literal", start_pos)
        
        return Token("STRING", result, start_pos)

    def identifier(self):
        """Return variable names like 'x' or 'foo'."""
        start_pos = self.position.copy()
        result = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result == "اكتب":
            return Token("PRINT", result, start_pos)
        if result == "أو":
            return Token("OR", result, start_pos)
        if result == "و":
            return Token("AND", result, start_pos)
        if result == "لا":
            return Token("NOT", result, start_pos)
        if result == "اذا":
            return Token("IF", result, start_pos)
        if result == "وإلا":
            return Token("ELSE", result, start_pos)
        if result == "بينما":
            return Token("WHILE", result, start_pos)
        if result == "لكل":
            return Token("FOR", result, start_pos)
        if result == "في":
            return Token("IN", result, start_pos)
        if result == "حتى":
            return Token("UNTIL", result, start_pos)

        return Token("IDENTIFIER", result, start_pos)

    def get_next_token(self):
        """The main magic: returns the next token."""
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char in ('"', "'"):
                return self.string()

            if self.current_char == '+':
                pos = self.position.copy()
                self.advance()
                return Token("PLUS", '+', pos)

            if self.current_char == '-':
                pos = self.position.copy()
                self.advance()
                # Check if this is a unary minus (followed by a digit)
                if self.current_char and self.current_char.isdigit():
                    # This is a negative number, not a minus operator
                    num_str = "-"
                    while self.current_char and self.current_char.isdigit():
                        num_str += self.current_char
                        self.advance()
                    return Token("NUMBER", int(num_str), pos)
                return Token("MINUS", '-', pos)

            if self.current_char == '*':
                pos = self.position.copy()
                self.advance()
                return Token("STAR", '*', pos)

            if self.current_char == '/':
                pos = self.position.copy()
                self.advance()
                return Token("SLASH", '/', pos)

            if self.current_char == '=':
                pos = self.position.copy()
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("EQUAL_EQUAL", '==', pos)
                return Token("EQUAL", '=', pos)

            if self.current_char == '!':
                pos = self.position.copy()
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("NOT_EQUAL", '!=', pos)
                raise LexicalError(f"Unexpected character: !", pos)

            if self.current_char == '>':
                pos = self.position.copy()
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("GREATER_EQUAL", '>=', pos)
                return Token("GREATER", '>', pos)

            if self.current_char == '<':
                pos = self.position.copy()
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("LESS_EQUAL", '<=', pos)
                return Token("LESS", '<', pos)

            if self.current_char == '(':
                pos = self.position.copy()
                self.advance()
                return Token("LPAREN", '(', pos)

            if self.current_char == ')':
                pos = self.position.copy()
                self.advance()
                return Token("RPAREN", ')', pos)

            if self.current_char == '[':
                pos = self.position.copy()
                self.advance()
                return Token("LBRACKET", '[', pos)

            if self.current_char == ']':
                pos = self.position.copy()
                self.advance()
                return Token("RBRACKET", ']', pos)

            if self.current_char == ';':
                pos = self.position.copy()
                self.advance()
                return Token("SEMICOLON", ';', pos)

            pos = self.position.copy()
            raise LexicalError(f"Unexpected character: {self.current_char}", pos)

        return Token("EOF", None, self.position.copy())

    def tokenize(self):
        """Return a full list of tokens."""
        tokens = []
        while True:
            token = self.get_next_token()
            if token.type == "EOF":
                break
            tokens.append(token)
        return tokens
