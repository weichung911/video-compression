import cv2 as cv
import numpy as np
from funtion import RGB2Ycbcr, Ycbcr444toYcbcr420_file, Ycbcr420_file2img, Ycbcr2BGR, build_table,huffman_encode,huffman_decode
import io

frame_rgb = []
frame_ycbcr = []
bitstream = ''
width = 176
height = 144
channel = 3
f = open('question2_with_subsampling.yuv','rb')
tmp_f = io.BytesIO()
for i in range(3):
    tmp = f.read(int(height*width*1.5))
    tmp_f.write(tmp)
    frame_ycbcr.append(Ycbcr420_file2img(tmp_f,(height,width)))
    tmp_f.seek(0)
    tmp_f.truncate(0)
    # frame_rgb.append(cv.imread("foreman_qcif_"+ str(i) +"_rgb.bmp"))
    # frame_ycbcr.append(RGB2Ycbcr(frame_rgb[i]))
    frame_ycbcr[i] = (frame_ycbcr[i]/32).astype(np.uint8)

info, code, root = build_table(frame_ycbcr)

for img in frame_ycbcr:
    for c in range(3):
        tmp = img[:,:,c].flatten()
        bitstream += ''.join(str(p) for p in tmp)

encode_stream = huffman_encode(bitstream,code)
# print(encode_stream)
decode_stream = huffman_decode(encode_stream, root)
# print(decode_stream)

decode_frame = []
de_ycbvr = []
for i in range(len(decode_stream)//(height*width*channel)):
    tmp = decode_stream[:height*width*channel]
    decode_stream = decode_stream[height*width*channel:]
    img = np.fromstring(tmp, np.int8) - 48
    for j in range(channel):
        tmp_img = img[:height*width]
        img = img[height*width:]
        tmp_img = tmp_img.reshape(height,width)
        tmp_img = (tmp_img*32).astype(np.uint8)
        de_ycbvr.append(tmp_img)
    de_img = cv.merge((de_ycbvr[0],de_ycbvr[1],de_ycbvr[2]))
    de_ycbvr = []
    decode_frame.append(de_img)


print((decode_frame[0] == decode_frame[1]).all())
for i, img in enumerate(decode_frame):
    # img = Ycbcr2BGR(img)
    cv.imshow(str(i),img)
    

cv.waitKey(0)


