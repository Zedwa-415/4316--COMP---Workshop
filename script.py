#what is the relationship between diet quality and alcohol units drunk?
import csv
import sys
import matplotlib.pyplot as pl
import pandas as pd
print ("dada")

CardioData = pd.read_csv('cardiovascular_risk_dataset.csv')
CardioData.plot(kind= 'scatter',x = "Alcohol Units drunk", y = "data quality")
CardioData.show()