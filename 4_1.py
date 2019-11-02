def computepay(hours, hrate, hlimit):
    if hours <= hlimit:
        return hours * hrate
    else:
        return hlimit * hrate + (hours - hlimit) * hrate * 1.5

#ask for work_hours
work_hours = input('Enter hours: ')
try:
    work_hours = float(work_hours)
except Exception as e:
    print('You entered wrong value!')
    exit()

#ask for rate per hour
rate = input('Enter rate: ')
try:
    rate = float(rate)
except Exception as e:
    print('You entered wrong value!')
    exit()

work_hours_limit = 40

#output
print(computepay(work_hours, rate, work_hours_limit))
