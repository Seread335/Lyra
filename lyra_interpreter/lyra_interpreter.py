#!/usr/bin/env python3
"""
LYRA INTERPRETER - Python Implementation
A working Lyra interpreter that executes .lyra programs
"""

import sys
from enum import Enum
from typing import Any, List, Optional

# ============================================================================
# LEXER - TOKENIZE INPUT
# ============================================================================

class TokenType(Enum):
    EOF = 0
    NUMBER = 1
    STRING = 2
    IDENTIFIER = 3
    KEYWORD = 4
    OPERATOR = 5
    LPAREN = 6
    RPAREN = 7
    LBRACE = 8
    RBRACE = 9
    SEMICOLON = 10
    COLON = 11
    COMMA = 12
    EQUALS = 13
    LBRACKET = 14
    RBRACKET = 15

class Token:
    def __init__(self, type: TokenType, value: str, line: int = 1):
        self.type = type
        self.value = value
        self.line = line
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r})"

class Lexer:
    KEYWORDS = {'var', 'proc', 'if', 'else', 'while', 'for', 'return', 
                'true', 'false', 'print', 'break', 'continue', 'in'}
    OPERATORS = {'+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=',
                 '&&', '||', '!', '=', '+=', '-=', '*=', '/='}
    
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.tokens: List[Token] = []
    
    def peek(self, offset: int = 0) -> str:
        pos = self.pos + offset
        if pos < len(self.code):
            return self.code[pos]
        return ''
    
    def next(self) -> str:
        if self.pos < len(self.code):
            char = self.code[self.pos]
            if char == '\n':
                self.line += 1
            self.pos += 1
            return char
        return ''
    
    def skip_whitespace(self):
        while self.pos < len(self.code) and self.code[self.pos].isspace():
            self.next()
    
    def scan_string(self):
        quote = self.next()  # Skip opening quote
        value = ''
        while self.pos < len(self.code) and self.code[self.pos] != quote:
            if self.code[self.pos] == '\\':
                self.next()
                char = self.next()
                if char == 'n':
                    value += '\n'
                elif char == 't':
                    value += '\t'
                else:
                    value += char
            else:
                value += self.next()
        
        if self.pos < len(self.code):
            self.next()  # Skip closing quote
        return value
    
    def scan_number(self) -> str:
        value = ''
        while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == '.'):
            value += self.next()
        return value
    
    def scan_identifier(self) -> str:
        value = ''
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
            value += self.next()
        return value
    
    def add_token(self, type: TokenType, value: str = ''):
        self.tokens.append(Token(type, value, self.line))
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.code):
            self.skip_whitespace()
            
            if self.pos >= len(self.code):
                break
            
            char = self.peek()
            
            # Comments
            if char == '/' and self.peek(1) == '/':
                while self.pos < len(self.code) and self.code[self.pos] != '\n':
                    self.next()
                continue
            
            # Strings
            if char in ('"', "'"):
                value = self.scan_string()
                self.add_token(TokenType.STRING, value)
            
            # Numbers
            elif char.isdigit():
                value = self.scan_number()
                self.add_token(TokenType.NUMBER, value)
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                value = self.scan_identifier()
                if value in self.KEYWORDS:
                    self.add_token(TokenType.KEYWORD, value)
                else:
                    self.add_token(TokenType.IDENTIFIER, value)
            
            # Operators and punctuation
            elif char == '(':
                self.next()
                self.add_token(TokenType.LPAREN, '(')
            elif char == ')':
                self.next()
                self.add_token(TokenType.RPAREN, ')')
            elif char == '{':
                self.next()
                self.add_token(TokenType.LBRACE, '{')
            elif char == '}':
                self.next()
                self.add_token(TokenType.RBRACE, '}')
            elif char == '[':
                self.next()
                self.add_token(TokenType.LBRACKET, '[')
            elif char == ']':
                self.next()
                self.add_token(TokenType.RBRACKET, ']')
            elif char == ';':
                self.next()
                self.add_token(TokenType.SEMICOLON, ';')
            elif char == ':':
                self.next()
                self.add_token(TokenType.COLON, ':')
            elif char == ',':
                self.next()
                self.add_token(TokenType.COMMA, ',')
            elif char == '=' and self.peek(1) == '=':
                self.next()
                self.next()
                self.add_token(TokenType.OPERATOR, '==')
            elif char == '!':
                self.next()
                if self.peek() == '=':
                    self.next()
                    self.add_token(TokenType.OPERATOR, '!=')
                else:
                    self.add_token(TokenType.OPERATOR, '!')
            elif char == '-':
                self.next()
                if self.peek() == '=':
                    self.next()
                    self.add_token(TokenType.OPERATOR, '-=')
                elif self.peek() == '>':
                    self.next()
                    self.add_token(TokenType.OPERATOR, '->')
                else:
                    self.add_token(TokenType.OPERATOR, '-')
            elif char == '<':
                self.next()
                if self.peek() == '=':
                    self.next()
                    self.add_token(TokenType.OPERATOR, '<=')
                else:
                    self.add_token(TokenType.OPERATOR, '<')
            elif char == '>':
                self.next()
                if self.peek() == '=':
                    self.next()
                    self.add_token(TokenType.OPERATOR, '>=')
                else:
                    self.add_token(TokenType.OPERATOR, '>')
            elif char == '&' and self.peek(1) == '&':
                self.next()
                self.next()
                self.add_token(TokenType.OPERATOR, '&&')
            elif char == '|' and self.peek(1) == '|':
                self.next()
                self.next()
                self.add_token(TokenType.OPERATOR, '||')
            elif char in '+*/%':
                op = self.next()
                if self.peek() == '=':
                    op += self.next()
                self.add_token(TokenType.OPERATOR, op)
            elif char == '=':
                self.next()
                self.add_token(TokenType.EQUALS, '=')
            else:
                self.next()
        
        self.add_token(TokenType.EOF, '')
        return self.tokens

