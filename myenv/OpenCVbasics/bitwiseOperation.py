#Bitwise_and : 0 if both are 0, 1 if either is 1
#Bitwise_or : 0 if both are 0, 1 if either is 1 (Applies a logical OR operation)
#Bitwise_xor : 0 if both are 0 or 1, 1 if either is 1 (Applies a logical XOR operation)
#Bitwise_not : 0 if 1, 1 if 0 (Inverts the pixels)

import cv2
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# Bitwise OR
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)

