#BackgroundSubtractorMOG
# import cv2
# import numpy as np

# fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     fgmask1 = fgbg1.apply(frame)

#     cv2.imshow('Original', frame)
#     cv2.imshow('MOG', fgmask1)
#     k = cv2.waitKey(30) & 0xff

#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()



#BackgroundSubtractorMOG2

# import cv2
# import numpy as np

# fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg2 = cv2.createBackgroundSubtractorMOG2()

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     fgmask1 = fgbg1.apply(frame)
#     fgmask2 = fgbg2.apply(frame)

#     cv2.imshow('Original', frame)
#     cv2.imshow('MOG1', fgmask1)
#     cv2.imshow('MOG2', fgmask2)
#     k = cv2.waitKey(30) & 0xff

#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()



#BackgroundSubtractorGMG

import cv2
import numpy as np

fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    fgmask1 = fgbg1.apply(frame)
    fgmask2 = fgbg2.apply(frame)
    fgmask3 = fgbg3.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('MOG1', fgmask1)
    cv2.imshow('MOG2', fgmask2)
    cv2.imshow('GMG', fgmask3)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

