#read file name
file_name = input('Enter file name: ')

try:
    file = open(file_name)
except Exception as e:
    print("File can't be found!")
    exit()

#add to list
result = list()

for line in file:
    line_list = line.rstrip().split()
    for word in line_list:
        if word not in result:
            result.append(word)

#sort list
result.sort()

#print
print(result)
