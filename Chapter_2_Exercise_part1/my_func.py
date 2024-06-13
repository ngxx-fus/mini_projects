import RPi.GPIO as GPIO

#using GPIO# in stead off # in board
GPIO.setmode(GPIO.BCM)
#turn off warning 
GPIO.setwarnings(False)

# pin_list = [6, 13, 19, 26] 
# io_list  = [1, 0,  0,  0 ] 1 : input & 0 : output
# initial_state_list = [ x, 1, 0, 0]
# if the pin is INPUT PIN, initial_state_list value for the position of the pin is "don't care"!
def pin_setup(pin_list, io_list, initial_state_list):
	if not ( len(pin_list) == len(io_list) and len(io_list) == len(initial_state_list) ) :
		print( "pin_setup: Invalid parameters!")
		return

	for  i in range(len(pin_list)):
		if io_list[i] == 0:
			if initial_state_list[i] == 0:
				GPIO.setup( pin_list[i], GPIO.OUT, initial=GPIO.LOW)
			else:
				GPIO.setup( pin_list[i], GPIO.OUT, initial=GPIO.HIGH)
		else:
			GPIO.setup( pin_list[i], GPIO.IN)


def set_state(pin_list, state_list):
	if not ( len(pin_list) == len(state_list) ) :
		print("set_state: Invalid parameters!")
		return
	for i in range(len(pin_list)):
		GPIO.output( pin_list[i] , state_list[i])


if __name__ == "__main__":
	print("Running pins configuartions...")
	print("GPIO mode: BCM")
	print("Warning: false\nDone~\n")
