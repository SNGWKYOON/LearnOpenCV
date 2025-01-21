import cv2

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

# Simple Thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
threshold, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY) # pixel value > 120 -> 255, else 0
cv2.imshow('Simple Thresholded', thresh)

# Inverse Thresholding
threshold, thresh_inv = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV) # pixel value > 120 -> 0, else 255
cv2.imshow('Inverse Thresholded', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

cv2.waitKey(0)

