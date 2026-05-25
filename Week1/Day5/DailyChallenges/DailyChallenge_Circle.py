
import math


class Circle:
    """
    Represents a simple circle.

    A circle can be created using:
    - a radius
    - or a diameter with the class method.
    """

    def __init__(self, radius):
        """
        Initialize a circle with a radius.

        Args:
            radius (float): The radius of the circle.
        """

        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """
        Create a Circle instance using a diameter.

        Args:
            diameter (float): The diameter of the circle.

        Returns:
            Circle: A new Circle instance.
        """

        radius = diameter / 2

        return cls(radius)

    @property
    def diameter(self):
        """
        Return the diameter of the circle.

        Returns:
            float: The diameter of the circle.
        """

        return self.radius * 2

    @property
    def area(self):
        """
        Calculate the area of the circle.

        Formula:
            A = πr²

        Returns:
            float: The area of the circle.
        """

        return math.pi * (self.radius ** 2)

    def __str__(self):
        """
        Return a readable string representation
        of the circle.

        Returns:
            str: Description of the circle.
        """

        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter:.2f}, "
            f"area={self.area:.2f})"
        )

    def __repr__(self):
        """
        Return the official string representation
        of the circle.

        Returns:
            str: Circle representation.
        """

        return f"Circle({self.radius})"

    def __add__(self, other):
        """
        Add two circles together.

        The new circle has a radius equal to
        the sum of both radii.

        Args:
            other (Circle): Another circle.

        Returns:
            Circle: A new circle.
        """

        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        """
        Compare two circles using the '>' operator.

        Args:
            other (Circle): Another circle.

        Returns:
            bool: True if this circle is larger.
        """

        return self.radius > other.radius

    def __eq__(self, other):
        """
        Compare two circles using the '==' operator.

        Args:
            other (Circle): Another circle.

        Returns:
            bool: True if both circles have
            the same radius.
        """

        return self.radius == other.radius

    def __lt__(self, other):
        """
        Compare two circles using the '<' operator.

        Args:
            other (Circle): Another circle.

        Returns:
            bool: True if this circle is smaller.
        """

        return self.radius < other.radius

c1 = Circle(5)

c2 = Circle.from_diameter(10)

print(c1)
print(c2)