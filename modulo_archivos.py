from modulo_matematico import calcularPremio, calcularTotal, getBalance
import os

path = os.path.dirname(os.path.abspath(__file__))
pathTotal = path + "\\premios.txt"
f = open(pathTotal,"a+")
primeraVez = True

def escribirBalance(balance):
    f.write("Estimado jugador:%d\r\n")
    write = "Tu balance era de: " + balance + "%d\r\n"
    f.write(write)
    global primeraVez
    primeraVez = False
    
def escribirPremio(apuesta, color, premio):
    if primeraVez:
        escribirBalance(getBalance())
    if color == "rojo":
        f.write("Apostaste: ", apuesta, " pero perdiste.", "%d\r\n")
    else:
        f.write("Apostaste: ", apuesta, "y ganaste ", premio, "€", "%d\r\n")
        
def escribirFinal():
    if calcularTotal() < 0:
        f.write("Resultado: has perdido ", calcularTotal(),"€")    
    elif calcularTotal() > 0:
        f.write("Resultado: en total has ganado ", calcularTotal, "€")
    f.write("Gracias por jugar con nosotros.", "%d\r\n")
    f.write("Vuelve pronto!", "%d\r\n")

def borrarArchivo():
    f.truncate(0)

def getPath():
    return pathTotal
