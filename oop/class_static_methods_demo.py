class Calculator:
    """
    A simple calculator class that includes a static method and a class method
    to demonstrate their usage and differences.
    """
    # A class attribute that can be accessed by class methods.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers.
        It doesn't require access to class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers.
        It has access to class attributes via the `cls` parameter.
        """
        # The `cls` parameter is used here to access the class attribute.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# The following code block is provided for testing and demonstration,
# as per the `main.py` example in the task description.
def main():
    """
    Tests the static and class methods of the Calculator class.
    """
    # Using the static method directly from the class.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method, also directly from the class.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
