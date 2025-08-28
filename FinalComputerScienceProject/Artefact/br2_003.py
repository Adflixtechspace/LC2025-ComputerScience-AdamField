import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

def main():
    annuals = makeAnnualComps()
    print(annuals)
    #plotStatistics(annuals)
    plotStats(annuals)
    
#makes mean, mode, median for a particular year, returns a dictionary
def makeStats(year):
    data = pd.read_csv("clean_data_"+str(year)+".csv")
    totalSs, medianLoc, medianPts, depth, medianApprox = getMedian(data)
    meanPoints = getMean(data, totalSs)
    modalClass, modeApprox = getMode(data, depth)
    singleYearHist(data, year) #<- Generates histograms for each year
    print("in", year, "the modal class was", modalClass,  ", the mean was", meanPoints,
          "and the median student was in the", medianPts, "class")
    threeStats = ["Approx Mean", "Modal Class", "Approx Mode", "Median Class", "Approx Median", "year"] #This is a list
    return {threeStats[0]: meanPoints, threeStats[1]:modalClass, threeStats[2] : modeApprox,
            threeStats[3] : medianPts , threeStats[4] : medianApprox, threeStats[5]: year} # <- this is a dictionary, it uses the list threeStats

#finds the median by finding (bottom of col 3 + 1)/2, returns a tuple of useful data
def getMedian(data):
    depth = len(data["3"])-1
    totalSs = int(data["3"][depth])
    medianS =  (totalSs + 1)/2
    
    i = 0
    while int(data["3"][i]) < medianS:
        i = i + 1
       
    medianPts = data["0"][i]
    medianApprox = data["midinterval"][i]
    
    return (totalSs , medianS, medianPts, depth, medianApprox)  # <- this is a tuple

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
    return (data["0"][maxFreqLoc], data["midinterval"][maxFreqLoc])


    
#puts all annual stats into one dataFrame    
def makeAnnualComps():   
    statsDictionary = {}
    for year in range(2018, 2025):
        
        statsDictionary[year] = makeStats(year)
    statsDf = pd.DataFrame(statsDictionary).transpose()
    return statsDf


def plotStats(statsDF):
    #y_values = [10, 15, 13, 17, 14]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x =statsDF["year"], y=statsDF["Approx Mean"], name='Means'))
    fig.add_trace(go.Scatter(x =statsDF["year"], y=statsDF["Approx Median"], name='Medians'))
    fig.add_trace(go.Scatter(x =statsDF["year"], y=statsDF["Approx Mode"], name='Modes'))
    fig.update_layout(
        title='Line Graph of Annual Statistics',
        xaxis_title='Years',
        yaxis_title='CAO Points'
    )
    fig.show()
    plotHTMLcode = fig.to_html(full_html=False, include_plotlyjs="cdn")
    
    file = open("annStatTemp.txt", "w")
    file.write(plotHTMLcode)
    file.close()

#makes histograms for each year, and saves html code to a file called singleYr_XXXX.txt
def singleYearHist(data, year):
    data = data.drop(53)
    intervals = data["midinterval"]
    frequencies = data["1"]
    fig = go.Figure(data=[go.Bar(x=intervals, y=frequencies, width= 9)])
    fig.update_layout(
        title={'text': "CAO Points distribution: "+str(year), "x": 0.5, 'xanchor': 'center', "yanchor": "top"},                    
        xaxis_title='Points',
        yaxis_title='Frequency',
        template='plotly'
    )
    
    fig.add_annotation(text="Fig."+str(year - 2017),
    xref="paper", yref="paper",  
    x=0.01, y=1.1,              
    showarrow=False,            
    font=dict(size=14, color="black")  
    )
    fig.show()
    plotHTMLcode = fig.to_html(full_html=False, include_plotlyjs="cdn")
    
    file = open("singleYr_"+str(year)+".txt", "w")
    file.write(plotHTMLcode)
    file.close()
    

            

main()





    