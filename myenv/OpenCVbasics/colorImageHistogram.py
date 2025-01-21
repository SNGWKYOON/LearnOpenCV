import cv2
import matplotlib.pyplot as plt

# Absolute path to the image
img = cv2.imread('/Users/seungwookyoon/LearnOpenCV/myenv/images/Cat2.jpg')

cv2.imshow('Cat', img)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)

