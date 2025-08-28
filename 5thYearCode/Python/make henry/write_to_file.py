import csv

#opens file
f = open("henry.csv", "w",newline="")

#create the csv writer
writer = csv.writer(f)

#write rows to the csv file
writer.writerow([7])
#close the file
f.close()