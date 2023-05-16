import cv2 as cv
import numpy as np

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

def SAD_block(current_block, search_block):
    if current_block.shape != search_block.shape:
        raise Exception("SAD_block : current_block.shape != search_block.shape")
    return np.sum(np.abs(search_block - current_block))

def Full_search(block, search_area,block_point,search_point):
    h, w = search_area.shape
    h_b , w_b = block.shape
    search_block = search_area[0:h_b,0:w_b]
    # print(block.shape,search_block.shape)
    Motion_Vector_sad = SAD_block(block,search_block)
    mv = [0,0]
    for y in range(1,h-h_b):
        for x in range(1,w-w_b):
            search_block = search_area[y:y+h_b,x:x+w_b]
            tmp_sad = SAD_block(block,search_block)
            if tmp_sad < Motion_Vector_sad :
                mv = np.array(search_point) + np.array([x,y]) - np.array(block_point)
                mv.tolist
    return mv
