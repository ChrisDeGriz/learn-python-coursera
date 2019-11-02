fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except Exception as e:
    print("File wasn't found!")
    exit()

count = 0

for line in fh:
    line_list = line.split()
    if line_list.count("From"):
        print(line_list[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
