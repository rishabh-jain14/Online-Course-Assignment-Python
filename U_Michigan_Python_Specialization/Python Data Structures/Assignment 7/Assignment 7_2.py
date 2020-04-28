# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
L = []
f = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        L.append(float(line[line.rfind(' ')+1:]))
        f = f + L[len(L)-1]
print("Average spam confidence:" , f/len(L))