# Import math module for calculations
import math

def calculate_area(shape, *args):
    """
    A function to calculate the area of different shapes.

    Parameters:
    shape (str): A string representing the name of the shape for which to calculate the area.
    args: Any number of arguments that are required to calculate the area of the given shape.

    Returns:
    The area of the shape as a float.
    """

    # Define conditions for finding areas of different shapes
    if shape == 'triangle':
        base, height = args
        return 0.5 * base * height
    elif shape == 'rectangle':
        length, width = args
        return length * width
    elif shape == 'circle':
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == 'square':
        side = args[0]
        return side ** 2
    else:
        print(f"Error: Shape {shape} not supported")
        return None

# Examples for usage:
print(calculate_area('triangle', 13, 2))
print(calculate_area('rectangle', 18, 4))
print(calculate_area('circle', 8))
print(calculate_area('square', 7))
print(calculate_area('pentagon', 5))
