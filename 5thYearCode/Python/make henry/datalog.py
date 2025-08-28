import serial
import codecs
import csv
f = open("henry.csv", "w",newline="")
writer = csv.writer(f)

while True:
    
        ser = serial.Serial("COM6",115200)
        serialValue = ser.readline()
        serialValue = int(codecs.decode(serialValue))
        writer.writerow([serialValue])
        ser.close()
        f.close()