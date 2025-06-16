class calculator:
    """
    A calculator class for performing arithmetic operations between
    two lists.

    You can call the class without creating
    an instance thanks to the static methods.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.
        """
        dot_product = 0
        for i in range(len(V1)):
            dot_product += (V1[i] * V2[i])
        print(dot_product)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise and print the result vector.
        """
        new_lst = []
        for i in range(len(V1)):
            new_lst.append(float(V1[i] + V2[i]))
        print(new_lst)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors element-wise and print the result vector.
        """
        new_lst = []
        for i in range(len(V1)):
            new_lst.append(float(V1[i] - V2[i]))
        print(new_lst)


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
