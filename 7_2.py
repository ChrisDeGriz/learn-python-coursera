#ask for filename
file_name = input('Please enter name of file: ')

#try to open file
try:
    file = open(file_name, 'r')
except Exception as e:
    print('File is not found!')
    exit()

count = 0
sam_of_numbers = 0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos_of_column = line.find(':')
        number = float(line[pos_of_column + 1:].strip())
        sam_of_numbers = sam_of_numbers + number

print('Average spam confidence:',sam_of_numbers / count)
