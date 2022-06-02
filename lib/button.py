from machine import Pin

class Button:
    def __init__(self, button_pin):
        self.button = Pin(button_pin, Pin.IN)
        
    #Returns if button is pressed or not
    def is_button_pressed(self):
        logic_state = self.button.value()
        return logic_state
