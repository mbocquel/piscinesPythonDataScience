import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Function that return a list of Body Mass Index from a list of height
    and a list of weight. BMI = weight / (height x height).
    """
    try:
        assert len(height) == len(weight), "height and list of different size"
        assert all(map(lambda i: isinstance(i, (int, float)),
                       height)), ("some height are not int or float")
        assert all(map(lambda i: isinstance(i, (int, float)),
                       weight)), ("some height are not int or float")
        heightArray = np.array(height)
        weightArray = np.array(weight)
        assert heightArray.min() > 0, "some height are not > 0"
        assert weightArray.min() > 0, "some weight are not >= 0"
        bmi = (weightArray / (heightArray * heightArray))
        return (bmi.tolist())
    except AssertionError as msg:
        print("AssertionError give_bmi:", msg)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Function that takes a list of int and float and check
    if the values are higher than the limit.
    """
    try:
        assert all(map(lambda i: isinstance(i, (int, float)),
                       bmi)), ("some bmi are not int or float")
        assert type(limit) is int, "Limit is not int"
        bmiArray = np.array(bmi)
        limit = bmiArray > limit
        return (limit.tolist())
    except AssertionError as msg:
        print("AssertionError apply_limit:", msg)
