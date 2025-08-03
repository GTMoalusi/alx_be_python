"""
robust_division_calculator.py
A module containing a function for safe division with error handling.
"""

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the string arguments to floats.
        num = float(numerator)
        den = float(denominator)

        # Handle the ZeroDivisionError within a nested try-except block.
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handle cases where the input strings are not valid numbers.
        return "Error: Please enter numeric values only."

