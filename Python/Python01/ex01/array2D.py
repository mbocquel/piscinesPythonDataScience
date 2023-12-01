import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided
    start and end arguments
    """
    try:
        assert type(family) is list, "Gime me a list please"
        my2DArray = np.array(family)
        print("My shape is :", np.shape(my2DArray))
        newArray = my2DArray[start:end]
        print("My new shape is :", np.shape(newArray))
        return (newArray.tolist())
    except AssertionError as msg:
        print("AssertionError slice_me:", msg)
    except ValueError:
        print("ValueError slice_me: the list are not the same size")
