name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    handle = open(name)
except Exception as e:
    print("File wasn't found")
    exit()

dictionary = dict()

for line in handle:
    line_list = line.split()
    if line_list.count("From"):
        dictionary[line_list[1]] = dictionary.get(line_list[1], 0) + 1

max_val = None
max_key = None
for key,value in dictionary.items():
    if max_val == None or max_val < value:
        max_val = value
        max_key = key

print(max_key,max_val)
