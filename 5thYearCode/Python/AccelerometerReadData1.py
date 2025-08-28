import serial
import codecs

maxval = 6120
limitpercent = 0.9

while True:  
        ser = serial.Serial("COM14",115200)
        serialValue = ser.readline()
        try:
            serialValueInt = codecs.decode(serialValue)
            if int(serialValueInt) > maxval*limitpercent:
                print("Warning, Washing Machine is ready to blastoff, keep your distance")
        except:
            pass
#        print(serialValueInt)
        ser.close()