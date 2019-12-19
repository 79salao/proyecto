from modulo_matematico import calcularPremio, calcularTotal, getBalance
import os

path = os.path.dirname(os.path.abspath(__file__))
pathTotal = path + "\\premios.txt"
f = open(pathTotal,"a+")
primeraVez = True 

def escribirBalance(balance):
    f.write("Estimado jugador:%d\r\n")
    write = "Tu balance era de: " + str(balance) + "%d\r\n"
    f.write(write)
    global primeraVez
    primeraVez = False
    
def escribirPremio(apuesta, color, premio):
    mensaje1 = "Apostaste: " + str(apuesta) + " pero perdiste.%d\r\n"
    mensaje2 = "Apostaste: " + str(apuesta) + "y ganaste " + str(premio) + "€%d\r\n"
    if primeraVez:
        escribirBalance(getBalance())
    if color == "rojo":
        f.write(mensaje1)
    else:
        f.write(mensaje2)
        
def escribirFinal():
    mensaje1 = "Resultado: has perdido " + str(calcularTotal()) + "€"
    mensaje2 = "Resultado: en total has ganado " + str(calcularTotal()) + "€"
    if calcularTotal() < 0:
        f.write(mensaje1)    
    elif calcularTotal() > 0:
        f.write(mensaje2)
    f.write("Gracias por jugar con nosotros.%d\r\n")
    f.write("Vuelve pronto!%d\r\n")

def borrarArchivo():
    f.truncate(0)

def getPath():
    return pathTotal