# ============================================================================
# PARSER - BUILD AST
# ============================================================================

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements: List[Any]) -> None:
        self.statements = statements

class VarDecl(ASTNode):
    def __init__(self, name: str, type: str, value: Any) -> None:
        self.name = name
        self.type = type
        self.value = value

class Assignment(ASTNode):
    def __init__(self, name: str, value: Any) -> None:
        self.name = name
        self.value = value

class BinOp(ASTNode):
    def __init__(self, left: Any, op: str, right: Any) -> None:
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, op: str, operand: Any) -> None:
        self.op = op
        self.operand = operand

class Number(ASTNode):
    def __init__(self, value: Any) -> None:
        self.value = float(value)

class String(ASTNode):
    def __init__(self, value: str) -> None:
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name: str) -> None:
        self.name = name

class CallExpr(ASTNode):
    def __init__(self, name: str, args: List[Any]) -> None:
        self.name = name
        self.args = args

class IfStmt(ASTNode):
    def __init__(self, condition: Any, then_branch: Any, else_branch: Optional[Any]=None) -> None:
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStmt(ASTNode):
    def __init__(self, condition: Any, body: List[Any]) -> None:
        self.condition = condition
        self.body = body

class FunctionDef(ASTNode):
    def __init__(self, name: str, params: List[str], return_type: str, body: List[Any]) -> None:
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body

class ReturnStmt(ASTNode):
    def __init__(self, value: Any) -> None:
        self.value = value

