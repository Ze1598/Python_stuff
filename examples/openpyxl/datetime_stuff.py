#Script to calculate the time needed to pay off a credit card debt, with given balance\
#interest rate and monthly payment

import datetime, calendar

def card_debt(debt, interest_rate, month_payment):
    # Variable to hold the initial debt; only to be used in the final return string
    initial_debt = debt
    # Convert the annual interest rate to a decimal
    interest_rate *= 0.01
    # Get the date for today (YYYY-MM-DD)
    current_date = datetime.date.today()
    # (first_week_day_month, month_length)[1] | (int ("Monday":0), int (28-31))
    days_in_current_month = calendar.monthrange(current_date.year, current_date.month)[1]
    # The number of days left in the current month is the difference between the number of days in the month and what day is today
    days_left_in_month = days_in_current_month - current_date.day
    #The debt will only be paid on the first day of each month, starting next month
    #This way, 'start_date' is equivalent to the first day of next month, specifically, the date for the first payment
    start_date = current_date + datetime.timedelta(days = days_left_in_month + 1)
    #Variable to hold the date for the monthly payments
    #Starts as 'start_date' because that's when the first payment is made
    pay_date = start_date

    #Each iteration of the loop represents a month
    while debt > 0:
        #Increment the debt by the monthly interest rate value
        debt += debt*(interest_rate/12)
        #To reduce problems with floats, after the monthly interest rate, round the debt to 2 decimal units
        debt = round(debt,2)
        #Pay the monthly payment, which means the debt will decrease
        debt -= month_payment
        #In case the debt is paid (in case the debt goes under zero), simply assign debt to zero to stop the loop
        if debt < 1:
            debt = 0
            continue
        #After the monthly operations, move to the next month
        days_left_in_month = calendar.monthrange(pay_date.year, pay_date.month)[1]
        #Because here we know we are working with the first day of each month, we can simply add to the current date the \
        #number of days of the current month to move to the next one
        pay_date = pay_date + datetime.timedelta(days=days_left_in_month)
    
    return f'A debt of {initial_debt}$ with an annual interest rate of {interest_rate//0.01}% with monthly payments of \
{month_payment}$ will be paid in {pay_date} if the payments start in {start_date}.'

if __name__ == "__main__":
    print(card_debt(10000, 13, 1000),'\n')
    print(card_debt(3500, 7, 300), '\n')
    print(card_debt(75000, 4, 800))