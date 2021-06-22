inputArray = []
ElementCount = int(input("Enter number of element in array:"))
print("Enter {} number".format(ElementCount))

for x in range(ElementCount):
    value = int(input("Please inter the {} element of list:".format(x)))
    inputArray.append(value)
for i in range(0, ElementCount):
    for j in range (i,ElementCount):
        if inputArray[i]>inputArray[j]:
            temp = inputArray[i]
            inputArray[i]=inputArray[j]
            inputArray[j]=temp
print("The Sorted List :", inputArray)