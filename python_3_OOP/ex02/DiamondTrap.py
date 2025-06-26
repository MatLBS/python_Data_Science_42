from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Representing the King class
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a King with a first
        name and an alive status.
        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool): The alive status of the
            character, default is True.
        """
        super().__init__(first_name, is_alive)

    def set_hairs(self, value):
        """
        Set the hairs attribute to value.
        Args:
            value (str): The color of the hairs
        """
        self.hairs = value

    def set_eyes(self, value):
        """
        Set the eyes attribute to value.
        Args:
            value (str): The color of the eyes
        """
        self.eyes = value

    def get_hairs(self):
        """
        Return 
        """
        return self.hairs

    def get_eyes(self):
        return self.eyes


def main():
    try:
        print(King.__mro__)
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
