#ask for filename
file_name = input('Please enter name of file: ')

#try to open file
try:
    file = open(file_name, 'r')
except Exception as e:
    print('File is not found!')
    exit()

#print result in uppercase
for line in file:
    line = line.rstrip()
    print(line.upper())
