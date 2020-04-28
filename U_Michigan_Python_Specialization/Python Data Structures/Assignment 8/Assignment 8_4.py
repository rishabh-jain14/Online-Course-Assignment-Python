fname = input("Enter file name: ")
fh = open(fname)
Lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in Lst:
            Lst.append(word)
        else :
            continue
Lst.sort()
print(Lst)