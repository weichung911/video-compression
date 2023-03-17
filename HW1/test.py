import cv2 as cv
import numpy as np
from scipy import signal

# 定义RGB到YCbCr的转换矩阵
RGB2YCbCr = np.array([[0.299, 0.587, 0.114],
                      [-0.169, -0.331, 0.5],
                      [0.5, -0.419, -0.081]])


def rgb2ycbcr(img):
    # 将图像数据类型转换为浮点型，并归一化到0-1之间
    img = img.astype(np.double) / 255.

    # 对RGB图像进行矩阵乘法运算，得到YCbCr图像
    ycbcr420 = np.dot(img, RGB2YCbCr.T)

    # 对Cb和Cr分量进行4:2:0采样
    # Cb = signal.convolve2d(ycbcr[:, :, 1], np.ones((2, 2)), mode='valid')[::2, ::2]
    # Cr = signal.convolve2d(ycbcr[:, :, 2], np.ones((2, 2)), mode='valid')[::2, ::2]

    # # 将Y、Cb和Cr分量合并为YCbCr 4:2:0格式的图像
    # ycbcr420 = np.zeros((img.shape[0] // 2, img.shape[1] // 2, 3))
    # ycbcr420[:, :, 0] = ycbcr[::2, ::2, 0]
    # ycbcr420[:, :, 1] = Cb
    # ycbcr420[:, :, 2] = Cr

    return ycbcr420
foreman_qcif_0_rgb = cv.imread('foreman_qcif_0_rgb.bmp')
ycbcr420 = rgb2ycbcr(foreman_qcif_0_rgb)

cv.imshow('RGB',foreman_qcif_0_rgb)
cv.imshow('resize',ycbcr420)
cv.waitKey(0)
