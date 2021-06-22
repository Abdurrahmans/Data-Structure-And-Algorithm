number = int(input("Enter a number:"))
revers = 0
while number!=0:
    rightDigit = number%10
    revers =(revers*10) + rightDigit
    number = number // 10
print("Revesred number {}".format(revers))