import cv2 as cv
import numpy as np
import os

def RGB2Ycbcr(img_rgb):
    height ,width ,channel= img_rgb.shape

    print(height,width,channel)
    img_Ycbcr = np.zeros((height,width,channel))
    
    # ITU-R BT.709 Ycbcr 
    [B,G,R] = cv.split(img_rgb)
    img = np.zeros((2,3))
    Y = 0.183*R + 0.614*G + 0.062*B + 16
    cb = -0.101*R - 0.339*G + 0.439*B + 128
    cr = 0.439*R - 0.399*G - 0.040*B + 128
    img_Ycbcr[:,:,0] = Y
    img_Ycbcr[:,:,1] = cb
    img_Ycbcr[:,:,2] = cr
    img_Ycbcr = img_Ycbcr.astype(np.uint8)

    return img_Ycbcr

def Ycbcr444toYcbcr420(img_ycbcr):
    (Y,cb,cr) = cv.split(img_ycbcr)
    


foreman_qcif_0_rgb = cv.imread('foreman_qcif_0_rgb.bmp')
foreman_qcif_0_Ycbcr = RGB2Ycbcr(foreman_qcif_0_rgb)
ycbcr = cv.cvtColor(foreman_qcif_0_rgb,cv.COLOR_BGR2YCR_CB)
cv.imshow('RGB',foreman_qcif_0_rgb)
cv.imshow('Ycbcr',foreman_qcif_0_Ycbcr)
cv.imshow('cvycbcr',ycbcr)
cv.waitKey(0)
 