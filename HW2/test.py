import numpy as np
from function import prediction_mode
def intra_prediction(pixel_block, mode):
    # 定义像素块的大小和模式
    block_size = pixel_block.shape[0]
    assert block_size == pixel_block.shape[1]
    
    # 创建一个空的预测块
    predicted_block = np.zeros((block_size, block_size))

    if mode == 0:
        # Mode 0: DC prediction (平均值预测)
        dc_value = np.mean(pixel_block)
        predicted_block.fill(dc_value)
        
    elif mode == 1:
        # Mode 1: 垂直预测
        for i in range(block_size):
            predicted_block[:, i] = pixel_block[:, 0]
            
    elif mode == 2:
        # Mode 2: 水平预测
        for i in range(block_size):
            predicted_block[i, :] = pixel_block[0, :]
            
    elif mode == 3:
        # Mode 3: 左上角像素预测
        predicted_block = pixel_block.copy()
        for i in range(1,block_size):
            for j in range(1,block_size):
                if i ==  j :
                    predicted_block[i, j] = predicted_block[0, 0]
                else:
                    predicted_block[i, j] = predicted_block[i-1, j-1]
    
    # 返回预测块
    return predicted_block[1:,1:]

# Example usage
pixel_block = np.array([[11, 12, 13, 14, 15],
                        [10, 20, 30, 40, 30],
                        [15, 25, 35, 45, 30],
                        [12, 22, 32, 42, 30],
                        [18, 28, 38, 48, 32]])

mode = 2# 使用 Mode 0 进行预测

predicted_block = intra_prediction(pixel_block, mode)
print(predicted_block)
# print(np.concatenate((pixel_block[0][1:],pixel_block[1:,0])))
# prediction_mode(pixel_block)