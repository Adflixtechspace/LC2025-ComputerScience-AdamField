import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    annuals = makeAnnualComps()
    #print(annuals.index())
    
#makes mean, mode, median for a particular year, returns a dictionary
def makeStats(year):
    data = pd.read_csv("clean_data_"+str(year)+".csv")
    totalSs, medianLoc, medianPts, depth = getMedian(data)
    meanPoints = getMean(data, totalSs)
    modalClass = getMode(data, depth)
    print("in", year, "the modal class was", modalClass,  ", the mean was", meanPoints,
          "and the median student was in the", medianPts, "class")
    threeStats = ["Approx Mean", "Modal Class", "Median"] #This is a list
    return {threeStats[0]: meanPoints, threeStats[1]:modalClass, threeStats[2] : medianPts} # <- this is a dictionary, it uses the list threeStats

#finds the median by finding (bottom of col 3 + 1)/2, returns a tuple of useful data
def getMedian(data):
    depth = len(data["3"])-1
    totalSs = int(data["3"][depth])
    medianS =  (totalSs + 1)/2
    
    i = 0
    while int(data["3"][i]) < medianS:
        i = i + 1
       
    medianPts = data["0"][i]
    
    return (totalSs , medianS, medianPts, depth)  # <- this is a tuple

#approximates the mean using mid interval values. (midIntVal * frequency)/(sum of frequencies)
def getMean(data, totalSs):
    data["rowContributes"] = data["1"] * data["midinterval"]
    sumOfColumn = data["rowContributes"].sum()
    meanPoints = round(sumOfColumn/totalSs, 2)
    return meanPoints

#finds the max of the frequencies, disregards the 0-99 points scheme
def getMode(data,depth):
    maxFreq = 0
    maxFreqLoc = 0
    for i in range(depth - 2):
        if data["1"][i] > maxFreq:
            maxFreq = data["1"][i]
            maxFreqLoc = i
    return data["0"][maxFreqLoc]
    
#puts all annal stats into one dataFrame    
def makeAnnualComps():   
    statsDictionary = {}
    for year in range(2018, 2025):
        statsDictionary[year] = makeStats(year)
    statsDf = pd.DataFrame(statsDictionary).transpose()
    return statsDf

main()



    