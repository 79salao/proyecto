# Zaragoza Roulette creado por Salahdin y Mihai

Juego de ruleta con raspberry Pi programado en Python 3.

## Componentes de hardware necesarios:

1. Necesitaremos dos boards.
2. 10 luces LED. 1 blanca, 2 amarillas, 2 verdes, y 5 rojas.
3. Una pantalla LCD.
4. Un mando.
5. Un buzzer.
6. 10 resistencias de 200 Ω.
7. 19 cables.

## Configuración de hardware:

### Configuración de LEDs:

Para los LEDs, el GND es compartido en la fila NEGATIVO de la placa IZQUIERDA.

- LED 1: GPIO 18, GND, resistencia de 200 Ω.

- LED 2: GPIO 16, GND, resistencia de 200 Ω.

- LED 3: GPIO 23, GND, resistencia de 200 Ω.

- LED 4: GPIO 13, GND, resistencia de 200 Ω.

- LED 5: GPIO 27, GND, resistencia de 200 Ω.

- LED 6: GPIO 4, GND, resistencia de 200 Ω.

- LED 7: GPIO 6, GND, resistencia de 200 Ω.

- LED 8: GPIO 5, GND, resistencia de 200 Ω.

- LED 9: GPIO 24, GND, resistencia de 200 Ω.

- LED 10: GPIO 25, GND, resistencia de 200 Ω.


### Configuración del mando:

El GND del mando se conectará a la fila NEGATIVO de la placa DERECHA.

El mando estará conectado al GPIO17, y el 3V3 será compartido en el POSITIVO de la placa DERECHA.

### Configuración del buzzer:

El GND del buzzer se conectará a la fila NEGATIVO de la placa IZQUIERDA.

El buzzer estará conectado al GPIO 12.

### Configuración de la pantalla LCD:

El GND de la pantalla se conectará a fila NEGATIVO de la placa DERECHA.

El VCC se conectará al 5VD.

El SDA estará conectado al SDA1.

El SCL estará conectado al SCL1.


## Configuración de software:

El software está escrito en Python 3, y está dividido en módulos. Cada módulo deberá importar las librerías correspondientes.

### Librerías necesarias:

1. Módulo Pantalla: 
    - Importamos smbus.
    - Importamos time.
2. Módulo Luces:
    - Desde gpiozero importamos LED.
    - Importamos time.
    - Importamos random.
    - Desde modulo_archivos importamos el método escribirPremio.
    - Desde modulo_matematico importamos los métodos calcularPremio, getApuesta, restarApuesta, reiniciarApuesta, añadirJugada
3. Módulo Archivo:
    - Desde modulo_matematico importamos los métodos calcularPremio, calcularTotal , getBalance
4. Módulo Mando:
    - Desde lirc importamos el método RawConnection
5. Módulo Sonido:
    - Importamos RPi.GPIO
    - Importamos time


## Configuración del software del mando:

- La configuración sera mediante la consola de comandos del nuestra Raspberry Pi 3.

    1.Instalar Lirc:
        - Abrimos nuestra terminal y vamos a introducir los siguentes comandos.
            - $ sudo apt-get update
            - $ sudo apt-get install licr
        - Si generase el error "Error al iniciar el soporte de la aplicación de entrada / salida remota IR flexible" ya que el sufijo .dist debe eliminarse de lirc_options.conf. Simplemente cambie el
          nombre del archivo como se muestra
            - $ sudo mv/etc/lirc/lirc_options.confi.dist/etc/lirc/lirc_options.conf    
        - Volvemos a instalar lirc ahora que el archivo lirc_options.conf ha cambiado de nombre
            - $ sudo apt-get install lirc
    
    2. Editamos Lirc_options.conf:
        - Edite /etc/lirc/lirc_options.conf de la siguiente manera cambiando estas dos líneas:
        - :
        - :
        - driver = default
        - device =/dev/lircO
        - :
        - :
    3.  Vamos a eliminar .dist Suffix de Lircd.conf.dist
        - Eliminamos suffix.dist form/etc/lirc/lircd.conf.dist
            - sudo mv/etc/lirc/lircd.conf.dist/etc/lirc/lirc.conf
 
    4. Editamos Config.txt:
        - Edite /boot/config.txt agregando una línea en la sección del módulo lirc-rpi de la siguiente manera. Este ejemplo asume que el RPi está 'escuchando' en el Pin 17 de BCM para el receptor IR, pero se puede
          usar cualquier pin RPI IO, pero si desea enviar comandos desde el RPi, agregue y descomente la cuarta línea que se muestra a continuación para enviar comandos IR en el pin 18 de BCM
            - :
            - :
            - dtoverlay=lirc-rpi
            - dtoverlay=gpio-ir,gpio_pin=17
            - dtoverlay=gpio-ir-tx, gpio_pin=18
            - :
            - :

    5. Comprobamos estado y hacemos Reboot:
        - Pare, inicie y verifique el estado de lircd para asegurarse de que no haya errores
            - $ sudo systemctl stop lircd.service
            - $ sudo systemctl start lircd.service
            - $ sudo systemctl status lircd.service
        - Reboot
            - $ sudo reboot

    6. Probamos Mando:
        - En este paso se asume que tiene un receptor IR conectado a su RPi en el pin especificado en el archivo config.txt.
        - Detenga el servicio LIRCD y pruebe el control remoto con el comando mode2
            - sudo systemctl stop lircd.service
            - sudo mode2 -d/dev/lircO
        - Apunte el control remoto al receptor y presione algunos botones. Debería ver algo como esto:
            - :
            - :
            - space 
            - pulse
            - :
            - :
        - Presionar Ctrl-C para salir
        - Su receptor IR está configurado y listo para continuar con la Parte 2 y acceder a él en Python.

    7. Ocultar Devinput.lircd.conf
        - Sus archivos de configuración remota se colocarán en el directorio /etc/lirc/lircd.conf.d. LIRC encontrará cualquier archivo en este directorio siempre que tenga una extensión .conf (es decir:JVC.lircd.conf)
        - No utilizaremos el archivo devinput.lircd.conf, por lo que lo ocultaremos cambiando la extensión de la siguiente manera cambiando el nombre de devinput.lircd.conf a devinput.lircd.conf.copy
            - sudo mv /etc/lirc/lircd.conf.d/devinput.lircd.conf /etc/lirc/lircd.conf.d/devinput.lircd.conf.copy

    8. Descargue el archivo .conf para su control remoto:
        - http://osoyoo.com/driver/pi3_start_learning_kit_lesson_19/lircd.conf

    
