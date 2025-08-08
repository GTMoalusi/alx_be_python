import math

class Shape:
    
    def area(self):
        
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    
    def __init__(self, length, width):
        """Initializes the Rectangle with a length and width."""
        self.length = length
        self.width = width

    def area(self):
        
        return self.length * self.width

class Circle(Shape):
   
    def __init__(self, radius):
        """Initializes the Circle with a radius."""
        self.radius = radius

    def area(self):
       
        return math.pi * self.radius * self.radius

def main():
   
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

