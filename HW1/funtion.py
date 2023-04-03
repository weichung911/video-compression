import cv2 as cv
import numpy as np
import os
import io
import matplotlib.pyplot as PLT
from tabulate import tabulate

def RGB2Ycbcr(img_rgb):
    filter = np.array([[0.183,0.614,0.062],
                        [-0.101,-0.339,0.439],
                        [0.439,-0.399,-0.040]])
    # BGR to RGB
    bgr = img_rgb.astype(np.double)
    bgr = img_rgb
    rgb = cv.merge((bgr[:,:,2], bgr[:,:,1], bgr[:,:,0]))
    img_Ycbcr = rgb.dot(filter.T)
    img_Ycbcr[:,:,0] += 16
    img_Ycbcr[:,:,[1,2]] += 128
    img_Ycbcr = img_Ycbcr.astype(np.uint8)
    return img_Ycbcr

def Downsample(img):
    height, width = img.shape
    downsample_img = np.zeros((height//2,width//2))
    for h in range(0,height,2):
        for w in range(0,width,2):
            downsample_img[h//2, w//2] = img[h, w]
    downsample_img = downsample_img.astype(np.uint8)
    return downsample_img

def cbcrcopy(img):
    height, width = img.shape
    copy_img = np.zeros((height*2, width*2))
    for h in range(height*2):
        for w in range(width*2):
            copy_img[h,w] = img[h//2, w//2]
    copy_img = copy_img.astype(np.uint8)
    return copy_img


def Ycbcr444toYcbcr420_file(img_ycbcr):
    (Y,cb,cr) = cv.split(img_ycbcr)
    # Downsample cb and cr (apply 420 format)
    cb = Downsample(cb)
    cr = Downsample(cr)
    # cv.imshow('Y',Y)
    # cv.imshow('cb',cb)
    # cv.imshow('cr',cr)
    # Open In-memory bytes streams (instead of using fifo)
    f = io.BytesIO()
    # Write Y, U and V to the "streams".
    f.write(Y.tobytes())
    f.write(cb.tobytes())
    f.write(cr.tobytes())
    f.seek(0)
    return Y, cb, cr, f, Y.shape

def Ycbcr420_file2img(f,Y_shape):
    f.seek(0)
    Y_data = f.read(Y_shape[0]*Y_shape[1])
    cb_data = f.read((Y_shape[0]*Y_shape[1])//4)
    cr_data = f.read((Y_shape[0]*Y_shape[1])//4)
    Y_img = np.frombuffer(Y_data, np.uint8).reshape(Y_shape[0], Y_shape[1])
    cb_img = np.frombuffer(cb_data, np.uint8).reshape(Y_shape[0]//2, Y_shape[1]//2)
    cr_img = np.frombuffer(cr_data, np.uint8).reshape(Y_shape[0]//2, Y_shape[1]//2)
    # resize cbcr cbcr to be the same size as Y 
    cb_img = cbcrcopy(cb_img)
    cr_img = cbcrcopy(cr_img)

    Ycbcr420 = cv.merge((Y_img, cb_img, cr_img))

    return Ycbcr420

def Ycbcr2BGR(img_Ycbcr):

    filter = np.array([[1.164, 0, 1.793],
                      [1.164, -0.213, -0.533],
                      [1.164, 2.112, 0.000]])
    Ycbcr = img_Ycbcr.astype(np.double)
    Ycbcr[:,:,0] -= 16
    Ycbcr[:,:,[1,2]] -= 128
    rgb = Ycbcr.dot(filter.T)
    # RGB to BGR
    img_BGR = cv.merge((rgb[:,:,2],rgb[:,:,1],rgb[:,:,0]))
    img_BGR = np.uint8(img_BGR)

    return img_BGR

def build_table(li=[]):
    table = np.zeros([8])
    for i, img in enumerate(li):
        for c in range(3):
            hist = cv.calcHist([img],[c],None,[8],[0, 8])
            table = np.sum([hist.flatten(),table],axis=0).tolist()
    sum_t = sum(table)
    probability = [item/sum_t for item in table]
    print(probability)
    
    info = {
        'code':[],
        'sym':[0,1,2,3,4,5,6,7],
        'probability':probability
    }
    print(tabulate(info, headers='keys'))





    

