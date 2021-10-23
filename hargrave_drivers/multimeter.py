from time import sleep
import time
import serial
from serial.tools import list_ports
from subprocess import Popen, PIPE
psu = serial.Serial('/dev/ttyUSB0',115200,timeout=1)
arduino = serial.Serial('/dev/ttyUSB1',115200,timeout=1)
sleep(3)
while True:
    psu.write("val1?\r\n")
    current = float(psu.readline())
    print(current)
    if(current < 200):
        arduino.write("1")
	sleep(2)
        arduino.write("0")
	sleep(3)
    else:
	arduino.write("0")
	sleep(2)

