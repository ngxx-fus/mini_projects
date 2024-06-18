# OLED hxw=32x128 Lib
## Acknowledgement
The lib is based on repository ***rpi_i2c_oled*** of ***crismc***. I have re-used file ***SSD1306.py*** in the repository and added some functions to convert a JPG photo to type that can be displayed in OLED wxh=123x32. In addition, some image processing functions have been added to convert RGB images to Binary images, overlay images, and text.
## Overview

The lib consists of three files (*.py) and one folder:

    - SSD1306.py: From ***crismc***, to transmit data to OLED using I2C protocol
    - IMG2OLED.py: Convert a JPG photo to type that can be displayed in OLED wxh=123x32
    - OLED_32x128_lib.py: Contain the class OLED_32x128, provide some helpful methods :>
    - DB: This folder contains some built-in  canvas (black, white, cpu, ram, ruler) and fonts.

The demo of the lib:

    - DistanceSensor.py: Using Ultrasonic Senor to measure the distance from the sensor to things.
## Circuit diagram
<br>
<img src="https://github.com/ngxx-fus/mini_projects/assets/75427876/54bb5066-a666-4abc-af17-44934a3cc406" width="401">
<br>

## Usage
<1> Clone three files (*.py) and one folder into the workspace folder, remember that the workspace folder also includes the current *.py file (the file that is being edited/coded/programmed). 
<br><2> import OLED_32x128 

    from OLED_32x128_lib import OLED_32x128
    my_oled = OLED_32x128()
    my_oled.start()

## Desciption
| function    | decription |
| -------- | ------- |
| OLED_32x128(db_path = './DB', based_canvas = 'white')  |  ***db_path*** is the path to DB folder <br>***based_canvas*** is the type of canvas, some valid canvas is 'white', 'black', 'cpu', 'ram', 'ruler'   |
| clear()           | Eased what is shown in the OLED screen, _buffer, but canvas and prev_canvas won't be eased        |
| set_based_canvas(based_canvas='white', reload_canvas = False)          |  based_canvas: is described above <br> reload_canvas: load the canvas, but prev_canvas isn't changed       |
| save_canvas(canvas=None)          | Save the canvas, specified type: PIL.Image <br>The default path is './being_used_imgs'       |
| load_canvas(based_canvas=None, clear_prev=True)          | To load the canvas; What is shown on the OLED screen won't be changed. <br>clear_prev: clear prev_canvas         |
| display()          | Show what stored in _buffer        |
| add_text(text="HelloW!", pos=(0, 0), size=12, color=(255,255,255), load_prev=False, save_curr=False)          | Overlay TEXT in the canvas.<br> load_prev to keep previous canvas (stored in prev_canvas).<br>save_curr to store changed in prev_canvas        |
| add_image(img, pos=(0, 0), thres=100, load_prev=False, save_curr=False)          |   Same with add_text      |
| add_image_from_path(img_path='', pos=(0, 0), thres=100, load_prev=False, save_curr=False) | Same with add_image, but parameter is path instead of image (PIL.Image) |
