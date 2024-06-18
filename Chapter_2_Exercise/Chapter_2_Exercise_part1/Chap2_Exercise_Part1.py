import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LEDpin = [26, 19, 13]
BUTTONpin = [6]
State  = [[1,  0,  0 ],
	[0, 1, 0 ],
	[0, 0, 1 ]]



if __name__ == "__main__":
	GPIO.setup(LEDpin, GPIO.OUT)
	GPIO.setup(BUTTONpin, GPIO.IN)
	GPIO.output(LEDpin, State[0])

	mode = 0
	print("Current mode: {}".format(mode))
	while True :
		if GPIO.input(BUTTONpin[0]) == GPIO.HIGH:
			mode = (mode+1)%3
			print("Current mode: {}".format(mode))
			GPIO.output(LEDpin, State[mode])
			time.sleep(0.200)
