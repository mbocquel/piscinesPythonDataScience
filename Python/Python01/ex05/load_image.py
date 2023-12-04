from PIL import Image
from PIL import UnidentifiedImageError
import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image file and print it's shape
    """
    try:
        im = Image.open(path, "r")
        imArray = np.array(im)
        print("The Shape of image is :", imArray.shape)
        fig, ax = plt.subplots()
        ax.imshow(imArray)
        plt.title("Original")
        plt.show()
        return (imArray)
    except FileNotFoundError:
        print("Error: File Not Found")
    except UnidentifiedImageError:
        print("Error: the image cannot be opened and identified.")
