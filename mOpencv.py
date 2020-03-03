# coding=utf-8
import cv2

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


def findface(faceimg):
    frame = faceimg
    classifier = cv2.CascadeClassifier("testdata/haarcascade_frontalface_alt.xml")
    minSize = (10, 10)
    faceRects = classifier.detectMultiScale(frame, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
    return faceRects

img = imread('testdata/face.jpg')
imwrite('testdata/w.jpg', img)
w, h = getsize(img)
print(w, h)
print(img2gray(img).shape)

# imshow("w",img)
# cv2.waitKey()