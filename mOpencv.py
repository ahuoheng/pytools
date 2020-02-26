# coding=utf-8
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def imread(imgfile):
    img = cv2.imread(imgfile)
    return img


def imshow(wname, img):
    cv2.imshow(wname, img)
    cv2.waitKey(1)


def imwrite(fname, img):
    cv2.imwrite(fname, img)

def getsize(img):
    size = img.shape
    height = size[0]
    width = size[1]
    return width, height

def img2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img = imread('testdata/face.jpg')
imwrite('testdata/w.jpg', img)
w, h = getsize(img)
print(w, h)
print(img2gray(img).shape)

# imshow("w",img)
# cv2.waitKey()