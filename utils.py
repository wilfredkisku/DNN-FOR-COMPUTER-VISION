import cv2
import PIL.Image as Image
import matplotlib.pyplot as plt

import math
import cmath
import time
import csv


class CreateImage():


    def generateBlackAndWhileSquareImage(imgSize, divs):

        img = np.zeros([imgSize, imgSize], dtype=int)
        

