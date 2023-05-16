import cv2
import numpy as np
from function import SAD_block
# # Load the reference frame and the current frame
# ref_frame = cv2.imread('foreman_qcif_0_rgb.bmp')
# current_frame = cv2.imread('foreman_qcif_1_rgb.bmp')

# # Convert the frames to grayscale
# ref_gray = cv2.cvtColor(ref_frame, cv2.COLOR_BGR2GRAY)
# current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

# # Define the block size and search range
# block_size = 16
# search_range = 16

# # Calculate the number of blocks in the frame
# height, width = current_gray.shape
# num_blocks_x = width // block_size
# num_blocks_y = height // block_size

# # Initialize an array to store the motion vectors
# motion_vectors = np.zeros((num_blocks_y, num_blocks_x, 2))

# # Loop through each block in the frame and find the best matching block in the reference frame
# for i in range(num_blocks_y):
#     for j in range(num_blocks_x):
#         x = j * block_size
#         y = i * block_size
#         block = current_gray[y:y+block_size, x:x+block_size]
#         search_area = ref_gray[max(0, y-search_range):min(height, y+block_size+search_range), max(0, x-search_range):min(width, x+block_size+search_range)]
#         print(block.shape, search_area.shape)
#         result = cv2.matchTemplate(search_area, block, cv2.TM_SQDIFF_NORMED)
#         min_val, _, min_loc, _ = cv2.minMaxLoc(result)
#         motion_vectors[i, j] = np.array(min_loc) - np.array([search_range, search_range])

# # Display the motion vectors
# for i in range(num_blocks_y):
#     for j in range(num_blocks_x):
#         x = j * block_size
#         y = i * block_size
#         x1 = x + block_size // 2
#         y1 = y + block_size // 2
#         x2 = int(x1 + motion_vectors[i, j, 0])
#         y2 = int(y1 + motion_vectors[i, j, 1])
#         cv2.arrowedLine(current_frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
# cv2.imshow('Motion Vectors', current_frame)
# cv2.waitKey(0)

# a = np.array([1,1,2])
# b = np.array([2,1,1])
# print(SAD_block(a,b))
a = (0,0)
print(type(a))