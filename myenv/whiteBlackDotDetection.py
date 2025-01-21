# import cv2

# # Absolute path to the image
# path = '/Users/seungwookyoon/LearnOpenCV/myenv/images/black-dot1.jpg'

# gray = cv2.imread(path, 0)

# #threshold

# th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU) # 100 is the threshold value and 255 is the max value

# # findcontours 
# cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

# # filter by area
# s1 = 3
# s2 = 20

# xcnts = []

# for cnt in cnts:
#     if s1<cv2.contourArea(cnt) < s2:
#         xcnts.append(cnt)

# print("Total Number of black dot is ", len(xcnts))
# cv2.waitKey(0)




import cv2

# Absolute path to the image
path = '/Users/seungwookyoon/LearnOpenCV/myenv/images/white-dot.png'

gray = cv2.imread(path, 0)

#threshold

th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) # 100 is the threshold value and 255 is the max value

# findcontours 
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 3
s2 = 20

xcnts = []

for cnt in cnts:
    if s1<cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

print("Total Number of white dot is ", len(xcnts))
cv2.waitKey(0)

