import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up a fresh SimpleCalculator instance for each test method."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(7, -2), 9)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-2, 8), -16)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(3.0, 2.5), 7.5)

    def test_division(self):
        """Test the divide method with normal and zero-division cases."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(12.0, 4.0), 3.0)

        # Test the edge case of division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == "__main__":
    unittest.main()
