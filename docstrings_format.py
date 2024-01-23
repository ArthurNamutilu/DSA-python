# Module Docstring:
"""This is a module-level docstring.

This module does XYZ.
"""
def function_in_module():
    """This function does ABC."""
    pass

Function Docstring:
def add_numbers(a, b):
    """Add two numbers and return the result.

    Args:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

Class Docstring:
class MyClass:
    """This is a docstring for the MyClass.

    Attributes:
    - attribute1 (int): Description of attribute1.
    - attribute2 (str): Description of attribute2.
    """

    def __init__(self, attribute1, attribute2):
        """Constructor for MyClass.

        Args:
        - attribute1 (int): Initial value for attribute1.
        - attribute2 (str): Initial value for attribute2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def some_method(self):
        """This method does something."""
        pass


# Function with Examples:

def divide(a, b):
    """Divide two numbers and return the result.

    Args:
    - a (float): The numerator.
    - b (float): The denominator.

    Returns:
    float: The result of the division.

    Raises:
    ValueError: If the denominator is 0.
    """

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b

# Examples:
result = divide(10, 2)
print(result)  # Output: 5.0

try:
    result = divide(5, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero.


# Multi-Line Docstring:
 
def complex_function(param1, param2):
    """
    This is a multi-line docstring.

    It can provide a more detailed description of the function,
    its purpose, and usage.

    Args:
    - param1 (str): Description of param1.
    - param2 (int): Description of param2.

    Returns:
    float: The result of the computation.
    """
    pass

