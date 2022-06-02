from machine import Pin
import time
     
class Ultrasound:
    def __init__(self, trig_pin, echo_pin):
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN, Pin.PULL_DOWN)
        
    def check_volume(self):
        self.trig.value(0)
        time.sleep(0.1)
        self.trig.value(1)
        time.sleep_us(2)
        self.trig.value(0)
        while self.echo.value() == 0:
            pulse_start = time.ticks_us()
        while self.echo.value() == 1:
            pulse_end = time.ticks_us()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 2 / 29.1
        distance = round(distance, 0)
        return distance
