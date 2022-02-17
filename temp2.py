from smbus2 import SMBus 
from mlx90614 import MLX90614  
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
dat = []
pos=[]
i = 0
bus = SMBus(1)
while i < 10:
    sensor = MLX90614 (bus, address=0x5A)
    print("Temperatura Ambiente :", sensor.get_ambient())
    print("Temperatura objetivo :", sensor.get_object_1())
    sleep(.2)
    i += 1
    dat.append(sensor.get_object_1())
    print(i)
bus.close()

print(dat)
plt.xlabel('lecturas')
plt.ylabel('Temperatura (°C)')
text= "Lecturas totales{red}".format(red= i)
plt.text(i-1,dat[-1], text, fontsize=20, color='green')
plt.title('Lab DLS')
plt.plot(dat)
plt.savefig("EventPrueba.png",bbox_inches='tight')
plt.show()
