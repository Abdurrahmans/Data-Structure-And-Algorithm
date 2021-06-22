number = int(input("Enter a positive number:"))
isPrime = 0
for x in range(2,number):
    if number % x==0:
        isPrime = 1
        break
if isPrime==0:
    print("{} is a prime number".format(number))
else:
    print("{} is not a prime number".format(number))

