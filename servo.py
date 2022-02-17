import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm7 = GPIO.PWM(7, 50)

while True:
    cycl = float(input('ciclo de trabajo' ))#1.5 - 12.5
    pwm7.start(cycl) # Ciclo de trabajo2
                        
    
pwm7.stop()
GPIO.cleanup()