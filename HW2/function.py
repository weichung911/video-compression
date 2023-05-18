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
        raise Exception("SAD_block : current_block.shape "+str(current_block.shape)+"!= "+str(search_block.shape)+"search_block.shape")
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
def intra_prediction(pixel_block, mode):
    # 定义像素块的大小和模式
    block_size = pixel_block.shape[0]
    assert block_size == pixel_block.shape[1]
    
    # 创建一个空的预测块
    predicted_block = np.zeros((block_size, block_size))

    if mode == 2:
        # Mode 2: DC prediction (平均值预测)
        dc_value = np.mean(np.concatenate((pixel_block[0][1:],pixel_block[1:,0])))
        predicted_block.fill(dc_value)
        
    elif mode == 1:
        # Mode 1: 垂直预测
        for i in range(block_size):
            predicted_block[:, i] = pixel_block[:, 0]
            
    elif mode == 0:
        # Mode 0: 水平预测
        for i in range(block_size):
            predicted_block[i, :] = pixel_block[0, :]
            
    elif mode == 4:
        # Mode 4: 左上角像素预测
        predicted_block = pixel_block.copy()
        for i in range(1,block_size):
            for j in range(1,block_size):
                if i ==  j :
                    predicted_block[i, j] = predicted_block[0, 0]
                else:
                    predicted_block[i, j] = predicted_block[i-1, j-1]
    
    # 返回预测块
    return predicted_block[1:,1:]

def prediction_mode(block):
    mode_0 = SAD_block(block[1:,1:],intra_prediction(block,0))
    mode_1 = SAD_block(block[1:,1:],intra_prediction(block,1))
    mode_2 = SAD_block(block[1:,1:],intra_prediction(block,2))
    mode_4 = SAD_block(block[1:,1:],intra_prediction(block,4))
    # print(block[1:,1:])
    # print(intra_prediction(block,4))
    # print([mode_0,mode_1,mode_2,mode_4])
    min = np.argmin([mode_0,mode_1,mode_2,mode_4])
    # print(min)
    if min == 3:
        return 4
    else:
        return min
    
def zero_padding(image, padding):
    padded_image = np.pad(image, ((padding, padding), (padding, padding)), mode='constant')
    return padded_image



