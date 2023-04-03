import cv2 as cv
import numpy as np
from funtion import RGB2Ycbcr, Ycbcr444toYcbcr420_file, Ycbcr420_file2img, Ycbcr2BGR, build_table

frame_rgb = []
frame_ycbcr = []
for i in range(3):
    frame_rgb.append(cv.imread("foreman_qcif_"+ str(i) +"_rgb.bmp"))
    frame_ycbcr.append(RGB2Ycbcr(frame_rgb[i]))
    frame_ycbcr[i] = (frame_ycbcr[i]/32).astype(np.uint8)

build_table(frame_ycbcr)