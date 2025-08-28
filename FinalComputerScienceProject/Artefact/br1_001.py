import pandas as pd
import numpy

#makes the data clean for a single year
def cleanData(year):
    filePath = "data_"+str(year)+".csv"
    cleanFile = "clean_" + filePath
    data = getData(filePath)
    getIntervalMin(data)
    getIntervalMax(data)
    getMidInterval(data)
    makeCleanDataFile(data, cleanFile)

# imports the data as a dataFrame and initially removes some unwanted characters
def getData(filePath):

    data = pd.read_csv(filePath, header =None)
    data = data.replace({"Candidates scoring between ":"", " points":""}, regex=True)
    data = data.replace({"%":"", ",":""}, regex=True)
    return data

# picks out the first three characters from points range, and makes these the min values
def getIntervalMin(data):
    intervalMin = []
    for i in range(len(data[0])):
        intervalMin.append(int(data[0][i][:3]))
    
    data["intervalMin"] = intervalMin
    
# picks out the last three characters from points range, and makes these the max values
def getIntervalMax(data):
    intervalMin = []
    for i in range(len(data[0])):
        intervalMin.append(int(data[0][i][-3:]))
    
    data["intervalMax"] = intervalMin
    

# the midinterval value will be the median of the min and max, makes a new column for these
def getMidInterval(data):
    data["midinterval"] = (data["intervalMax"] + data["intervalMin"])//2

# saves the dataFrame now as a new .csv with the midinterval values.     
def makeCleanDataFile(data, filePath):
    data.to_csv( filePath, index = False)

for year in range(2018,2025):
    cleanData(year)