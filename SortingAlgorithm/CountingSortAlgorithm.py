def countingSort(arr,m):
    n = len(arr)
    arr1 = [0] * n

    x = [0] * (m + 1)

    for i in range(0, n):
        x[arr[i]] += 1

    for i in range(1, m + 1):
        x[i] += x[i - 1]

    i = n - 1
    while i >= 0:
        arr1[x[arr[i]] - 1] = arr[i]
        x[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = arr1[i]


n = int(input("Enter how many element you want in the list : "))
arr = [int(input()) for i in range(n)]
k = max(arr)
countingSort(arr, k)
print('After Sorting number: {}'.format(arr))

