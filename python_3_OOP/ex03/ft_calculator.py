class calculator:
    """
    A calculator class for performing arithmetic operations between
    a list and a object.

    Attributes:
        list (list): The list on which operations will be performed.

    Methods:
        __init__(self, list): Init the calculator with the provided list.

        __add__(self, object): + a object value to each element of the vec.

        __mul__(self, object): * each element of the list by a object value.

        __sub__(self, object): - a object value from each element of the list

        __truediv__(self, object): / each element of the list by a object val
    """

    def __init__(self, lst):
        """
        Initializes the calculator with the provided list.

        Args:
            lst (list): The list on which operations will be performed.
        """
        self.lst = lst

    def __add__(self, object) -> None:
        """
        Returns:
            The resulting list after addition.
        """
        self.lst = [x + object for x in self.lst]
        print(self.lst)
        return [x for x in self.lst]

    def __mul__(self, object) -> None:
        """
        Returns:
            The resulting list after multiplication.
        """
        self.lst = [x * object for x in self.lst]
        print(self.lst)
        return [x for x in self.lst]

    def __sub__(self, object) -> None:
        """
        Returns:
            The resulting list after subtraction.
        """
        self.lst = [x - object for x in self.lst]
        print(self.lst)
        return [x for x in self.lst]

    def __truediv__(self, object) -> None:
        """
        Returns:
            The resulting list after division.

        Raises:
            ZeroDivisionError: If the object value is 0.
        """
        assert object != 0, "You cannot do a division by 0."
        self.lst = [x / object for x in self.lst]
        print(self.lst)
        return [x for x in self.lst]


def main():
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
