import datetime

def dayoftheWeek (day, month, year):
    #The names of each day of the week
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    #The names of each month
    months_list =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #The day of the week of the first day of each month in 2017
    months = {'1': 'Sunday',
        '2': 'Wednesday',
        '3': 'Wednesday',
        '4': 'Saturday',
        '5': 'Monday',
        '6': 'Thursday',
        '7': 'Saturday',
        '8': 'Tuesday',
        '9': 'Friday',
        '10': 'Sunday',
        '11': 'Wednesday',
        '12': 'Friday'
    }

#First week of a month
    if day <= 7:
#'day_index' is the sum between the index of the first day of 'month' in the 'week_days' list \
#with the difference between 'day' and 1
#in other words, 'day_index' verifies how many days are between the first day of the month and the current 'day'
        day_index = week_days.index(months[str(month)]) + (day-1) 
#then if 'day_index' is out of range in 'week_days', subtract 7 from it to make sure it will be in the 0-6 range needed
        if day_index > (len(week_days)-1):
            day_index -= 7
        # print(day_index)
        # print('Today is {}, {} {}th.'.format(week_days[day_index], months_list[month-1], day))
        return 'Today is {}, {} {}th, {}.'.format(week_days[day_index], months_list[month-1], day, year)
#Second week
    elif day <= 14:
        day_index = (week_days.index(months[str(month)]) + (day-1)) - 7
        if day_index > (len(week_days)-1):
            day_index -= 7
        # print(day_index)
        # print('Today is {}, {} {}th.'.format(week_days[day_index], months_list[month-1], day))
        return 'Today is {}, {} {}th, {}.'.format(week_days[day_index], months_list[month-1], day, year)
#Third week
    elif day <= 21:
        day_index = week_days.index(months[str(month)]) + (day-1) - 14
        if day_index > (len(week_days)-1):
            day_index -= 7
        # print(day_index)
        # print('Today is {}, {} {}th.'.format(week_days[day_index], months_list[month-1], day))
        return 'Today is {}, {} {}th, {}.'.format(week_days[day_index], months_list[month-1], day, year)
#Fourth week
    elif day <= 28:
        day_index = week_days.index(months[str(month)]) + (day-1) - 21
        if day_index > (len(week_days)-1):
            day_index -= 7
        # print(day_index)
        # print('Today is {}, {} {}th.'.format(week_days[day_index], months_list[month-1], day))
        return 'Today is {}, {} {}th, {}.'.format(week_days[day_index], months_list[month-1], day, year)
#Fifth week
    else:
        day_index = week_days.index(months[str(month)]) + (day-1) - 28
        if day_index > (len(week_days)-1):
            day_index -= 7
        # print(day_index)
        # print('Today is {}, {} {}th.'.format(week_days[day_index], months_list[month-1], day))
        return 'Today is {}, {} {}th, {}.'.format(week_days[day_index], months_list[month-1], day, year)


#Current day (1-31)
day = datetime.datetime.now().day
#Current month (1-12)
month = datetime.datetime.now().month
#Current year
year = datetime.datetime.now().year

print(dayoftheWeek(day, month, year))