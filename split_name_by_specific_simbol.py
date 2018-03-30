import re

x = '201802_02_01_db'
words = re.split('_', x)
doclist = []
for word in words:
    doclist.append(word)
print(doclist)
#Output: ['201802', '02', '01', 'db']