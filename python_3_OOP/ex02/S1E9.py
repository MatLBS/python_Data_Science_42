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

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return self.family_name + " " + self.eyes + " " + self.hairs

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


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
