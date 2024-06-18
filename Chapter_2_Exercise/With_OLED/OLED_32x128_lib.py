#!/usr/bin/python
# ref: https://pinout.xyz/pinout/i2c
# ref: https://raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
# ref: https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/
# ref: https://github.com/crismc/rpi_i2c_oled/
# ref: https://pillow.readthedocs.io/en/stable/reference/Image.html

import time
from SSD1306 import SSD1306_128_32
from IMG2OLED import extract_img
from IMG2OLED import binary_scale

import numpy as np
from PIL import Image, ImageFont, ImageDraw

class OLED_32x128():
    def __init__(self, db_path = './DB', based_canvas = 'white'):
        self.the_oled = SSD1306_128_32()
        self.based_canvas = based_canvas # white / ruler / disk / RAM ...
        self.db_path = db_path
        self.temporary_canvas = Image.fromarray(np.zeros((32, 128)))
        self.canvas = Image.fromarray(np.zeros((32, 128)))
        self.prev_canvas = Image.fromarray(np.zeros((32, 128)))

    def start(self):
        self.load_canvas()
        self.the_oled.begin()
        self.the_oled._buffer = extract_img(self.canvas)
        self.the_oled.display()

    def clear(self):
        self.the_oled.clear()
        self.display()

    def set_based_canvas(self, based_canvas='white', reload_canvas = False):
        self.based_canvas = based_canvas
        if reload_canvas == True:
            self.load_canvas()

    def save_canvas(self, canvas=None):
        if canvas != None:
            canvas.save(self.db_path+'/being_used_imgs/based_canvas_prev.jpg')
        else:
            self.canvas.save(self.db_path+'/being_used_imgs/based_canvas_prev.jpg')

    def load_canvas(self, based_canvas=None, clear_prev=True):
        if based_canvas == None:
            based_canvas = self.based_canvas
        if based_canvas == 'white':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_white.jpg')
        elif based_canvas == 'black':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_black.jpg')
        elif based_canvas == 'ruler':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_ruler.jpg')
        elif based_canvas == 'disk':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_disk.jpg')
        elif based_canvas == 'ram':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_ram.jpg')
        elif based_canvas == 'cpu':
            self.canvas = Image.open(self.db_path+'/based_imgs/based_canvas_cpu.jpg')
        elif based_canvas == 'prev':
            self.canvas = Image.open(self.db_path+'/being_used_imgs/based_canvas_prev.jpg')
        if clear_prev == True:
            self.prev_canvas = self.canvas

    def display(self):
        self.the_oled.display()
    
    def add_text(self, text="HelloW!", pos=(0, 0), size=12, color=(255,255,255), load_prev=False, save_curr=False):
        Img = self.canvas.copy()
        if load_prev == True:
            Img = self.prev_canvas.copy()
        DrawnImg = ImageDraw.Draw(Img)
        FontImg = ImageFont.truetype(self.db_path+'/fonts/SVN-Arial-2-bold.ttf', size)
        DrawnImg.text(pos, text, color, FontImg)
        if save_curr == True:
            self.prev_canvas = Img
        self.the_oled._buffer = extract_img(Img, thres=50)
        self.the_oled.display()

    def add_image(self, img, pos=(0, 0), thres=100, load_prev=False, save_curr=False):
        current_canvas = self.canvas.copy()
        if load_prev == True:
            current_canvas = self.prev_canvas.copy()
        col0, row0 = pos
        w, h = img.size
        for col in range(col0, min(col0+w, 128)):
            for row in range(row0,  min(col0+h, 32)):
                b, g, r = img.getpixel((col-col0, row-row0))
                cb, cg, cr = current_canvas.getpixel((col, row))
                if int((int(cb+int(cg)+int(cr)))/3.0) < thres:
                    if int((int(b)+int(g)+int(r))/3.0) >= thres:
                        current_canvas.putpixel((col, row), (255, 255, 255))
        if save_curr == True:
            self.prev_canvas = current_canvas
        self.the_oled._buffer = extract_img(current_canvas, thres=50)
        self.the_oled.display()

    def add_image_from_path(self, img_path='', pos=(0, 0), thres=100, load_prev=False, save_curr=False):
        img = Image.open(img_path)
        self.add_image(img, pos, thres, load_prev, save_curr)

if __name__ == "__main__":
    oled = OLED_32x128(based_canvas='black')
    oled.start()
    oled.add_text(text='CPU', pos=(64,7), save_curr=True)
    oled.add_image_from_path('./DB/based_imgs/based_canvas_cpu.jpg', pos=(0,4), load_prev=True, save_curr=True)
    time.sleep(1)
    oled.add_image_from_path('./DB/based_imgs/based_canvas_ram.jpg', pos=(70,4), load_prev=True, save_curr=True)
