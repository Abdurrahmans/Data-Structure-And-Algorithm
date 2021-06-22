inputArray = []
n = int(input("Enter number of element in Array:"))
print('Enter {} Number'.format(n))
for x in range(n):
    value = int(input("Enter Sorted number:\n"))
    inputArray.append(value)
low = 0
high = len(inputArray)-1

num = int(input('Enter a Number to search in Array:'))
found = False
while low<= high:
    mid = (low+high)//2
    if inputArray[mid]==num:
        found = True
        print("Number {0} found at index {1}".format(num, mid))
        break
    else:
        if num < inputArray[mid]:
            high = mid - 1
        else:
            low = mid + 1
if not found:
    print('Number {} Not Present in Input Array'.format(num))