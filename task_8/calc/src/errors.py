class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class InvalidExpressionError(CalculatorError):
    """Raised when an expression has an invalid format or contains invalid tokens."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when a division by zero operation is attempted."""
    pass

class UnsupportedOperatorError(CalculatorError):
    """Raised when an unsupported operator is encountered."""
    pass

class MismatchedParenthesesError(CalculatorError):
    """Raised when parentheses in an expression are mismatched."""
    pass
