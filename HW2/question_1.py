import cv2 as cv
from function import *

ref_frame = cv.imread('foreman_qcif_0_rgb.bmp')
current_frame = cv.imread('foreman_qcif_1_rgb.bmp')
ref_frame_ycbcr = RGB2Ycbcr(ref_frame)
current_frame_ycbcr = RGB2Ycbcr(current_frame)
ref_frame_y, ref_frame_cb, ref_frame_cr = cv.split(ref_frame_ycbcr)
current_frame_y, current_frame_cb, current_frame_cr = cv.split(current_frame_ycbcr)
cv.imshow("y",current_frame_y)
block_size = 16
search_range = 16
height, width = current_frame_y.shape
num_blocks_x = width // block_size
num_blocks_y = height // block_size
print(num_blocks_x,num_blocks_y)
idx = 0
MVs = []
# (a)
for i in range(num_blocks_y):
    for j in range(num_blocks_x):
        x = j * block_size
        y = i * block_size
        block = current_frame_y[y:y+block_size, x:x+block_size]
        block_point = [x,y]
        search_area = ref_frame_y[max(0, y-search_range):min(height, y+search_range+block_size), max(0, x-search_range):min(width, x+search_range+block_size)]
        search_point = [max(0, x-search_range),max(0, y-search_range)]
        # print(search_point)
        mv = Full_search(block,search_area,block_point,search_point)
        MVs.append([idx,mv[0],mv[1]])
        idx += 1
print("------------MV.txt------------")
for i in MVs:
    print('Block '+str(i[0])+' - ('+str(i[1])+','+str(i[2])+')')
print("------------------------------")
with open('MV.txt','w') as f:
    for mv in MVs:
        f.writelines('Block '+str(mv[0])+' - ('+str(mv[1])+','+str(mv[2])+')\n')

# (b)
collage = np.zeros((height,width))

count_b = 0
for i in range(num_blocks_y):
    for j in range(num_blocks_x):
        x = j * block_size
        y = i * block_size
        ref_x = x + MVs[count_b][1]
        ref_y = y + MVs[count_b][2]
        
        match_block = ref_frame_y[ref_y:ref_y+block_size, ref_x:ref_x+block_size]
        collage[y:y+block_size, x:x+block_size] = match_block
        # np.copyto(roi,match_block)
        count_b +=1
# collage = cv.resize(collage,(width*2,height*2))
cv.imshow("collage", collage.astype(np.uint8))
cv.waitKey(0)
