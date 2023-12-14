from abc import ABC, abstractclassmethod


class Character(ABC):
    """My abstract class docstring"""
    def __init__(self, first_name, is_alive=True) -> None:
        """My abstract class constructor docstring"""
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractclassmethod
    def die(self):
        """My abstract class die method docstring"""
        pass


class Stark(Character):
    """My class docstring"""
    def __init__(self, first_name, is_alive=True) -> None:
        """My class constructor docstring"""
        super().__init__(first_name, is_alive)

    def die(self):
        """My class die method docstring"""
        self.is_alive = False
