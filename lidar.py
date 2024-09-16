from servo import Servo
from machine import Pin, ADC
import time

led_pin = Pin(2, Pin.OUT)
ir_rangefinder = ADC(Pin(33))
servo1 = Servo(pin=12)
servo2 = Servo(pin=22)

for i in range(180):
    servo1.move(i)
    for j in range(150):
        servo2.move(j)
        time.sleep_ms(100)
        reading = ir_rangefinder.read()
        print(f'{i}, {j}, {reading}')


