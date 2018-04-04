import datetime
date_format = "%Y%m%d"
a = datetime.datetime.strptime('20180403', date_format)
b = datetime.datetime.strptime(datetime.datetime.now().strftime ("%Y%m%d"), date_format)
delta = b - a
print(delta.days)
#Output: 39