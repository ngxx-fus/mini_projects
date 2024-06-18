import time
import datetime
import RPi.GPIO as GPIO

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
	# wait for HIGH state of ECHO (posedge)
    i = datetime.datetime.now()
    while GPIO.input(echo) == GPIO.LOW:
        if (datetime.datetime.now() - i).total_seconds() > 1:
            return -1
	# wait for LOW state of ECHO (negedge)
    i = datetime.datetime.now()
    while GPIO.input(echo) == GPIO.HIGH:
        if (datetime.datetime.now() - i).total_seconds() > 1:
            return -2
    f = datetime.datetime.now()

    # compute the distance
    return get_time(i, f) * 343 * 100 / 2;

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LEDpin = [26, 19, 13]
State  = [[1,  0,  0 ],
	[0, 1, 0 ],
	[0, 0, 1 ],
    [1, 1, 1 ]]
TRIG = 22
ECHO = 27


if __name__ == "__main__":
	GPIO.setup(LEDpin, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setup(TRIG, GPIO.OUT)

	mode = 0
	while True :
		d = get_distance(TRIG, ECHO)
		print("d= {}".format(round(d, 4)))
		if d < 0:
			GPIO.output(LEDpin, State[-1])
		elif d < 20:
			GPIO.output(LEDpin, State[0])
		elif d > 80:
			GPIO.output(LEDpin, State[2])
		else:
			GPIO.output(LEDpin, State[1])
		time.sleep(0.2)
