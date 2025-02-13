"""
escription:
After a hard quarter in the office you decide to get some rest on a vacation.
So you will book a flight for you and your girlfriend and
try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation.
The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days,
you get $50 off your total. Alternatively, if you rent the car for 3 or more days,
you get $20 off your total.

Write a code that gives out the total amount for different days(d).

Fundamentals
"""
#pseudo code:
# daily rental =  £40
# total = daily x £40
# >= 7 days = total-£50
# > 3 days = total- £20
# if statements

def rental_car_cost(d):
    daily = 40
    total_daily = d * daily
    if d >= 7:
        total_amt = total_daily - 50
    elif d > 3:
        total_amt = total_daily - 20
    elif d > 0:
        total_amt = total_daily
    return print(f" Total cost of {d} days rental: £{total_amt}")

rental_car_cost(9)


