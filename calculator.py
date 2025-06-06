"""Simple command-line calculator."""

import sys


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b.

    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <operator> <num2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        operator = sys.argv[2]
        b = float(sys.argv[3])
    except ValueError:
        print("Error: numeric arguments required")
        sys.exit(1)

    try:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == 'x' or operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        else:
            print(f"Unknown operator: {operator}")
            sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()

