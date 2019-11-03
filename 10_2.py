name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    handle = open(name)
except Exception as e:
    print('File not found!')
    exit()

result_dict = dict()

for line in handle:
    split_line = line.split()
    if split_line.count('From'):
        time = split_line[5].split(':')
        result_dict[time[0]] = result_dict.get(time[0], 0) + 1

tpl = sorted(result_dict.items())

for k,v in tpl:
    print(k,v)
