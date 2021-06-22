def CountingSort(array, place):
    size = len(array)
    count = [0] * 10
    output = [0] * n

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


def RadixSort(array):
    place = 1
    k = max(arr)
    while k // place > 0:
        CountingSort(array, place)
        place *= 10


n = int(input("Enter how many element you want in the list: "))
arr = [int(input()) for i in range(n)]
RadixSort(arr)
print('After Sorting : {}'.format(arr))
