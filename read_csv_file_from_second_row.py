import os
import csv
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = []
sizes = []
with open(os.getcwd()+'/files/people.csv') as csvfile:
    next(csvfile)#Next Line
    row_csv = csv.reader(csvfile, delimiter=',')
    for row in row_csv:
        labels.append(row[0])
        sizes.append(float(row[1]))

print(labels)
#['Luis', 'Maria', 'Camila', 'Peter']