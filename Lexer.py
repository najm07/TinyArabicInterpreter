# --- Tiny Interpreter: Lexer Stage ---

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None

    def advance(self):
        """Move to the next character."""
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
        num_str = ""
        while self.current_char and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token("NUMBER", int(num_str))

    def string(self):
        """Return string literals like 'hello' or "world"."""
        quote_char = self.current_char  # Save the quote character (' or ")
        self.advance()  # Skip the opening quote
        
        result = ""
        while self.current_char and self.current_char != quote_char:
            result += self.current_char
            self.advance()
        
        if self.current_char == quote_char:
            self.advance()  # Skip the closing quote
        else:
            raise Exception(f"Unterminated string literal")
        
        return Token("STRING", result)

    def identifier(self):
        """Return variable names like 'x' or 'foo'."""
        result = ""
        while self.current_char and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        if result == "اكتب":
            return Token("PRINT", result)
        if result == "أو":
            return Token("OR", result)
        if result == "و":
            return Token("AND", result)
        if result == "لا":
            return Token("NOT", result)
        if result == "اذا":
            return Token("IF", result)
        if result == "وإلا":
            return Token("ELSE", result)
        if result == "بينما":
            return Token("WHILE", result)
        if result == "لكل":
            return Token("FOR", result)
        if result == "في":
            return Token("IN", result)
        if result == "حتى":
            return Token("UNTIL", result)

        return Token("IDENTIFIER", result)

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
                self.advance()
                return Token("PLUS", '+')

            if self.current_char == '-':
                self.advance()
                return Token("MINUS", '-')

            if self.current_char == '*':
                self.advance()
                return Token("STAR", '*')

            if self.current_char == '/':
                self.advance()
                return Token("SLASH", '/')

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("EQUAL_EQUAL", '==')
                return Token("EQUAL", '=')

            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("NOT_EQUAL", '!=')
                raise Exception(f"Unexpected character: !")

            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("GREATER_EQUAL", '>=')
                return Token("GREATER", '>')

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token("LESS_EQUAL", '<=')
                return Token("LESS", '<')

            if self.current_char == '(':
                self.advance()
                return Token("LPAREN", '(')

            if self.current_char == ')':
                self.advance()
                return Token("RPAREN", ')')

            if self.current_char == '[':
                self.advance()
                return Token("LBRACKET", '[')

            if self.current_char == ']':
                self.advance()
                return Token("RBRACKET", ']')

            if self.current_char == ';':
                self.advance()
                return Token("SEMICOLON", ';')

            raise Exception(f"Unexpected character: {self.current_char}")

        return Token("EOF", None)

    def tokenize(self):
        """Return a full list of tokens."""
        tokens = []
        while True:
            token = self.get_next_token()
            if token.type == "EOF":
                break
            tokens.append(token)
        return tokens
