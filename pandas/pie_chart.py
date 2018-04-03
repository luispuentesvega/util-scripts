import os
import csv
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

labels = []
sizes = []
with open(os.getcwd()+'/../files/people.csv') as csvfile:
    next(csvfile)
    row_csv = csv.reader(csvfile, delimiter=',')
    for row in row_csv:
        labels.append(row[0])
        sizes.append(float(row[1]))

#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#explode=explode,
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()