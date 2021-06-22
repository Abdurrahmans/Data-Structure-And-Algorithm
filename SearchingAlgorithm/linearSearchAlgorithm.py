inputArray = []
n = int(input("Enter number of element in Array:"))
print('Enter {} Number'.format(n))
for x in range(n):
    value = int(input())
    inputArray.append(value)
num = int(input('Enter a Number to search in Array:'))
found = False
for x in range(n):
    if inputArray[x]==num:
        found = True
        print("Number {0} found at index {1}".format(num,x))
        break
if not found:
    print('Number {} Not Present in Input Array'.format(num))