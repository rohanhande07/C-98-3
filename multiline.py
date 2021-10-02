f = open("newfile.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)