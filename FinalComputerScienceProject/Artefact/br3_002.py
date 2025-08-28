import pandas as pd
import plotly.graph_objects as go



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


    #fig.show()
    
    plotHTMLcode = fig.to_html(full_html=False, include_plotlyjs="cdn")
    
    file = open("singleYr_"+str(year)+".txt", "w")
    file.write(plotHTMLcode)
    file.close()
    
def allYearHists():
    for year in range(2018,2025):
        data = pd.read_csv("clean_data_"+str(year)+".csv")
        singleYearHist(data, year)
        
    
allYearHists()
