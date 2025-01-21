import cv2

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

# Averaging
average = cv2.blur(img, (7,7))
cv2.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv2.medianBlur(img, 9)
cv2.imshow('Median Blur', median)

# Bilateral Blur - Highly effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow('Bilateral Blur', bilateral)

cv2.waitKey(0)

