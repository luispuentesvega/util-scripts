import os
import csv

with open(os.getcwd()+'/files/people.csv') as csvfile:
    row_csv = csv.reader(csvfile, delimiter=',')
    for row in row_csv:
        print(row)
"""
Output:
['name', 'age']
['Luis', '25']
['Maria', '25']
['Camila', '30']
['Peter', '23']
"""