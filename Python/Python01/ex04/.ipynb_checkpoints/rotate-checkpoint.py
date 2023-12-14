from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def transpose2DMatrix(matrix: np.ndarray) -> np.ndarray:
    """
    Function that transpose a 2D matrix
    """
    if (matrix.ndim != 2):
        return (matrix)
    li = len(matrix)
    cl = len(matrix[0])
    return np.array([[matrix[i][j] for i in range(li)] for j in range(cl)])


def main():
    """
    Program which load the image "animal.jpeg", cut a square part from it
    and transpose it, display it, print the new shape and the data of
    the image after the transpose.
    """
    try:
        path = "animal.jpeg"
        animalArray = ft_load(path)
        assert isinstance(animalArray, np.ndarray)
        animalInGrey = Image.open(path).convert("L")
        animalInGreyArray = np.array(animalInGrey)
        slicedAnimalInGreyArray = animalInGreyArray[100:500, 450:850]
        print("The shape of image is:", slicedAnimalInGreyArray.shape)
        print(slicedAnimalInGreyArray)
        transposedArray = transpose2DMatrix(slicedAnimalInGreyArray)
        print("New shape after Transpose:", transposedArray.shape)
        print(transposedArray)
        fig, ax = plt.subplots()
        ax.imshow(transposedArray, cmap='gray')
        plt.show()

    except AssertionError:
        print("AssertionError: error with the file")


if __name__ == "__main__":
    main()
