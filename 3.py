import math

class Circle:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def get_perimeter(self) -> float:
        return self.get_circumference()

    def get_circumference(self) -> float:
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    x = float(input("Enter x coordinate of the center: "))
    y = float(input("Enter y coordinate of the center: "))
    radius = float(input("Enter the radius of the circle: "))

    circle = Circle(x, y, radius)

    print(f"Area of the circle: {circle.get_area():.2f}")
    print(f"Circumference of the circle: {circle.get_circumference():.2f}")
