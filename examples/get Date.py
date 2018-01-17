import datetime, re
today = datetime.datetime.date(datetime.datetime.now()) 
split_today = re.split('-', str(today))
year = split_today[0]
months_list =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = months_list[int(split_today[1]) - 1]
day = split_today[2]
print(today)
print('Today is {} {}th of the year {}.'.format(month, day, year))