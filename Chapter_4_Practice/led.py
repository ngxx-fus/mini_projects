import RPi.GPIO as GPIO
import datetime
import time

#set # is GPIO, not # in board
GPIO.setmode(GPIO.BCM)
#turn off warning for pins is re-configed
GPIO.setwarnings(False)

#list of output
Pin = [ 3, 19, 26]

#set pin is output pin
GPIO.setup(pin, GPIO.OUT)

#list of state
St = [[ GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
	[GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
	[GPIO.HIGH, GPIO.LOW, GPIO.HIGH],
	[GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
	[GPIO.HIGH, GPIO.LOW, GPIO.LOW],
	[GPIO.LOW, GPIO.LOW, GPIO.LOW],
	[GPIO.HIGH, GPIO.HIGH, GPIO.HIGH],
	[GPIO.LOW, GPIO.LOW, GPIO.LOW],
	[GPIO.LOW, GPIO.HIGH, GPIO.LOW],
	[GPIO.HIGH, GPIO.HIGH, GPIO.HIGH]]

if __name__ == "__main__":
	
