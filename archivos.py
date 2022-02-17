from os import chdir


ruta = '/home/pi/Documents/python/Control-ext/extintor-control/texto.txt'
archivo = open(ruta, 'r') #r de read

#print(archivo.read())
print(archivo.readlines())

archivo.close()

cont = "pura palaberia, pana"
new_rute = '/home/pi/Documents/python/Control-ext/extintor-control/texto2.txt'
archivo = open(new_rute, 'r+') #w de write
archivo.write(cont) #escribe archivo
archivo.seek(4)
print(archivo.read())
archivo.close()




