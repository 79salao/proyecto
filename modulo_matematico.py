
balance = 100

apuesta = 0

arrayDePremios = []

arrayDeApuestas = []

def anadirJugada(apuesta, premio):
    arrayDePremios.append(premio)
    arrayDeApuestas.append(apuesta)

def calcularTotal():
    total = 0
    for i in range(len(arrayDePremios)):
        total = total + arrayDePremios[i]
    for i in range(len(arrayDeApuestas)):
        total = total - arrayDeApuestas[i]
    return total    

def subirApuesta():
    if apuesta == balance:
        pass
    else:
        apuesta = apuesta + 1

def bajarApuesta():
    if apuesta == 1:
        pass
    else:
        apuesta = apuesta - 1

def restarApuesta():
    balance = balance - apuesta

def reiniciarApuesta():
    apuesta = 0

def calcularPremio(apuesta, color):
    if color == "blanco":
        return apuesta * 10
    elif color == "amarillo":
        return apuesta * 1.5
    elif color == "verde":
        return apuesta * 3
    elif color == "rojo":
        return 0

def getApuesta():
    return apuesta

def getBalance():
    return balance