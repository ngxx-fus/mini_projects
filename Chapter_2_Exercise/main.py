import RPi.GPIO as GPIO
import time
from my_func import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin = [6, 26, 19, 13]
IO  = [1, 0,  0,  0 ]
St  = [[0, 1,  0,  0 ],
	[0, 0, 1, 0 ],
	[0, 0, 0, 1 ]]



if __name__ == "__main__":
	mode = 0
	print("Current mode: {}".format(mode))
	pin_setup(pin, IO, St[mode])
	while True :
		if GPIO.input(pin[0]) == GPIO.HIGH:
			mode = (mode+1)%3
			print("Current mode: {}".format(mode))
			set_state(pin[1:], St[mode][1:])
			time.sleep(0.200)
