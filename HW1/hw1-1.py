import cv2 as cv
import numpy as np
import os

def RGB2Ycbcr(img_rgb):
    height ,width ,channel= img_rgb.shape
    print(height,width,channel)
    img_Ycbcr = np.zeros((height,width,channel))
    # ITU-R BT.709 Ycbcr = [16,128,128] + filter*rgb
    filter_RGB2Ycbcr = np.array([[0.183, 0.614, 0.062],
                                [-0.101, -0.339, 0.439],
                                [0.439, -0.399, -0.040]])
    for h in range (height):
        for w in range(width):
            img_Ycbcr[h,w] = [16,128,128] + filter_RGB2Ycbcr.dot(img_rgb[h,w])
    img_Ycbcr = img_Ycbcr.astype(np.uint8)
    print(img_Ycbcr[1,0])

    (R,G,B) = cv.split(img_rgb)
    cv.imshow('my_ycbcr',img_Ycbcr)
    # cv.waitKey(0)


foreman_qcif_0_rgb = cv.imread('foreman_qcif_0_rgb.bmp')
print(type(foreman_qcif_0_rgb[0,0]))
RGB2Ycbcr(foreman_qcif_0_rgb)
ycbcr = cv.cvtColor(foreman_qcif_0_rgb,cv.COLOR_BGR2YCR_CB)
cv.imshow('im',foreman_qcif_0_rgb)
cv.imshow('cV_cbcr',ycbcr)
cv.waitKey(0)
 