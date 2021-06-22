firstNumber = int(input("Enter the first number:"))
secondNumber = int(input("Enter the second number:"))
thirdNumber = int(input("Enter the third number:"))

if (firstNumber>secondNumber and firstNumber>thirdNumber):
    print("{} is the largest number".format(firstNumber))
elif(secondNumber>firstNumber and secondNumber>thirdNumber):
    print("{} is the largest number".format(secondNumber))
else:
    print("{} is the largest number".format(thirdNumber))

