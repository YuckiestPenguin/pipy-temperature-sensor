import os
from datetime import datetime


def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(device_id):
    location = '/sys/bus/w1/devices/' + device_id + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop(device_id):
    while True:
        if read(device_id) != None:
            print "\n"
            print datetime.now().strftime('%A %m-%d-%Y %H:%M:%S')
            print "Current temperature : %0.3f F" % read(device_id)[1]

def kill():
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()

