from PIL import Image
import numpy as np

im = Image.open("landscape.jpg")
print(im.size, im.width, im.height)
print(im.format, im.info)
print(im.mode)
print(im.getpixel([0,1]))

imArray = np.array(im)
print(imArray.shape)
print(imArray)