from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for character.
        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool): The alive status of the
            character, default is True.
        """
        assert isinstance(first_name, str), "First Name must be a string"
        assert isinstance(is_alive, bool), "Is_alive must be a boolean"
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the health state of the character.
        """
        pass


class Stark(Character):
    """
    This class inherits from Character and represents
    a Stark character in the game.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Stark character with a first name and an alive status.
        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool): The alive status of the
            character, default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Marks the Stark character as dead by setting is_alive to False.
        """
        self.is_alive = False


def main():
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        # hodor = Character("hodor")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
