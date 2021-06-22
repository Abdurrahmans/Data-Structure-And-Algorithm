inputArray = []
ElementCount =int(input("Enter number of element in Array:"))
print("Enter {} number".format(ElementCount))
for x in range(ElementCount):
    value = int(input("Please inter the {} element of list:".format(x)))
    inputArray.append(value)

for i in range(ElementCount-1):
    for j in range(ElementCount-i-1):
         if (inputArray[j] > inputArray[j+1]):
            temp = inputArray[j]
            inputArray[j]=inputArray[j+1]
            inputArray[j+1]=temp

print("The Sorted List in Ascending order :",inputArray)