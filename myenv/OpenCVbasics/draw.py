import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # 500x500 black image with 3 channels
# cv.imshow('Blank', blank)
# paint the image a certain color
# blank[200:300, 300:400] = 0, 255, 0 # BGR
# cv.imshow('Green', blank)

# Draw a rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1]//3, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED) 
# cv.imshow('Rectangle', blank)

# Draw a circle
# cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)

# Draw a line
# cv.line(blank, (20, 20), (blank.shape[1]//3, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hello', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0) # 0 means infinite time