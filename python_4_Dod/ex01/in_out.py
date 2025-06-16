def square(x: int | float) -> int | float:
    """
    Function that returns the square of a number.
    Args:
        x (int | float): The number to be squared.
    Returns:
        int | float: The square of the input number.
    """
    assert isinstance(x, (int, float)), "The value must be integer or float"
    assert x != 0, "You can not divide by 0"
    return x**2


def pow(x: int | float) -> int | float:
    """
    Function that returns the power of a number raised to itself.
    Args:
        x (int | float): The number to be raised to the power of itself.
    Returns:
        int | float: The result of raising the input
        number to the power of itself.
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Create a counter function that performs calculations and
    updates its input value.
    Args:
        x (int | float): The initial value to be processed.
        function: A function that takes a single argument and returns a value.
    Returns:
        object: A callable function that, when invoked,
        applies the given function
        to the current value of x and updates x with the result.
    """
    def inner() -> float:
        """
        Inner function that applies the provided function
        to the current value of x
        and updates x with the result.
        Returns:
            float: The result of applying the function to x.
        """
        nonlocal x
        result = function(x)
        x = result
        return result

    return inner


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
