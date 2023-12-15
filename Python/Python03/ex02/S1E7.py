from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, family_name='Baratheon',
                 eyes='brown', hairs='dark') -> None:
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Killing a Bratheon"""
        self.is_alive = False

    @property
    def __str__(self):
        """__str__ property method of Bratheon"""
        return str(f'<bound method Baratheon.__str__ of Vector: (\'\
                   {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')>')

    @property
    def __repr__(self):
        """__repr__ property method of Bratheon"""
        return str(f'<bound method Baratheon.__repr__ of Vector: (\'\
                   {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')>')


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, family_name='Lannister',
                 eyes='blue', hairs='light') -> None:
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Killing a Lannister"""
        self.is_alive = False

    @property
    def __str__(self):
        """__str__ property method of Lannister"""
        return str(f'<bound method Lannister.__str__ of Vector: (\'\
                   {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')>')

    @property
    def __repr__(self):
        """__repr__ property method of Lannister"""
        return str(f'<bound method Lannister.__repr__ of Vector: (\'\
                   {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')>')

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Lanister class Method to create other lanister"""
        return cls(first_name, is_alive)
