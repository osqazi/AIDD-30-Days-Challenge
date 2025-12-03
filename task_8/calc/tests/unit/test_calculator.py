import pytest
from src.calculator import Calculator
from src.errors import InvalidExpressionError, DivisionByZeroError, UnsupportedOperatorError, MismatchedParenthesesError

@pytest.fixture
def calculator():
    return Calculator()

def test_evaluate_basic_addition(calculator):
    assert calculator.evaluate_expression("5 + 3") == 8

def test_evaluate_basic_subtraction(calculator):
    assert calculator.evaluate_expression("10 - 4") == 6

def test_evaluate_basic_multiplication(calculator):
    assert calculator.evaluate_expression("6 * 7") == 42

def test_evaluate_basic_division(calculator):
    assert calculator.evaluate_expression("8 / 2") == 4

def test_evaluate_order_of_operations(calculator):
    assert calculator.evaluate_expression("1 + 2 * 3") == 7

def test_evaluate_with_parentheses(calculator):
    assert calculator.evaluate_expression("(1 + 2) * 3") == 9

def test_evaluate_complex_expression(calculator):
    assert calculator.evaluate_expression("10 - (2 + 1) * 3 / 3") == 7

def test_evaluate_floating_point_numbers(calculator):
    assert calculator.evaluate_expression("1.5 + 2.5") == 4.0
    assert calculator.evaluate_expression("10 / 4") == 2.5

def test_evaluate_negative_numbers(calculator):
    assert calculator.evaluate_expression("-5 + 3") == -2
    assert calculator.evaluate_expression("5 + -3") == 2
    assert calculator.evaluate_expression("-5 * -3") == 15

def test_evaluate_expression_with_spaces(calculator):
    assert calculator.evaluate_expression("  1 +   2*3  ") == 7

# Test for InvalidExpressionError
def test_empty_expression(calculator):
    with pytest.raises(InvalidExpressionError, match="Expression cannot be empty or non-string."):
        calculator.evaluate_expression("")

def test_non_string_expression(calculator):
    with pytest.raises(InvalidExpressionError, match="Expression cannot be empty or non-string."):
        calculator.evaluate_expression(123)

def test_expression_only_spaces(calculator):
    with pytest.raises(InvalidExpressionError, match="Expression cannot be empty or non-string."):
        calculator.evaluate_expression("   ")

# Test for MismatchedParenthesesError (will be more specific once parsing is implemented)
def test_mismatched_parentheses_open(calculator):
    with pytest.raises(MismatchedParenthesesError):
        calculator.evaluate_expression("((1 + 2)")

def test_mismatched_parentheses_close(calculator):
    with pytest.raises(MismatchedParenthesesError):
        calculator.evaluate_expression("(1 + 2))")

# Test for UnsupportedOperatorError
def test_unsupported_character_in_expression(calculator):
    with pytest.raises(InvalidExpressionError, match="Unexpected character: '%'"):
        calculator.evaluate_expression("1 % 2")

# Test for DivisionByZeroError
def test_division_by_zero(calculator):
    with pytest.raises(DivisionByZeroError):
        calculator.evaluate_expression("10 / 0")

def test_division_by_zero_complex(calculator):
    with pytest.raises(DivisionByZeroError):
        calculator.evaluate_expression("5 + (10 / (5 - 5))")
