name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle :
    line = line.strip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'From' :
        continue
    hrs = words[5].split(':')
    hours[hrs[0]] = hours.get(hrs[0] , 0) + 1
t = sorted([(k, v) for (k, v) in hours.items()])
for (x,y) in t:
    print(x, y)