# coding=utf-8
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def imread(imgfile):
    img=cv2.imread(imgfile)
    return img

def imshow(wname,img):
    cv2.imshow(wname, img)
    cv2.waitKey(1)

img=imread('testdata/face.jpg')
imshow("w",img)
cv2.waitKey()