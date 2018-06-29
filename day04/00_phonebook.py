import sys
def read_file(filename):
    file = open(filename, "r")
    d = {}
    for line in file:
        line = line.split(",")
        key = line[0]
        try:
            value = line[1].rstrip("/n")
        except:
            print("Error in line: ", line)
            sys.exit();
        d.setdefault(key, [])
        d[key].append(value)
    return d

def readfile(file_name):
    file = open(file_name, "r")
    i = {}
    for line in file:
        line = line.split(",")
        key = line[1].rstrip("/n")
        value = line[0]
        i.setdefault(key, [])
        i[key].append(value)
    return i
print("")
print("")
print("")
print("** Shared First Names **")
d = read_file("names.txt")
for key, value in d.items():
    lent = len(value)
    if len(value) > 1:
        value = str(value)
        print(key, "(", lent , "):", value.replace(" \ " , "" ))
print("")
print("")
print("")
print("")
print("** Shared Last Names **")
i = readfile("names.txt")
for key, value in i.items():
    lent = len(value)
    if len(value) > 1:
        value = str(value)
        print(key, "(", lent , "):", value.replace(" \ " , "" ))
