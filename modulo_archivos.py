from modulo_matematico import calcularPremio, calcularTotal
f = open("premios.txt","w+")

primeraVez = True

def escribirBalance(balance):
    f.write("Estimado jugador:%d\r\n")
    f.write("Tu balance era de: ", balance,"%d\r\n")
    primeraVez = False
    
def escribirPremio(apuesta, color, premio):
    if primeraVez:
        escribirBalance()
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


