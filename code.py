import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Task01.jpg", 0)
kernel = np.ones((5,5), np.float32)/25
gblur = cv2.GaussianBlur(img, (5,5), 0)

sobelX=cv2.Sobel(gblur,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(gblur,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelcombined=cv2.bitwise_or(sobelX,sobelY)

cv2.imwrite("output.jpg", sobelcombined)
