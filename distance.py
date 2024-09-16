from machine import Pin, ADC
import time

ir_rangefinder = ADC(Pin(33))
led_pin = Pin(2, Pin.OUT)

while True:
    reading = ir_rangefinder.read()
    if reading > 1700:
        led_pin.on()
    else:
        led_pin.off()
    print(reading)
    time.sleep_ms(75)
