hrs = float(input("Enter Hours : "))
rate = float(input("Enter Rate : "))
if hrs > 40 :
    pay = 40*rate + (hrs-40)*(rate*1.5)
else :
    pay = hrs*rate
print(pay)