import time
import RPi.GPIO as GPIO
from OLED_32x128_lib import OLED_32x128

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LEDpin = [26, 19, 13]
BUTTONpin = [6]
State  = [[1,  0,  0 ],
	[0, 1, 0 ],
	[0, 0, 1 ]]

if __name__ == "__main__":
	oled = OLED_32x128(based_canvas='white')
	oled.start()

	GPIO.setup(LEDpin, GPIO.OUT)
	GPIO.setup(BUTTONpin, GPIO.IN)
	GPIO.output(LEDpin, State[0])

	mode = 0
	oled.add_text("Mode {} | {}".format(mode, State[mode]), (4,7), color=(0,0,0), size=14)
	print("Current mode: {}".format(mode))
	while True :
		if GPIO.input(BUTTONpin[0]) == GPIO.HIGH:
			oled.add_text("Mode {} | {}".format(mode, State[mode]), (4,7), color=(0,0,0), size=14)
			mode = (mode+1)%3
			print("Current mode: {}".format(mode))
			GPIO.output(LEDpin, State[mode])
			time.sleep(0.200)