class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.pos = 0
    
    def peek(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]  # EOF
    
    def next(self) -> Token:
        token = self.peek()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token
    
    def expect(self, type: TokenType) -> Token:
        token = self.peek()
        if token.type != type:
            raise SyntaxError(f"Expected {type.name}, got {token.type.name}")
        return self.next()
    
    def parse(self) -> Program:
        statements: List[Any] = []
        while self.peek().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)
    
    def parse_statement(self) -> Any:
        if self.peek().type == TokenType.KEYWORD:
            keyword = self.peek().value
            if keyword == 'var':
                return self.parse_var_decl()
            elif keyword == 'proc':
                return self.parse_proc()
            elif keyword == 'if':
                return self.parse_if()
            elif keyword == 'while':
                return self.parse_while()
            elif keyword == 'print':
                return self.parse_print()
            elif keyword == 'return':
                self.next()
                expr = self.parse_expression()
                if self.peek().type == TokenType.SEMICOLON:
                    self.next()
                return ReturnStmt(expr)
        
        # Try assignment
        if self.peek().type == TokenType.IDENTIFIER:
            name = self.next().value
            if self.peek().type == TokenType.EQUALS:
                self.next()
                value = self.parse_expression()
                if self.peek().type == TokenType.SEMICOLON:
                    self.next()
                return Assignment(name, value)
        
        # Try expression statement
        expr = self.parse_expression()
        if self.peek().type == TokenType.SEMICOLON:
            self.next()
        return expr
    
    def parse_var_decl(self):
        self.expect(TokenType.KEYWORD)  # 'var'
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.COLON)
        type_name = self.expect(TokenType.IDENTIFIER).value
        
        value = None
        if self.peek().type == TokenType.EQUALS:
            self.next()
            value = self.parse_expression()
        
        if self.peek().type == TokenType.SEMICOLON:
            self.next()
        
        return VarDecl(name, type_name, value)
    
    def parse_proc(self):
        self.expect(TokenType.KEYWORD)  # 'proc'
        name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LPAREN)
        params = []
        while self.peek().type != TokenType.RPAREN:
            param_name = self.expect(TokenType.IDENTIFIER).value
            if self.peek().type == TokenType.COLON:
                self.next()
                self.expect(TokenType.IDENTIFIER)  # parameter type
            params.append(param_name)
            if self.peek().type == TokenType.COMMA:
                self.next()
        self.expect(TokenType.RPAREN)
        
        return_type = "i32"
        if self.peek().type == TokenType.OPERATOR and self.peek().value == '->':
            self.next()
            return_type = self.expect(TokenType.IDENTIFIER).value
        
        body = self.parse_block() or []
        return FunctionDef(name, params, return_type, body)
    
    def parse_if(self):
        self.expect(TokenType.KEYWORD)  # 'if'
        condition = self.parse_expression()
        then_branch = self.parse_block() or []
        else_branch = None
        if self.peek().value == 'else':
            self.next()
            else_branch = self.parse_block() or []
        return IfStmt(condition, then_branch, else_branch)
    
    def parse_while(self):
        self.expect(TokenType.KEYWORD)  # 'while'
        condition = self.parse_expression()
        body = self.parse_block() or []
        return WhileStmt(condition, body)
    
    def parse_block(self) -> Optional[List[Any]]:
        if self.peek().type == TokenType.LBRACE:
            self.next()
            statements: List[Any] = []
            while self.peek().type != TokenType.RBRACE and self.peek().type != TokenType.EOF:
                stmt = self.parse_statement()
                if stmt:
                    statements.append(stmt)
            if self.peek().type == TokenType.RBRACE:
                self.next()
            return statements
        return None
    
    def parse_print(self) -> Any:
        self.expect(TokenType.KEYWORD)  # 'print'
        self.expect(TokenType.LPAREN)
        args: List[Any] = []
        while self.peek().type != TokenType.RPAREN:
            args.append(self.parse_expression())
            if self.peek().type == TokenType.COMMA:
                self.next()
        self.expect(TokenType.RPAREN)
        if self.peek().type == TokenType.SEMICOLON:
            self.next()
        return CallExpr('print', args)
    
    def parse_expression(self) -> Any:
        return self.parse_or()
    
    def parse_or(self) -> Any:
        left = self.parse_and()
        while self.peek().value == '||':
            op = self.next().value
            right = self.parse_and()
            left = BinOp(left, op, right)
        return left
    
    def parse_and(self) -> Any:
        left = self.parse_comparison()
        while self.peek().value == '&&':
            op = self.next().value
            right = self.parse_comparison()
            left = BinOp(left, op, right)
        return left
    
    def parse_comparison(self) -> Any:
        left = self.parse_additive()
        while self.peek().value in ('==', '!=', '<', '>', '<=', '>='):
            op = self.next().value
            right = self.parse_additive()
            left = BinOp(left, op, right)
        return left
    
    def parse_additive(self) -> Any:
        left = self.parse_multiplicative()
        while self.peek().value in ('+', '-'):
            op = self.next().value
            right = self.parse_multiplicative()
            left = BinOp(left, op, right)
        return left
    
    def parse_multiplicative(self) -> Any:
        left = self.parse_unary()
        while self.peek().value in ('*', '/', '%'):
            op = self.next().value
            right = self.parse_unary()
            left = BinOp(left, op, right)
        return left
    
    def parse_unary(self) -> Any:
        if self.peek().value in ('!', '-'):
            op = self.next().value
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        return self.parse_primary()
    
    def parse_primary(self):
        token = self.peek()
        
        if token.type == TokenType.NUMBER:
            self.next()
            return Number(token.value)
        
        elif token.type == TokenType.STRING:
            self.next()
            return String(token.value)
        
        elif token.type == TokenType.IDENTIFIER:
            name = self.next().value
            if self.peek().type == TokenType.LPAREN:
                # Function call
                self.next()
                args: List[Any] = []
                while self.peek().type != TokenType.RPAREN:
                    args.append(self.parse_expression())
                    if self.peek().type == TokenType.COMMA:
                        self.next()
                self.expect(TokenType.RPAREN)
                return CallExpr(name, args)
            else:
                return Identifier(name)
        
        elif token.type == TokenType.KEYWORD:
            if token.value in ('true', 'false'):
                self.next()
                return Number(1 if token.value == 'true' else 0)
        
        elif token.type == TokenType.LPAREN:
            self.next()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        raise SyntaxError(f"Unexpected token: {token}")

