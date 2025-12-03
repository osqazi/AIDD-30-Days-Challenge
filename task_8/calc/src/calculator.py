import re
from .errors import InvalidExpressionError, MismatchedParenthesesError, UnsupportedOperatorError, DivisionByZeroError

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Calculator:
    _operator_precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        'u-': 3 # Unary minus has higher precedence
    }

    def _tokenize(self, expression: str):
        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('BIN_OPERATOR', r'[+\-*/]'),  # Binary arithmetic operators
            ('LPAREN',   r'\('),           # Left parenthesis
            ('RPAREN',   r'\)'),           # Right parenthesis
            ('SKIP',     r'\s+'),          # Whitespace
            ('MISMATCH', r'.'),            # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        
        tokens = []
        last_token_type = None

        for mo in re.finditer(tok_regex, expression):
            kind = mo.lastgroup
            value = mo.group(kind)
            
            if kind == 'NUMBER':
                tokens.append(Token(kind, float(value)))
                last_token_type = kind
            elif kind == 'BIN_OPERATOR':
                # Distinguish between binary '-' and unary '-'
                if value == '-' and (last_token_type is None or 
                                     last_token_type == 'OPERATOR' or # Check for previous binary operator
                                     last_token_type == 'UNARY_MINUS' or # Check for previous unary minus
                                     last_token_type == 'LPAREN'):
                    tokens.append(Token('UNARY_MINUS', 'u-')) # Use 'u-' as value for unary minus
                elif value in self._operator_precedence: # Ensure it's a known binary operator
                    tokens.append(Token('OPERATOR', value)) # Store as OPERATOR with its value
                else:
                    raise UnsupportedOperatorError(f"Unsupported operator: '{value}'")
                last_token_type = tokens[-1].type
            elif kind == 'LPAREN':
                tokens.append(Token(kind, value))
                last_token_type = kind
            elif kind == 'RPAREN':
                tokens.append(Token(kind, value))
                last_token_type = kind
            elif kind == 'SKIP':
                pass
            elif kind == 'MISMATCH':
                raise InvalidExpressionError(f"Unexpected character: '{value}'")
        
        if not tokens:
            raise InvalidExpressionError("Expression contains no valid tokens.")
        
        return tokens

    def _shunting_yard(self, tokens: list[Token]) -> list[Token]:
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.type == 'NUMBER':
                output_queue.append(token)
            elif token.type == 'OPERATOR' or token.type == 'UNARY_MINUS':
                # For precedence, look up using token.value for operators, or token.type for UNARY_MINUS
                current_op_prec = self._operator_precedence.get(token.value if token.type == 'OPERATOR' else token.type)

                while (operator_stack and 
                       (operator_stack[-1].type == 'OPERATOR' or operator_stack[-1].type == 'UNARY_MINUS')):
                    stack_op_prec = self._operator_precedence.get(operator_stack[-1].value if operator_stack[-1].type == 'OPERATOR' else operator_stack[-1].type, 0)
                    if stack_op_prec >= current_op_prec:
                        output_queue.append(operator_stack.pop())
                    else:
                        break # Stack operator has lower precedence
                operator_stack.append(token)
            elif token.type == 'LPAREN':
                operator_stack.append(token)
            elif token.type == 'RPAREN':
                while operator_stack and operator_stack[-1].type != 'LPAREN':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise MismatchedParenthesesError("Mismatched parentheses: No matching left parenthesis.")
                operator_stack.pop() # Discard the left parenthesis
        
        while operator_stack:
            if operator_stack[-1].type == 'LPAREN' or operator_stack[-1].type == 'RPAREN':
                raise MismatchedParenthesesError("Mismatched parentheses: Unclosed left parenthesis.")
            output_queue.append(operator_stack.pop())
        
        return output_queue

    def _evaluate_rpn(self, rpn_tokens: list[Token]) -> float:
        operand_stack = []

        for token in rpn_tokens:
            if token.type == 'NUMBER':
                operand_stack.append(token.value)
            elif token.type == 'OPERATOR': # Binary operator
                if token.value not in self._operator_precedence: # Check for unsupported operator here
                    raise UnsupportedOperatorError(f"Unsupported operator: {token.value}")

                if len(operand_stack) < 2:
                    raise InvalidExpressionError("Invalid expression format: Not enough operands for binary operator.")
                
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()

                if token.value == '+':
                    operand_stack.append(operand1 + operand2)
                elif token.value == '-':
                    operand_stack.append(operand1 - operand2)
                elif token.value == '*':
                    operand_stack.append(operand1 * operand2)
                elif token.value == '/':
                    if operand2 == 0:
                        raise DivisionByZeroError("Division by zero.")
                    operand_stack.append(operand1 / operand2)
            elif token.type == 'UNARY_MINUS': # Unary operator
                if len(operand_stack) < 1:
                    raise InvalidExpressionError("Invalid expression format: Not enough operands for unary operator.")
                
                operand = operand_stack.pop()
                operand_stack.append(-operand) # Apply negation
        
        if len(operand_stack) != 1:
            raise InvalidExpressionError("Invalid expression format: Too many operands or operators.")
        
        return operand_stack[0]

    def evaluate_expression(self, expression: str) -> float:
        """
        Evaluates a mathematical expression string.
        """
        if not isinstance(expression, str) or not expression.strip():
            raise InvalidExpressionError("Expression cannot be empty or non-string.")
        
        tokens = self._tokenize(expression)
        rpn_tokens = self._shunting_yard(tokens)
        result = self._evaluate_rpn(rpn_tokens)
        
        return result