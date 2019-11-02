#ask for work_hours
work_hours = float(input('Enter hours: '))

#ask for rate per hour
rate = float(input('Enter rate: '))

#calculate Pay
work_hours_limit = 40

if work_hours <= work_hours_limit:
    pay = work_hours * rate
else:
    pay = work_hours_limit * rate + (work_hours - work_hours_limit) * rate * 1.5

#output
print(pay)
