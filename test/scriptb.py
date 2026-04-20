#what is the relationship between diet quality and alcohol units drunk?
import csv
import matplotlib.pyplot as plt

with open('cardiovascular_risk_dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    #obtaining alcohol units data from file
    AlcoholUnitsDrunk = []
    DietQuality = []
    for row in csv_reader:
        data = float(row[14])
        AlcoholUnitsDrunk.append(data)
        dat = float(row[13])
        DietQuality.append(dat)
    #AlcoholUnitsDrunk.sort()
    #DietQuality.sort()
    print (len(AlcoholUnitsDrunk), len(DietQuality))
    fig, ax = plt.subplots()
    plt.plot(AlcoholUnitsDrunk, DietQuality, 'go')
    plt.scatter(AlcoholUnitsDrunk, DietQuality, plotnonfinite=True, alpha=0.1)
    plt.xlabel("Alcohol Units drunk (au)")
    plt.ylabel("Diet Quality (1-10)")
    plt.show()
    #produces a curve suggesting as diet quality increases, alcohol units increase at an increasing rat