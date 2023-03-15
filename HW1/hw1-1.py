import cv2 as cv
import numpy as np
import os
foreman_qcif_0_rgb = cv.imread('foreman_qcif_0_rgb.bmp')
print(type(foreman_qcif_0_rgb))
cv.imshow('im',foreman_qcif_0_rgb)
cv.waitKey(0)
 