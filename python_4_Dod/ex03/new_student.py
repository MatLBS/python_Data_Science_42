import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character string for student ID.
    Returns:
        str: A random string of lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Class representing a student.
    Attributes:
        name (str): The first name of the student.
        surname (str): The surname of the student.
        active (bool): Indicates if the student is active. Defaults to True.
        login (str): The login name of the student. Defaults to "Eagle".
        id (str): A unique identifier for the student, generated automatically.
    """
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default="Eagle")
    id: int = field(init=False, default_factory=generate_id)


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except (TypeError, AssertionError) as error:
        print("TypeError:", error)


if __name__ == "__main__":
    main()
