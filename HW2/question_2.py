import cv2 as cv
from function import *

current_frame = cv.imread("foreman_qcif_0_rgb.bmp")
current_frame_Ycbcr = RGB2Ycbcr(current_frame)
current_frame_Y, current_frame_cb, current_frame_cr = cv.split(current_frame_Ycbcr)
cv.imshow("y",current_frame_Y)
block_size = 16
height, width = current_frame_Y.shape
num_blocks_x = width//block_size
num_blocks_y = height//block_size
print(num_blocks_x,num_blocks_y)
idx = 0
q2_MV=[]
# (a)
for i in range(num_blocks_y):
    for j in range(num_blocks_x):
        x = j * block_size
        y = i * block_size
        if (x == 0) and (y == 0):
            q2_MV.append([idx, -1]) 
        elif (y == 0):
            q2_MV.append([idx, 1])
        elif (x == 0):
            q2_MV.append([idx, 0])
        else:
            block = current_frame_Y[y-1:y+block_size, x-1:x+block_size]
            block_points = [x,y]
            q2_MV.append([idx,prediction_mode(block)])

        idx += 1
print('-------MV.txt---------')
for i in q2_MV:
    print('Block '+str(i[0])+' - '+str(i[1]))
print('----------------------')
with open('q2_MV.txt','w') as f:
    for mv in q2_MV:
        f.writelines('Block '+str(mv[0])+' - '+str(mv[1])+'\n')
# (b)
collage = np.zeros((height,width))

count_b = 0
for i in range(num_blocks_y):
    for j in range(num_blocks_x):
        x = j * block_size
        y = i * block_size
        padded_img = zero_padding(current_frame_Y,1)
        match_block = padded_img[y:y+block_size+1, x:x+block_size+1]
        if q2_MV[count_b][1] != -1:
            collage[y:y+block_size, x:x+block_size] = intra_prediction(match_block,q2_MV[count_b][1])
        # np.copyto(roi,match_block)
        count_b +=1

cv.imshow("collage", collage.astype(np.uint8))
cv.imwrite("q2_collage.png", collage)
cv.waitKey(0)



