import RPi.GPIO as GPIO
import time
import datetime
from my_func import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin =  [6, 26, 19, 13]
IO  =  [1, 0,  0,  0 ]
St  =  [[0, 1,  0,  0 ],
	[0, 0, 1, 0 ],
	[0, 0, 0, 1 ]]
trig   = 27
echo   = 6


if __name__ == "__main__":
	pin_setup([trig, echo], [0, 1], [0, 0])
	pin_setup(pin, IO, St[0])
	while True :
		distance = HC_SR04_Distance(trig, echo)
		print("HC_SR04_Distance: {}".format(distance))
		if distance < 20.0:
			set_state(pin[1:], St[2][1:])
		elif distance > 80.0:
			set_state(pin[1:], St[0][1:])
		else:
			set_state(pin[1:], St[1][1:])
		time.sleep(3)
