import modulo_luces
import modulo_email
import modulo_mando
import modulo_matematico
import modulo_pantalla
import modulo_sonidos
import modulo_archivos
import random

command = ""

def girar():
    global command
    modulo_pantalla.mensajeGiro()
    direccion = random.choice([True, False])
    velocidad = random.uniform(0.05, 0.025)
    while True:
        modulo_luces.parar(command)
        modulo_luces.girarRuleta(direccion,velocidad,modulo_matematico.apuesta)
        
def salir():
    modulo_pantalla.despedida()
    modulo_archivos.escribirFinal()
    #modulo_email.enviarEmail()
    print("enviar email")

def inicio():
    global command
    modulo_luces.apagarLuces()
    modulo_pantalla.bienvenida()
    empezar = False
    while True: 
        if command == "KEY_1":
            empezar = True
            return
        modulo_luces.bienvenida(empezar)

def apostar():
    global command
    modulo_pantalla.mostrarBalance()
    #modulo_pantalla.seleccioneApuesta()
    while True:
        modulo_pantalla.mostrarApuesta()
        if command == "KEY_1":
            modulo_matematico.subirApuesta()
        elif command == "KEY_2":
            modulo_matematico.bajarApuesta()
        elif command == "KEY_3":
            #modulo_pantalla.apuestaSeleccionada()
            return

inicio()
apostar()
girar()

while True:
    global command
    if command == "KEY_1":
        apostar()
        girar()
    elif command == "KEY_2":
        salir()
