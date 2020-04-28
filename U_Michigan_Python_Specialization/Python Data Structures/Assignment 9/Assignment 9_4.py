name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
bigvalue = 0
bigword = ''
for line in handle :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != 'From':
        continue
    count[words[1]] = count.get(words[1], 0) + 1
    if count[words[1]] > bigvalue :
            bigvalue = count[words[1]]
            bigword = words[1]
print(bigword, bigvalue)