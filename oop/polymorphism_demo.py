import math

class Shape:
    """
    Base class for geometric shapes.
    It defines an area() method that must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises an error to ensure subclasses implement their own version.
        """
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """
    A derived class for a rectangle, inheriting from Shape.
    It calculates the area based on its length and width.
    """
    def __init__(self, length, width):
        """Initializes the Rectangle with a length and width."""
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the Shape.area() method to calculate the rectangle's area.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A derived class for a circle, inheriting from Shape.
    It calculates the area based on its radius.
    """
    def __init__(self, radius):
        """Initializes the Circle with a radius."""
        self.radius = radius

    def area(self):
        """
        Overrides the Shape.area() method to calculate the circle's area.
        """
        return math.pi * self.radius ** 2

def main():
    """
    Demonstrates polymorphism by creating and using different shape objects
    in a uniform way.
    """
    # A list containing different shape objects.
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # The loop calls the area() method on each object,
    # and Python's polymorphism ensures the correct method for each shape is used.
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()