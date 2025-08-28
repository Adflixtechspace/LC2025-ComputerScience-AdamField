import serial
import codecs

maxval = 6120
limitpercent = 0.9
spin_cycles = [1400, 1200, 1000, 800, 600]
counter = 0
print(spin_cycles[counter])

while True:  
        ser = serial.Serial("COM14",115200)
        serialValue = ser.readline()
        try:
            serialValueInt = codecs.decode(serialValue)
            if int(serialValueInt) > maxval*limitpercent:
                print("Warning, Washing Machine is ready to blastoff, keep your distance")
                counter = counter + 1
                print(spin_cycles[counter])
            if counter > 4:
                counter = 4
                print(spin_cycles[counter])
        except:
            pass
#        print(serialValueInt)
        ser.close()