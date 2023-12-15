class calculator:
    """My amazing calculator"""
    def __init__(self, my_vector) -> None:
        self.my_vector = my_vector
    
    def __add__(self, object):
        """Adding is not that hard..."""
        self.my_vector = [elem + object for elem in self.my_vector]
        print(self.my_vector)

    def __mul__(self, object):
        """Multiply"""
        self.my_vector = [elem * object for elem in self.my_vector]
        print(self.my_vector)

    def __sub__(self, object):
        """Substraction"""
        self.my_vector = [elem - object for elem in self.my_vector]
        print(self.my_vector)

    def __truediv__(self, object):
        """Div"""
        if object == 0:
            print("Error: Div by zero")
        else:
            self.my_vector = [elem / object for elem in self.my_vector]
            print(self.my_vector)
