import cv2

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

# cv2.imshow('Cat', img)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

# Blur
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT) # (7, 7) is the kernel size
# cv2.imshow('Blur', blur)

# Edge Cascade
canny = cv2.Canny(blur, 125, 175) # 125 is the lower threshold, 175 is the upper threshold
# cv2.imshow('Canny Edges', canny)

# Dilating the image (thickening the edges)
dilated = cv2.dilate(canny, (3, 3), iterations=3)
# cv2.imshow('Dilated', dilated)

# Resize
resized = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)
# cv2.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
