number = int(input("Enter a number:"))
ReversNumber = 0
temp = number

while temp!=0:
    RightDigit = temp%10
    ReversNumber=(ReversNumber*10) + RightDigit
    temp //=10
if ReversNumber==number:
    print(" {} is Polindrome number".format(number))
else:
    print(" {} is not Polindrome number".format(number))
