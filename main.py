#Imports
import lib.display as display
import ultrasound
import button
import time
from machine import Pin

#Variables
sda = 2
scl = 3

trig = 14
echo = 15

button_pin = 13

pump_pin = 16

#In mm
percentage_warning = 20
min_distance = 27
max_distance = 42
warning = False

#Class init
#Display(sda, scl)
disp = display.Display(sda, scl)
#Ultrasound(trig, echo)
ult_sou = ultrasound.Ultrasound(trig, echo)
#Button(button_pin)
button = button.Button(button_pin)

pump = Pin(pump_pin, Pin.OUT)
pump.low()

distance_diff = max_distance - min_distance

#Loop
while True:
    disp.display_fill()
    
    current_distance = ult_sou.check_volume()
    current_level = current_distance - min_distance
    print(current_level)
    
    current_percentage = 100 - ((current_level / distance_diff) * 100)
    
    disp.show_current_capacity(current_percentage)
    
    if (current_percentage < percentage_warning):
        disp.show_message("Reabastecer!!")
        warning = True
    else:
        disp.show_message("Abastecimento OK")
        warning = False
    
    if(warning == False):
        if (button.is_button_pressed()):
            #Ativar a bomba
            pump.high()
        else:
            pump.low()
    else:
        print("Compartimento vazio!!")
        pump.low()
        
    disp.display_show()

    time.sleep_us(1)