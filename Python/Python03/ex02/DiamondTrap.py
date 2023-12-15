from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """An awfull thing to create"""

    def __init__(self, first_name) -> None:
        """My monster initialisateur, it will be a Baratheon (MRO)"""
        super().__init__(first_name)

    def set_eyes(self, eyes_color):
        """My eyes setter"""
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        """My hairs setter"""
        self.hairs = hairs_color

    def get_eyes(self):
        """My eyes getter"""
        return self.eyes

    def get_hairs(self):
        """My hairs getter"""
        return self.hairs
