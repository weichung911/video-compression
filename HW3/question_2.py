import cv2
import numpy as np

# Load the image
image = cv2.imread("foreman_qcif_0_rgb.bmp",0)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)  # Convert to YUV color space

# Define the quantization matrix
quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])


# Split the image into 8x8 blocks
blocks = [image[i:i+8, j:j+8] for i in range(0, image.shape[0], 8) for j in range(0, image.shape[1], 8)]

# DCT, quantization, inverse quantization, and IDCT for each block
decoded_blocks = []
for block in blocks:
    # DCT
    dct_block = cv2.dct(np.float32(block))

    # Quantization
    quantized_block = np.round(dct_block / quantization_matrix)

    # Inverse quantization
    dequantized_block = quantized_block * quantization_matrix

    # IDCT
    idct_block = cv2.idct(np.float32(dequantized_block))

    decoded_blocks.append(idct_block)

# Reconstruct the image from the decoded blocks
reconstructed_image = np.zeros_like(image[:, :])
for idx, block in enumerate(decoded_blocks):
    i = (idx // (image.shape[1] // 8)) * 8
    j = (idx % (image.shape[1] // 8)) * 8
    reconstructed_image[i:i+8, j:j+8] = block

reconstructed_image = reconstructed_image.astype(np.uint8)
# Display the decoded frame
cv2.imshow("Decoded Frame", reconstructed_image)
cv2.imshow('im',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
