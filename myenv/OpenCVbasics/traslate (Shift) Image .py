import cv2
import numpy as np

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

# Translation (shifting the image)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # x is the number of pixels to shift right, y is the number of pixels to shift down
    dimension = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimension)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, -100) # shift left 100 pixels, shift up 100 pixels
cv2.imshow('Translated', translated)

cv2.waitKey(0)

