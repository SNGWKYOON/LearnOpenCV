import cv2
import numpy as np

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/pic.jpg')

cv2.imshow('image', img)

b,g,r = cv2.split(img)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

print(img.shape)
print(g.shape)

# Merge the color channels
merged = cv2.merge([b,g,r])
cv2.imshow('Merged', merged)

cv2.waitKey(0)

