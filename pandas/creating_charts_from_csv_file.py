import os
import requests
import matplotlib.pyplot as plt
import pandas as pd

#1.Getting the csv file
url = 'https://tutorials.technology/data/world-population.csv'
response = requests.get(url)

#2.Creating csv file on local
with open(os.getcwd()+'/../files/world-population.csv', 'wb') as csv_file:
    csv_file.write(response.content)

#3.Printing the chart
population = pd.read_csv(os.getcwd()+'/../files/world-population.csv', index_col=0, encoding='utf8')
plot = population.plot(kind='line', title='World Population', lw=3, colormap='BuPu_r', marker='.', markersize=10)
plot.set_xlabel("Year")
plot.set_ylabel("Population")
plt.show()
