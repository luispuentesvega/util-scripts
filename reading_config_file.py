import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

print(config['ftp']['server'])
#Output: ftp.dlptest.com

print(config['people'][1]['name'])
#Output: Ana