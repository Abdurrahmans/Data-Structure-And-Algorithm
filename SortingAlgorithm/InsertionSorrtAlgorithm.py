inputArray = []
ElementCount = int(input("Enter number of element in array:"))
print("Enter {} number".format(ElementCount))

for x in range(ElementCount):
    value = int(input("Please inter the {} element of list:".format(x)))
    inputArray.append(value)
for i in range(ElementCount):
    x = inputArray[i]
    j = i-1
    while (j>=1 and inputArray[j]>x):
        inputArray[j+1] = inputArray[j]
        j -=1
    inputArray[j+1] = x
print("The Sorted List :", inputArray)