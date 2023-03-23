import cv2 as cv
import numpy as np
import os
import io
from funtion import RGB2Ycbcr, Ycbcr444toYcbcr420_file, Ycbcr420_file2img ,Ycbcr2BGR


foreman_qcif_0_rgb = cv.imread('foreman_qcif_0_rgb.bmp')
foreman_qcif_0_Ycbcr = RGB2Ycbcr(foreman_qcif_0_rgb)
f_0_Y, f_0_cb, f_0_cr, f_0, f_0_shape= Ycbcr444toYcbcr420_file(foreman_qcif_0_Ycbcr)
foreman_qcif_0_Ycbcr420 = Ycbcr420_file2img(f_0, f_0_shape)
f_0_bgr = Ycbcr2BGR(foreman_qcif_0_Ycbcr420)
cv.imshow('RGB',foreman_qcif_0_rgb)
cv.imshow('Ycbcr',foreman_qcif_0_Ycbcr)
cv.imshow('Y',f_0_Y)
cv.imshow('cb',f_0_cb)
cv.imshow('cr',f_0_cr)
cv.imshow('Ycbcr420',foreman_qcif_0_Ycbcr420)
cv.imshow('bgr',f_0_bgr)
cv.waitKey(0)
 