from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def printInfoImgGrey(imArray: np.ndarray):
    """
    Small function that print the interesting data of my 2D Array
    """
    print("New shape after slicing: ", imArray.shape)
    ArrayX = np.array([[x] for x in imArray[0]])
    ArrayY = np.array([[y] for y in imArray[1]])
    ArrayPrintable = np.array([ArrayX, ArrayY])
    print(ArrayPrintable)


def main():
    """
    Program that open a photo, print some information, create a new image in
    grey scale, print some information and zoom on it.
    """
    try:
        path = "animal.jpeg"
        animalArray = ft_load(path)
        assert isinstance(animalArray, np.ndarray)
        print(animalArray)
        animalInGrey = Image.open(path).convert("L")
        animalInGreyArray = np.array(animalInGrey)
        slicedAnimalInGreyArray = animalInGreyArray[100:500, 450:850]
        printInfoImgGrey(slicedAnimalInGreyArray)
        fig, ax = plt.subplots()
        ax.imshow(slicedAnimalInGreyArray, cmap='gray')
        plt.show()

    except AssertionError:
        print("AssertionError: error with the file")


if __name__ == "__main__":
    main()
