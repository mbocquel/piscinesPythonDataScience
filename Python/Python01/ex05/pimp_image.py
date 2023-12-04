import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received and show it.
    """
    newArray = 255 - array
    print(newArray)
    fig, ax = plt.subplots()
    ax.imshow(newArray)
    plt.title("ft_invert")
    plt.show()
    return (newArray)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Only keep the red part of the image and show it.
    """
    newArray = array.copy()
    newArray[:, :, (1, 2)] = 0
    print(newArray)
    fig, ax = plt.subplots()
    ax.imshow(newArray)
    plt.title("ft_red")
    plt.show()
    return (newArray)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Only keep the green part of the image and show it.
    """
    newArray = array.copy()
    newArray[:, :, (0, 2)] = 0
    print(newArray)
    fig, ax = plt.subplots()
    ax.imshow(newArray)
    plt.title("ft_green")
    plt.show()
    return (newArray)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Only keep the blue part of the image and show it.
    """
    newArray = array.copy()
    newArray[:, :, (0, 1)] = 0
    print(newArray)
    fig, ax = plt.subplots()
    ax.imshow(newArray)
    plt.title("ft_blue")
    plt.show()
    return (newArray)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Remove the color and keep only greyscale of image and show it.
    """
    img = Image.fromarray(array).convert("L")
    newArray = np.array(img)
    print(newArray)
    fig, ax = plt.subplots()
    ax.imshow(newArray, cmap="grey")
    plt.title("ft_grey")
    plt.show()
    return (newArray)
