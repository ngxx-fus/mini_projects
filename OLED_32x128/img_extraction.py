import numpy as np
import cv2

img_path = r"frame1.jpg"

img = cv2.imread(img_path)

print(img.shape)
h, w, c = img.shape

pkt_list = []
pkt_ac = 0

for page in range(4):
    for col in range(w):
        for row in range(page*8, page*8+8):
            # print(f"row: {row} col: {col}")
            gray = img[row, col, 2]/3 + img[row, col, 1]/3 + img[row, col, 0]/3
            gray = int(gray)
            if( gray > 50):
                pkt_ac = pkt_ac + (2**(row%8))

        pkt_list.append(int(pkt_ac))
        pkt_ac  = 0

print(len(pkt_list))
k = 0
for i in range(16):
    for j in range(32):
        print(f" {pkt_list[k]},", end='')
        k = k+1
    print('\n', end='')
    if (i+1)%4 == 0:
        print('\n', end='')
