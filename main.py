#______________Import________________
import csv
import pandas as pd
import plotly.figure_factory as ff
#____________________________________

# Getting all the Data and reading it......
File_Object = pd.read_csv("BelloCurve1\Bell_CurveData\Mobile_Data.csv")

#Creating a List and stoaring in avg rate
Avg_Rating = File_Object["Avg Rating"].tolist()

fig = ff.create_distplot([Avg_Rating], ["Avg-Rating"],show_hist=False)
fig.show()