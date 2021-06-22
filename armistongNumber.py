number = int(input("Enter the number:"))
sum = 0
temp = number
while temp!=0:
    lastDigit =temp%10
    sum +=(lastDigit*lastDigit*lastDigit)
    temp //=10

if sum==number:
    print("{} number is Armstrong number".format(number))
else:
    print("{} number is not Armstrong number".format(number))




