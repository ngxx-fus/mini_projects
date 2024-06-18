import numpy as np
from PIL import Image
import cv2

def binary_scale(img):
	return img.convert('1')

def extract_img(img, thres=100):
	w, h = img.size
	# print("Processing img ", (h, w))

	pkt_list = []
	pkt_ac = 0

	for page in range(4):
		for col in range(w):
			pkt_ac = 0
			for row in range(page*8, page*8+8):
				"""pixel"""
				r, g, b = img.getpixel((col, row))
				gray = (int(r)+int(g)+int(b))/3
				gray = int(gray)
				if( gray >= thres):
					pkt_ac = pkt_ac + (2**(row%8))
			pkt_list.append(pkt_ac)
			pkt_ac  = 0


	# print("Packet len: ", len(pkt_list), '\n')
#    k = 0
#    for i in range(16):
#        for j in range(32):
#            print(f" {pkt_list[k]},", end='')
#            k = k+1
#        print('\n', end='')
#        if (i+1)%4 == 0:
#            print('\n', end='')
	return pkt_list

def extract_set_img(imgs_path, imgs_list):
    set_of_plt_list = []
    for filename in imgs_list:
        img = cv2.imread(imgs_path + "/" + filename)
        set_of_plt_list.append(extract_img(img))
    return set_of_plt_list

if __name__ == "__main__":
    img_path = r"./DB/based_imgs/based_canvas_ruler.jpg"
    img = Image.open(img_path)
    print(extract_img(img))
