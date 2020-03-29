import cv2
import numpy as np
import imutils

img = cv2.imread('D:\Desktop\Capture.png')
img2 = img[365:375,13:241]
frame = img2
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = np.array([48, 236,158])
upper_blue = np.array([83, 255,225])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(frame, frame, mask=mask)
cv2.imshow("frame", frame)
cv2.imshow("mask", mask)
cv2.imshow("result", result)

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
contours = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = contours
cnts = imutils.grab_contours(cnts)
for c in cnts:
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    print(extLeft,extRight,extTop,extBot)

val = extRight[0]
print(val)
persentage = (val / 227)* 100 # 227 come from getting extreme point of total bar(which can be fill). Not shown in the code

print("the persentage is: " , persentage, "% \n")

cv2.waitKey(0)
cv2.destroyAllWindows()
