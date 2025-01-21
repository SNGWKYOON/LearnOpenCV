import cv2

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)
def rescaleFrame(frame, scale=0.75): # resized 75% of original size
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

resized_image = rescaleFrame(img)
cv2.imshow('Cat Resized', resized_image)
cv2.waitKey(0)

# capture = cv2.VideoCapture('../LearnOpenCV/myenv/videos/video1.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, scale=0.2) # resized 20% of original size
#     cv2.imshow('Video', frame)
#     cv2.imshow('Video Resized', frame_resized)
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv2.destroyAllWindows()
