import numpy as np
import cv2

img = cv2.imread('foreman_qcif_0_rgb.bmp',0)

#  Fourier Transform
img_f = np.fft.fft2(img)
fshift = np.fft.fftshift(img_f )
magnitude_spectrum = 20 * np.log(np.abs(fshift))
magnitude_spectrum = magnitude_spectrum.astype(np.uint8)
cv2.imshow('f',magnitude_spectrum)
cv2.waitKey(0)