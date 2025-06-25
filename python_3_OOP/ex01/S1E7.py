from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon character with a first
        name and an alive status.
        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool): The alive status of the
            character, default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Marks the Baratheon character as dead by setting is_alive to False.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Lannister character with a
        first name and an alive status.
        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): The alive status of the
            character, default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Marks the Lannister character as dead by setting is_alive to False.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Class method to create a Lannister character.
        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): The alive status of the
            character, default is True.
        Returns:
            Lannister: An instance of the Lannister class.
        """
        return cls(first_name, is_alive)


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
