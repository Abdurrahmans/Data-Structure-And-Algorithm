list = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5]
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)