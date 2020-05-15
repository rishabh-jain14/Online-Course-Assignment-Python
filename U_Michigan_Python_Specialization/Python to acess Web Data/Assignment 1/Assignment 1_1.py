import re
fh = open('regex_sum_464832.txt')
sum = 0
for line in fh:
    lst = re.findall("[0-9]+", line)
    if len(lst) < 1 : continue
    for y in lst:
        sum += int(y)
print(sum)

#OR
#print(sum([int(x) in re.findall("[0-9]+", line) for line in open("regex_sum_464832.txt"),read()]})