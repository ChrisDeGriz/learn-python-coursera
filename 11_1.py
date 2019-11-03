import re

file = input('Enter file name: ')

try:
    fh = open(file)
except Exception as e:
    print('File is not found!')
    exit()

sum_numbers = 0

#REGEX which finds any appearance of numbers in text

for line in fh:
    number_list = re.findall('[0-9]+', line)
    for number in number_list:
        sum_numbers = sum_numbers + int(number)

print(sum_numbers)
