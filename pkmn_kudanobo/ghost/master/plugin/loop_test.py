from sys import argv

#argv[0] is the program name, don't want that.
lines = 0
f = open(argv[1])
for i in f:
    lines += 1
f.close()

print(lines,sep="")