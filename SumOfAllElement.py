inputArray = []
n = int(input("Enter number of element in Array:"))
print('Enter {} Number'.format(n))
for x in range(n):
    value = int(input())
    inputArray.append(value)

sum = 0
for i in range(n):
    sum += inputArray[i]
print('Sum of all numbers are: {}'.format(sum))
