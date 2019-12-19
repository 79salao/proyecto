import modulo_luces
import modulo_email
import modulo_mando
import modulo_matematico
import modulo_pantalla
import modulo_sonidos
import modulo_archivos
import random

def girar():
    modulo_pantalla.mensajeGiro()
    direccion = random.choice([True, False])
    velocidad = random.uniform(0.10, 0.25)
    while True:
        keyStop = modulo_mando.teclaMando()
        modulo_luces.girarRuleta(keyStop, direccion,velocidad,modulo_matematico.getApuesta())
        if keyStop == "KEY_1":
            break
        
def salir():
    modulo_pantalla.despedida()
    modulo_archivos.escribirFinal()
    modulo_email.enviarEmail()

def inicio():
    modulo_luces.apagarLuces()
    modulo_pantalla.bienvenida()
    while True:
        keyInicio = modulo_mando.teclaMando()
        modulo_luces.bienvenida(keyInicio)
        if keyInicio == "KEY_1":
            break

def apostar():
    modulo_pantalla.mostrarBalance(modulo_matematico.getBalance())
    modulo_pantalla.seleccioneApuesta()
    while True:
        modulo_pantalla.mostrarApuesta()
        keyApuesta = modulo_mando.teclaMando()
        if keyApuesta == "KEY_1":
            modulo_matematico.subirApuesta()
        elif keyApuesta == "KEY_2":
            modulo_matematico.bajarApuesta()
        elif keyApuesta == "KEY_3":
            modulo_pantalla.apuestaSeleccionada()
            break

inicio()
apostar()
girar()

while True:
    keyContinue = modulo_mando.teclaMando()
    if keyContinue == "KEY_1":
        apostar()
        girar()
    elif keyContinue == "KEY_2":
        salir()
