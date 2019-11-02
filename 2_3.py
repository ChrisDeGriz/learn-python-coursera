#ask hours from user
work_hours = input('Enter hours: ')

#ask rate from user
rate = input('Enter rate: ')

#calculate pay
pay = float(work_hours) * float(rate)

#output
print('Pay: ' + str(pay))
