import time

import time
import datetime
import RPi.GPIO as GPIO
from IMG2OLED import extract_img
from OLED_32x128_lib import OLED_32x128



def get_time(i, f):
    return (f-i).total_seconds()

def get_distance(trig, echo):

    # transmit
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.000001)
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(trig, GPIO.LOW)

    # wait and receive
    i = datetime.datetime.now()
    while GPIO.input(echo) == GPIO.LOW:
        if (datetime.datetime.now() - i).total_seconds() > 1:
            return -1

    i = datetime.datetime.now()
    while GPIO.input(echo) == GPIO.HIGH:
        if (datetime.datetime.now() - i).total_seconds() > 1:
            return -2
    f = datetime.datetime.now()

    # compute the distance

    return get_time(i, f) * 343 * 100 / 2;

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    ledpin = [13, 19, 26]
    buttonpin = [6]
    trig = 22
    echo = 27

    GPIO.setup(ledpin, GPIO.OUT)
    GPIO.setup(buttonpin, GPIO.IN) 
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.HIGH)

    oled = OLED_32x128(based_canvas='ruler')
    oled.start()

    for loop_c in range(100000):
        d = round(get_distance(trig, echo), 4)
        if abs(d-(-1)) < 0.001 :
            oled.based_canvas = 'black'
            oled.load_canvas()
            oled.add_text(text="E: LOW Timeout!", pos=(3,8))
        elif abs(d-(-2)) < 0.001 :
            oled.based_canvas = 'black'
            oled.load_canvas()
            oled.add_text(text="E: HIGH Timeout", pos=(3,8))
        else:
            oled.based_canvas = 'ruler'
            oled.load_canvas()
            oled.add_text(text=str(d), pos=(64,7))
        # time.sleep(1)
        

if __name__ == "__main__":
    main()