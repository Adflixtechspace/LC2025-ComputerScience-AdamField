import serial
import codecs

ser = serial.Serial("COM12", 115200)

while True:
    serialValue = ser.readline() #reads line
    decodedSerialValue = codecs.decode(serialValue) #decodes line
    if (decodedSerialValue[0]) == "x" and (decodedSerialValue[1]) != "x": #runs if 0 = x // 0th 1st 2nd
        print(decodedSerialValue[1:])
    
#    else:
#        print("OOPS", decodedSerialValue)
ser.close()