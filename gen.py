import datetime
import os
date = datetime.date.today()
hour = datetime.time(1,2,3)
#variables
print(hour)
temp0 = 50
tempF = 24
#Rutina para crear reporte de condiciones iniciales y finales
#datos relevantes
for i in range (3):
    cont = """se detectó un evento a las {hora}
    con fecha de {hoy}.
    La temperatura inicial fue {T0}
    La temperatura final fue de {Tf}""".format(hora = hour, hoy = date,T0 = temp0, Tf = tempF)
    os.mkdir('/home/pi/Documents/Event_{hoy}'.format(hoy = date, num = i))
    new_rute = ('/home/pi/Documents/Event_{hoy}/evento{num}.txt'.format(hoy = date, num = i)) #Creación de archivo con fecha

    archivo = open(new_rute, 'w') #w de write
    archivo.write(cont) #escribe archivo

    archivo.close()
