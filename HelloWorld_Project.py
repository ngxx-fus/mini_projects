import RPi.GPIO as GPIO
import datetime
from gpiozero import LED 
from time import sleep 

print("GPIO declaration...");
#declaration pinouts
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

pin0, pin1, pin2, pin3, pin4 = (5,6,13,19,26)

GPIO.setup(pin0, GPIO.IN)
LED1, LED2, LED3, LED4 = LED(pin1), LED(pin2), LED(pin3),LED(pin4)

print("Done!\n");
print("Running...");
#my code here
MODE = 0
loop_count = 1000000;

def SET_MODE_0():
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    sleep(0.2)
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    sleep(0.2)

def SET_MODE_1():
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.on()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    sleep(0.2)

def SET_MODE_2():
    LED1.on()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.off()
    LED2.on()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.off()
    LED2.off()
    LED3.on()
    LED4.off()
    sleep(0.2)
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.on()
    sleep(0.2)

def SET_MODE_3():
    LED1.off()
    LED2.on()
    LED3.off()
    LED4.on()
    sleep(0.2)
    LED1.on()
    LED2.off()
    LED3.on()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.on()
    LED3.off()
    LED4.on()
    sleep(0.2)
    LED1.on()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(0.2)
    LED1.on()
    LED2.off()
    LED3.off()
    LED4.on()
    sleep(0.2)

print("Current mode 0")
while( loop_count ):
    loop_count = loop_count - 1
    #hehe
    match MODE:
        case 0:
            #print("\tCASE 0")
            SET_MODE_1()
        case 1:
            #print("\tCASE 1")
            SET_MODE_2()
        case 2:
            #print("\tCASE 2")
            SET_MODE_3()
        case _:
            #print("\tCASE 3")
            SET_MODE_0()
    if GPIO.input(pin0) == True :
        MODE = (MODE + 1)%4
        SET_MODE_0()
        print("Changed mode {}!".format(MODE))
        #sleep(2)
        
print("Done!\n")
