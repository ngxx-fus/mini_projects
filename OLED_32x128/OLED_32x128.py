#!/usr/bin/python
# ref: https://pinout.xyz/pinout/i2c
# ref: https://raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
# ref: https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/
# ref: https://github.com/crismc/rpi_i2c_oled/

import time
from SSD1306 import *
from img_extraction import *


def main():
	imgs_path = "./imgs"
	imgs_list = ["frame0.jpg", "frame1.jpg", "frame2.jpg", "frame3.jpg"]

	extracted_frames = extract_set_img(imgs_path, imgs_list)

	print(extracted_frames)

	my_oled = SSD1306_128_32()
	my_oled.begin()
	repeat = 10
	for it in range(repeat):
		my_oled.clear()
		for frame in extracted_frames:
			my_oled._buferr = frame
			my_oled.display()
			time.sleep(1)

if __name__ == "__main__":
	main()
