import cv2
import PIL.Image as Image
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
import time
import csv


class CreateImage():
    def generateBlackAndWhiteStripImage(self, imgSize, divs):
        img = np.zeros([imgSize, imgSize], dtype=int)
        return img

    def generateBlackAndWhiteCircularImage(self, imgSize, dia, divs):
        img = np.zeros([imgSize, imgSize], dtype=int)
        return img

if __name__ == "__main__":

    obj = CreateImage()
    img = obj.generateBlackAndWhiteStripImage(320, 1)
    plt.imshow(img, cmap='gray')
    plt.show()

