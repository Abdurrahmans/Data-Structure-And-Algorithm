SecondNumber = CurrentNumber = 0
LastNumber=1
number = int(input("Enter a number tram of fibonacci Series:"))

for counter in range(0,number):
    if counter<2:
        CurrentNumber = counter
    else:
        CurrentNumber = SecondNumber+LastNumber
        SecondNumber = LastNumber
        LastNumber = CurrentNumber
    print("{}".format(CurrentNumber))




