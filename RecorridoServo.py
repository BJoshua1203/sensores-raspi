import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm7 = GPIO.PWM(7, 50)
x = 2
x = int(input("numero: "))

def adelante(x):
    cycl = x
    if cycl >= 2 :
        cycl += .1
        pwm7.start(cycl) # Ciclo de trabajo
    elif cycl == 12:

        pwm7.stop()
    print(cycl)
    time.sleep(.25)
    
adelante(x)

GPIO.cleanup()


