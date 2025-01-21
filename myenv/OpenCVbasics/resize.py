import cv2
import numpy as np

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

resized = cv2.resize(img, (300, 300), interpolation= cv2.INTER_CUBIC) # width, height
# cv2.imshow('Resized', resized)

# Flipping the image
# 0: flipping vertically
# 1: flipping horizontally
# -1: flipping both vertically and horizontally
flip = cv2.flip(img, 0)
cv2.imshow('Flipped', flip)

# Cropping the image
cropped = img[50:200, 100:200] # height, width
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)

