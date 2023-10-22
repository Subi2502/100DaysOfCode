#Create a class hierarchy for different shapes (circle, rectangle, triangle) and calculate their areas.
# print ("\nSubi - Day 33 of #100DaysOfCode\n") 
# print("\nCreate a class hierarchy for different shapes and calculate their areas\n")

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     def calculate_area(self) -> float:
#         pass

# class Circle(Shape):
#     def __init__(self, radius: float) -> None:
#         self.radius = radius

#     def calculate_area(self) -> float:
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, length: float, width: float) -> None:
#         self.length = length
#         self.width = width

#     def calculate_area(self) -> float:
#         return self.length * self.width

# class Triangle(Shape):
#     def __init__(self, base: float, height: float) -> None:
#         self.base = base
#         self.height = height

#     def calculate_area(self) -> float:
#         return 0.5 * self.base * self.height

# def main():
#     circle = Circle(5)
#     print(f"The area of the circle is {circle.calculate_area()}")

#     rectangle = Rectangle(10, 20)
#     print(f"The area of the rectangle is {rectangle.calculate_area()}")

#     triangle = Triangle(15, 20)
#     print(f"The area of the triangle is {triangle.calculate_area()}")

# if __name__ == "__main__":
#     main()


#Implement inheritance in a class hierarchy (e.g., create a subclass of a shape).
print("\nImplement inheritance in a class hierarchy\n")

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print("Drawing a circle with center at (%s, %s) and radius %s" % (self.x, self.y, self.radius))

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing a rectangle with top-left corner at (%s, %s) and width %s and height %s" % (self.x, self.y, self.width, self.height))

if __name__ == "__main__":
    circle = Circle(2, 4, 6)
    circle.draw()

    rectangle = Rectangle(8, 10, 12, 14)
    rectangle.draw()