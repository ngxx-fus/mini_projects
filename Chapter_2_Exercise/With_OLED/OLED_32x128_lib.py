#!/usr/bin/python
# ref: https://pinout.xyz/pinout/i2c
# ref: https://raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
# ref: https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/
# ref: https://github.com/crismc/rpi_i2c_oled/

import time
from SSD1306 import SSD1306_128_32
from IMG2OLED import extract_img

import numpy as np
from PIL import Image, ImageFont, ImageDraw

class OLED_32x128:
    def __init__(self, db_path = '.', based_canvas = 'white'):
        self.based_canvas = 'black' # white / ruler / disk / RAM ...
        self.db_path = '.'
        self.oled = SSD1306_128_32()
        self.canvas = Image.open(DB_path+'/based_imgs/based_canvas_white.jpg')
        if based_canvas == 'black':
            canvas = Image.open(DB_path+'/based_imgs/based_canvas_black.jpg')
        elif based_canvas == 'ruler':
            canvas = Image.open(DB_path+'/based_imgs/based_canvas_ruler.jpg')
        elif based_canvas == 'disk':
            canvas = Image.open(DB_path+'/based_imgs/based_canvas_disk.jpg')
        elif based_canvas == 'ram':
            canvas = Image.open(DB_path+'/based_imgs/based_canvas_ram.jpg')
        elif based_canvas == 'cpu':
            canvas = Image.open(DB_path+'/based_imgs/based_canvas_cpu.jpg')
        oled._buffer = extract_img(canvas)

    def begin():
        oled.begin()

    def clear():
        oled.clear()

    def load_canvas():
        oled._buffer = extract_img(canvas)

    def display():
        oled.display()
    
    def add_text(text="Hello!", pos=(0, 0), size=12, color=(255,255,255)):
        DrawnImg = ImageDraw( Image.fromarray(oled._buffer))
        FontImg = ImageFont.truetype(db_path+'/fonts/', size)
        ImgDrawn.text(pos, text, color, FontImg)
        oled.__buffer = extract_img(Image.alpha_composite(DrawnImg, Image.fromarray(oled._buffer)))

if __name__ == "__main__":
    oled = OLED_32x128(based_canvas='ruler')
    oled.begin()
    oled.display()
