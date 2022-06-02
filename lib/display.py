from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

class Display:
    def __init__(self, sda_pin, scl_pin):
        i2c = I2C(1, sda = Pin(sda_pin), scl = Pin(scl_pin), freq = 400000)
        self.display = SSD1306_I2C(128, 64, i2c)
    
    def show_message(self, message):
        self.display.text(message, 0, 32)
        
    def show_current_capacity(self, current_capacity):
        text = "Atual nivel: "
        capacity = "{}%".format(current_capacity)
        
        self.display.text("{}{}".format(text, capacity), 0, 0)
        
    def display_fill(self):
        self.display.fill(0)

    def display_show(self):
        self.display.show()
