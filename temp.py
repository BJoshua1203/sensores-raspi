import board
import busio as io
import adafruit_mlx90614 as ada
from time import sleep

while 1:

    i2c = io.I2C(board.SCL, board.SDA, frequency = 100000)
    mlx = ada.MLX90614(i2c)

    aTemp = "{:.2f}".format(mlx.ambient_temperature)
    tTemp = "{:.2f}".format(mlx.object_temperature)
    sleep(1)
    print("Temperatura ambiente: ",aTemp, "°C")
    print("Temperatura del objetivo : ",tTemp, "°C")
