#what is the relationship between diet quality and alcohol units drunk?
import csv
import sys
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
CardioData = pd.read_csv('cardiovascular_risk_dataset.csv')
#Comparison = sns.load_dataset('cardiovascular_risk_dataset.csv')
#ax = sns.regplot(data=Comparison, x="diet_quality_score", y="alcohol_units_per_week")
CardioData.plot(kind = 'scatter', x = "diet_quality_score", y = "alcohol_units_per_week")
#CardioData['logy']= np.log10(CardioData['alcohol_units_per_week'])
#pl.plot("diet_quality_score", "diet_quality_score")
#lines = CardioData.plot.line(x = "diet_quality_score", y = "alcohol_units_per_week",)
pl.show()