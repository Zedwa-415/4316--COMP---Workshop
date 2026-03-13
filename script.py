#what is the relationship between diet quality and alcohol units drunk?
import csv
import matplotlib.pyplot as plt

with open('cardiovascular_risk_dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    #obtaining alcohol units data from file
    AlcoholUnitsDrunk = []
    for row in csv_reader:
        data = float(row[14])
        AlcoholUnitsDrunk.append(data)
    DietQuality = []
    for row in csv_reader:
        data = int(row[13])
        DietQuality.append(data)
    #graph time
    fig, ax = plt.subplots()
    ax.plot(AlcoholUnitsDrunk, DietQuality, ro)
    plt.show()


