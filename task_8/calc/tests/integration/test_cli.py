import pytest
from unittest.mock import patch
from io import StringIO
import sys
from src.main import main

@pytest.fixture
def run_cli_with_input():
    def _run(input_str):
        with patch('sys.stdin', StringIO(input_str + '\nexit\n')), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
             patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            main()
            return mock_stdout.getvalue(), mock_stderr.getvalue()
    return _run

def test_cli_basic_addition(run_cli_with_input):
    stdout, stderr = run_cli_with_input("5 + 3")
    assert "Result: 8.0" in stdout
    assert not stderr

def test_cli_basic_subtraction(run_cli_with_input):
    stdout, stderr = run_cli_with_input("10 - 4")
    assert "Result: 6.0" in stdout
    assert not stderr

def test_cli_basic_multiplication(run_cli_with_input):
    stdout, stderr = run_cli_with_input("6 * 7")
    assert "Result: 42.0" in stdout
    assert not stderr

def test_cli_basic_division(run_cli_with_input):
    stdout, stderr = run_cli_with_input("8 / 2")
    assert "Result: 4.0" in stdout
    assert not stderr

def test_cli_order_of_operations(run_cli_with_input):
    stdout, stderr = run_cli_with_input("1 + 2 * 3")
    assert "Result: 7.0" in stdout
    assert not stderr

def test_cli_with_parentheses(run_cli_with_input):
    stdout, stderr = run_cli_with_input("(1 + 2) * 3")
    assert "Result: 9.0" in stdout
    assert not stderr

def test_cli_floating_point_numbers(run_cli_with_input):
    stdout, stderr = run_cli_with_input("1.5 + 2.5")
    assert "Result: 4.0" in stdout
    assert not stderr

def test_cli_multiple_expressions(run_cli_with_input):
    stdout, stderr = run_cli_with_input("1+1\n2*2")
    assert "Result: 2.0" in stdout
    assert "Result: 4.0" in stdout
    assert not stderr

def test_cli_empty_input_ignored(run_cli_with_input):
    stdout, stderr = run_cli_with_input("\n   \n5+5")
    assert "Result: 10.0" in stdout
    assert not stderr
