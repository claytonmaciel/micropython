import time
from machine import Pin

led = Pin(4,Pin.OUT)
led.value(False)

while True:
    led.value(not led.value())
    time.sleep(1)