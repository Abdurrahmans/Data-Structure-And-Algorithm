import math
number=int(input("Enter any positive number:"))
sum = 0
sum = number*(number + 1)/2
print("The sum of series upto {0} = {1}".format(number,sum))

total = 0
total =(number*(number+1)*(2*number+1))/6
print("The sum of series upto {0} = {1}".format(number,total))

total =math.pow(number*(number+1)/2,2)
print("The sum of series upto {0} = {1}".format(number,total))