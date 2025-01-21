import cv2

# Absolute path to the image
# img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

# cv2.imshow('Cat', img)
capture = cv2.VideoCapture('../LearnOpenCV/myenv/videos/video1.mp4')
#capture = cv2.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
