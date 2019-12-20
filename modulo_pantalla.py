import smbus
import time
import modulo_matematico

iniciada = False

I2C_ADDR  = 0x27 
LCD_WIDTH = 16   
LCD_CHR = 1 
LCD_CMD = 0 
LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0 
LCD_LINE_3 = 0x94 
LCD_LINE_4 = 0xD4
LCD_BACKLIGHT  = 0x08
ENABLE = 0b00000100
E_PULSE = 0.0005
E_DELAY = 0.0005
bus = smbus.SMBus(1)

def lcd_init():
  lcd_byte(0x33,LCD_CMD) 
  lcd_byte(0x32,LCD_CMD) 
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD) 
  lcd_byte(0x28,LCD_CMD) 
  lcd_byte(0x01,LCD_CMD) 
  time.sleep(E_DELAY)
def lcd_byte(bits, mode):
  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)
def lcd_toggle_enable(bits):
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)
def lcd_string(message,line):
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
    
########################################################

def bienvenida():
  global iniciada
  if iniciada == False:
    lcd_init()
    iniciada = True
  lcd_string("Bienvenido!",LCD_LINE_1)
  lcd_string("Gira la ruleta!",LCD_LINE_2)

def mostrarApuesta():
  apuesta = modulo_matematico.apuesta
  mensaje = str(apuesta) + "€"
  lcd_string("La apuesta es de:",LCD_LINE_1)
  lcd_string(mensaje,LCD_LINE_2)

def mostrarPremio(premio):
  mensaje = str(premio) + "€!"
  lcd_string("PREMIO! HAS GANADO",LCD_LINE_1)
  lcd_string(mensaje,LCD_LINE_2)

def mostrarBalance():
  balance = modulo_matematico.balance
  mensaje = str(balance) + "€"
  lcd_string("Tu balance es de",LCD_LINE_1)
  lcd_string(mensaje,LCD_LINE_2)

def despedida():
  lcd_string("Email enviado!",LCD_LINE_1)
  lcd_string("Vuelve pronto!",LCD_LINE_2)

def noPremio():
  lcd_string("No te ha tocado",LCD_LINE_1)
  lcd_string("Sigue intentandolo!",LCD_LINE_2)

def mensajeGiro():
  lcd_string("Girando ruleta!",LCD_LINE_1)
  lcd_string("Buena suerte!",LCD_LINE_2)

def selectapuesta():
  lcd_string("Selecione una apuesta!",LCD_LINE_1)
  lcd_string("Diviertase!!",LCD_LINE_2)


def apuestaselecionada(apuesta):
  mensaje = str(apuesta) + "€"
  lcd_string("Usted a selecionado",LCD_LINE_1)
  lcd_string(mensaje,LCD_LINE_2)


def email():
  lcd_string("Introduzca su email", LCD_LINE_1)
  lcd_string("Gracias!! ",LCD_LINE_2)













