import serial

port="/dev/ttyACM0"


s1 = serial.Serial(port,115200)
s1.flushInput()

while (1):
    s1.inWaiting()>0
    BPM   =s1.readline()
    temp  = s1.readline()
    humi  = s1.readline()
    print(int(BPM), "\t",float(temp), "\t",float(humi))
