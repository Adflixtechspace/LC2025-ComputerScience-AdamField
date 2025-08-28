import serial
import codecs

while True:  
        ser = serial.Serial("COM10",115200)
        serialValue = ser.readline()
        try:
            serialValueInt = codecs.decode(serialValue)
        except:
            pass
        
        print(serialValueInt)
        ser.close()