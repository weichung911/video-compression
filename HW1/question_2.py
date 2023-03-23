import cv2 as cv
import numpy as np
from funtion import RGB2Ycbcr, Ycbcr444toYcbcr420_file, Ycbcr420_file2img ,Ycbcr2BGR

frame_rgb = []
file_ycbcr444 = open('question2_without_subsampling.yuv','wb')
file_ycbcr444.truncate()
for i in range(3):
    frame_rgb.append(cv.imread("foreman_qcif_"+ str(i) +"_rgb.bmp"))
    (Y,cb,cr) = cv.split(frame_rgb[i])
    file_ycbcr444.write(Y.tobytes())
    file_ycbcr444.write(cb.tobytes())
    file_ycbcr444.write(cr.tobytes())
file_ycbcr444.seek(0)
file_ycbcr444.close()
file_ycbcr420 = open('question2_with_subsampling.yuv','wb')
file_ycbcr420.truncate()
for i in range(len(frame_rgb)):
    tmp_img = RGB2Ycbcr(frame_rgb[i])
    # cv.imshow('tmp_img',tmp_img)
    Y, cb, cr, tmp_file, tmp_shape = Ycbcr444toYcbcr420_file(tmp_img)
    file_ycbcr420.write(tmp_file.read())
file_ycbcr420.seek(0)
file_ycbcr420.close()

# cv.imshow('0',frame_ycbcr[0])
# cv.imshow('1',frame_ycbcr[1])
# cv.imshow('2',frame_ycbcr[2])
# cv.waitKey(0)
