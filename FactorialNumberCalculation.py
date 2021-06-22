n = int(input("Enter a number for factorail number:"))
factorial = 1
for x in range(1 ,n+1):
    factorial = factorial*x
print("Factorial of {} is {}".format(n,factorial))