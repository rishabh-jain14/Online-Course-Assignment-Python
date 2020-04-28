largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done" : break
    except:
        num = int(num)
        if smallest is None :
            smallest = num
    	if largest < num :
            largest = num
        elif smallest > num :
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)