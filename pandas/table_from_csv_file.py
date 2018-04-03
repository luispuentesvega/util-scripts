import pandas as pd

file = 'D://Luis/Programming/Python/util-scripts-py/files/people.csv'
data = pd.read_csv(file, encoding='utf-8')
#Printing Type
#print(type(data))
#Printing Data
data['age'].describe()
print(data)
#Print out three rows instead
#print(data.head(2))