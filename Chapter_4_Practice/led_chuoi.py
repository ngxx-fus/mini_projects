
from gpiozero import LED

led_red = LED(20)

while True:
    s = input("Enter command: ")
    if s in ["on","ON"]:
        print("Red LED on")
        led_red.on()
    elif s in ["off","OFF"]:
        print("Red LED off")
        led_red.off()
    elif s in ["q","quit"]:
        break
    else:
        print("Unknown command")

