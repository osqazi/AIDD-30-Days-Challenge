from src.calculator import Calculator
from src.errors import CalculatorError

def main():
    calculator = Calculator()
    print("Simple Expression Calculator")
    print("Enter an expression (e.g., '1 + 2 * 3') or 'exit' to quit.")

    while True:
        try:
            expression = input("> ")
            if expression.lower() == 'exit':
                break
            
            if not expression.strip():
                continue

            result = calculator.evaluate_expression(expression)
            print(f"Result: {result}")
        except CalculatorError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
