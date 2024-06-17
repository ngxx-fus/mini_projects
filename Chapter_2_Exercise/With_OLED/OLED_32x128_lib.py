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

class OLED_32x128():
    def __init__(self, db_path = './DB', based_canvas = 'white'):
        self.the_oled = SSD1306_128_32()
        self.based_canvas = based_canvas # white / ruler / disk / RAM ...
        self.db_path = db_path
        self.temporary_canvas = Image.fromarray(np.zeros((32, 128)))
        self.canvas = Image.fromarray(np.zeros((32, 128)))

    def start(self):
        self.load_canvas()
        self.the_oled.begin()
        self.the_oled._buffer = extract_img(self.canvas)
        # print(extract_img(self.canvas))
        self.the_oled.display()

    def clear(self):
        self.the_oled.clear()

    def load_canvas(self):
        if self.based_canvas == 'white':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_white.jpg')
        elif self.based_canvas == 'black':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_black.jpg')
        elif self.based_canvas == 'ruler':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_ruler.jpg')
        elif self.based_canvas == 'disk':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_disk.jpg')
        elif self.based_canvas == 'ram':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_ram.jpg')
        elif self.based_canvas == 'cpu':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_cpu.jpg')

    def display(self):
        self.the_oled.display()
    
    def add_text(self, text="Hé hé!", pos=(0, 0), size=12, color=(255,255,255), clear_prev = True):
        Img = self.canvas.copy()
        DrawnImg = ImageDraw.Draw(Img)
        FontImg = ImageFont.truetype(self.db_path+'/fonts/SVN-Arial-2-bold.ttf', size)
        DrawnImg.text(pos, text, color, FontImg)
        self.the_oled._buffer = extract_img(Img)
        self.the_oled.display()

if __name__ == "__main__":
    oled = OLED_32x128(based_canvas='ruler')
    oled.start()
    oled.add_text(pos=(69, 9))
    oled.add_text(pos=(71, 9))
    oled.add_text(pos=(73, 9))
    oled.add_text(pos=(77, 9))
    oled.add_text(pos=(82, 9))
    oled.add_text(pos=(88, 9))
    oled.add_text(pos=(64, 9))