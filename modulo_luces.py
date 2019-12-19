from gpiozero import LED
import time
import random
from modulo_archivos import escribirPremio
from modulo_matematico import calcularPremio, getApuesta, restarApuesta, reiniciarApuesta, anadirJugada

led1 = LED(18)
led2 = LED(16)
led3 = LED(23)
led4 = LED(13)
led5 = LED(27)
led6 = LED(4)
led7 = LED(6)
led8 = LED(5)
led9 = LED(24)
led10 = LED(25)

arrayDeLeds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10]

def girarRuleta(stop, direccion, velocidad, apuesta):
    #direccion = random.choice([True, False])
    #velocidad = random.uniform(0.10, 0.35)
    if direccion == True:
        for i in range(len(arrayDeLeds)):
            arrayDeLeds[i].toggle()
            time.sleep(velocidad)
            if stop == True:
                color = comprobarColor()
                premio = calcularPremio(apuesta,color)
                anadirJugada(apuesta,premio)
                escribirPremio(apuesta, color, premio)
                apagarLuces()
                restarApuesta()
                reiniciarApuesta()
                break
            arrayDeLeds[i].toggle()
            time.sleep(velocidad)
    elif direccion == False:
        arrayDeLeds2 = arrayDeLeds
        for i in range(len(arrayDeLeds2)):
            arrayDeLeds[i].toggle()
            time.sleep(velocidad)
            if stop == True:
                color = comprobarColor()
                premio = calcularPremio(apuesta,color)
                anadirJugada(apuesta,premio)
                escribirPremio(apuesta, color, premio)
                apagarLuces()
                restarApuesta()
                reiniciarApuesta()
                break
            arrayDeLeds[i].toggle()
            time.sleep(velocidad)

def convertirAColor(led):
    if led == led1:
        return "blanco"
    elif led == led2 or led == led3:
        return "verde"
    elif led == led4 or led == led5:
        return "amarillo"
    else:
        return "rojo"

def onOffTodas():
    led1.toggle()
    led2.toggle()
    led3.toggle()
    led4.toggle()
    led5.toggle()
    led6.toggle()
    led7.toggle()
    led8.toggle()
    led9.toggle()
    led10.toggle()
   
def parpadear(color):
    if color == "blanco":
        for i in range(8):
            onOffTodas()
            time.sleep(0.25)
            onOffTodas()
            time.sleep(0.25)
        apagarLuces()
    if color == "verde":
        for x in range(4):
            onOffTodas()
            time.sleep(0.5)
            onOffTodas()
            time.sleep(0.5)
        apagarLuces()
    if color == "amarillo":
        for j in range(2):
            onOffTodas()
            time.sleep(0.75)
            onOffTodas()
            time.sleep(0.75)
        apagarLuces()
        
def comprobarColor():
    if led1.is_active:
        return convertirAColor(led1)
    elif led2.is_active:
        return convertirAColor(led2)
    elif led3.is_active:
        return convertirAColor(led1)
    elif led4.is_active:
        return convertirAColor(led1)
    elif led5.is_active:
        return convertirAColor(led1)
    elif led6.is_active:
        return convertirAColor(led1)
    elif led7.is_active:
        return convertirAColor(led1)
    elif led8.is_active:
        return convertirAColor(led1)
    elif led9.is_active:
        return convertirAColor(led1)
    elif led10.is_active:
        return convertirAColor(led1)

def bienvenida(salir):
    while True:
        if salir == True:
            apagarLuces()
            break
        led2.toggle()
        led4.toggle()
        led6.toggle()
        led8.toggle()
        led10.toggle()
        time.sleep(0.3)
        led2.toggle()
        led4.toggle()
        led6.toggle()
        led8.toggle()
        led10.toggle()
        led1.toggle()
        led3.toggle()
        led5.toggle()
        led7.toggle()
        led9.toggle()
        time.sleep(0.3)
        led1.toggle()
        led3.toggle()
        led5.toggle()
        led7.toggle()
        led9.toggle()
        
def apagarLuces():
    if led1.is_active:
        led1.toggle()
    if led2.is_active:
        led1.toggle()
    if led3.is_active:
        led3.toggle()
    if led4.is_active:
        led4.toggle()
    if led5.is_active:
        led5.toggle()
    if led6.is_active:
        led6.toggle()
    if led7.is_active:
        led7.toggle()
    if led8.is_active:
        led8.toggle()
    if led9.is_active:
        led9.toggle()
    if led10.is_active:
        led10.toggle()