# ============================================================================
# INTERPRETER - EXECUTE AST
# ============================================================================

class Interpreter:
    def __init__(self) -> None:
        self.variables: dict[str, Any] = {}
        self.functions: dict[str, Any] = {}
    
    def interpret(self, ast: Program):
        for statement in ast.statements:
            result = self.execute(statement)
            if result is not None and isinstance(result, str) and result.startswith('RETURN:'):
                return result[7:]
        return None
    
    def execute(self, node: Any) -> Any:
        if isinstance(node, Program):
            return self.interpret(node)
        elif isinstance(node, VarDecl):
            value = self.evaluate(node.value) if node.value else 0
            self.variables[node.name] = value
            return None
        elif isinstance(node, Assignment):
            value = self.evaluate(node.value)
            self.variables[node.name] = value
            return None
        elif isinstance(node, FunctionDef):
            self.functions[node.name] = node
            return None
        elif isinstance(node, ReturnStmt):
            value = self.evaluate(node.value)
            return f"RETURN:{value}"
        elif isinstance(node, IfStmt):
            condition = self.evaluate(node.condition)
            if self.is_truthy(condition):
                for stmt in node.then_branch:
                    result = self.execute(stmt)
                    if result is not None and isinstance(result, str) and result.startswith('RETURN:'):
                        return result
            elif node.else_branch:
                for stmt in node.else_branch:
                    result = self.execute(stmt)
                    if result is not None and isinstance(result, str) and result.startswith('RETURN:'):
                        return result
            return None
        elif isinstance(node, WhileStmt):
            while self.is_truthy(self.evaluate(node.condition)):
                for stmt in node.body:
                    result = self.execute(stmt)
                    if result is not None and isinstance(result, str) and result.startswith('RETURN:'):
                        return result
            return None
        elif isinstance(node, CallExpr):
            if node.name == 'print':
                values = [str(self.evaluate(arg)) for arg in node.args]
                print(' '.join(values))
                return None
            else:
                # User-defined function
                if node.name in self.functions:
                    func_def = self.functions[node.name]
                    # Save current variables
                    saved_vars = self.variables.copy()
                    # Bind parameters
                    args = [self.evaluate(arg) for arg in node.args]
                    for i, param in enumerate(func_def.params):
                        if i < len(args):
                            self.variables[param] = args[i]
                    # Execute function body
                    result = 0
                    for stmt in func_def.body:
                        exec_result = self.execute(stmt)
                        if exec_result is not None and isinstance(exec_result, str) and exec_result.startswith('RETURN:'):
                            result = float(exec_result[7:])
                            break
                        # Last statement is return value if not explicitly returned
                        if isinstance(stmt, (BinOp, UnaryOp, Number, String, Identifier, CallExpr)):
                            result = self.evaluate(stmt)
                    # Restore variables
                    self.variables = saved_vars
                    return result
                return None
        elif isinstance(node, (BinOp, UnaryOp, Number, String, Identifier)):
            return self.evaluate(node)
        else:
            return None
    
    def evaluate(self, node: Any) -> Any:
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, Identifier):
            return self.variables.get(node.name, 0.0)
        elif isinstance(node, CallExpr):
            if node.name == 'print':
                values = [str(self.evaluate(arg)) for arg in node.args]
                print(' '.join(values))
                return 0.0
            elif node.name in self.functions:
                # Execute the function
                result = self.execute(node)
                return result if result is not None else 0.0
            return 0.0
        elif isinstance(node, BinOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right if right != 0 else 0.0
            elif node.op == '%':
                return float(int(left) % int(right)) if right != 0 else 0.0
            elif node.op == '==':
                return 1.0 if left == right else 0.0
            elif node.op == '!=':
                return 1.0 if left != right else 0.0
            elif node.op == '<':
                return 1.0 if left < right else 0.0
            elif node.op == '>':
                return 1.0 if left > right else 0.0
            elif node.op == '<=':
                return 1.0 if left <= right else 0.0
            elif node.op == '>=':
                return 1.0 if left >= right else 0.0
            elif node.op == '&&':
                return 1.0 if self.is_truthy(left) and self.is_truthy(right) else 0.0
            elif node.op == '||':
                return 1.0 if self.is_truthy(left) or self.is_truthy(right) else 0.0
        elif isinstance(node, UnaryOp):
            operand = self.evaluate(node.operand)
            if node.op == '-':
                return -operand
            elif node.op == '!':
                return 0.0 if self.is_truthy(operand) else 1.0
        elif isinstance(node, CallExpr):
            if node.name == 'print':
                values = [str(self.evaluate(arg)) for arg in node.args]
                print(' '.join(values))
                return None
        
        return 0.0
    
    def is_truthy(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return len(value) > 0
        return bool(value)

# ============================================================================
# MAIN INTERPRETER
# ============================================================================

def run_code(code: str):
    """Run Lyra code"""
    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.interpret(ast)
    except Exception as e:
        print(f"Error: {e}")

def run_file(filename: str):
    """Run a .lyra file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        run_code(code)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")

def repl():
    """Interactive REPL"""
    print("╔═════════════════════════════════════╗")
    print("║   LYRA INTERPRETER v1.0             ║")
    print("║   Type 'exit' to quit               ║")
    print("╚═════════════════════════════════════╝")
    print()
    
    while True:
        try:
            code = input(">>> ")
            if code.lower() == 'exit':
                break
            if code.strip():
                run_code(code)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run file
        run_file(sys.argv[1])
    else:
        # Interactive mode
        repl()
