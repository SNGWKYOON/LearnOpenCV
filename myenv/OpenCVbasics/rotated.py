import cv2
import numpy as np

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

# Rotation of the image
def rotate(img, angle, rotPoint=None): # rotPoint is the point where the image will rotate around
    (height, width) = img.shape[:2] # height, width of the image is the first two elements of the shape
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 is the scale
    dimension = (width, height)
    return cv2.warpAffine(img, rotMat, dimension)

rotated = rotate(img, -45) # rotate 45 degrees clockwise
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)

