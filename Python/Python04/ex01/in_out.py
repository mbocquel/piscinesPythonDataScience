def square(x: int | float) -> int | float:
    """return the square of a number"""
    return (x**2)


def pow(x: int | float) -> int | float:
    """Return a number power itself"""
    return x**x


def outer(x: int | float, function) -> object:
    """Return an object that when called returns
    the result of the arguments calculation """
    count = 0

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    count = x
    return inner
