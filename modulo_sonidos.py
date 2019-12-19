import time
from gpiozero import Buzzer
   
buzzer = Buzzer(12)

def sonido(color):
    if color =="blanco":
        for i in range(8):
            buzzer.on()
            time.sleep(0.25)
            buzzer.off()
            time.sleep (0.25)
            
    elif color =="verde":
        for i in range(4):
            buzzer.on()
            time.sleep(0.5)
            buzzer.off()
            time.sleep(0.5)
        
    elif color =="amarillo":
        for i in range(2):
            buzzer.on()
            time.sleep(0.75)
            buzzer.off()
            time.sleep(0.75)
        

