def QuickSort(my_list):
    n = len(my_list)
    Rec_quicksort(my_list, 0, n - 1)
def Rec_quicksort(my_list, first, last):
    if first < last:
        pos = partition(my_list, first, last)
        Rec_quicksort(my_list, first, pos - 1)
        Rec_quicksort(my_list, pos + 1, last)
def partition(my_list, first, last):
    pivot = my_list[first]
    i = first
    j = last
    while i < j:
        while i <= j and my_list[i] <= pivot:
            i = i + 1
        while my_list[j] > pivot:
            j = j - 1
        if i < j:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

    temp = my_list[first]
    my_list[first] = my_list[j]
    my_list[j] = temp
    return j


n = int(input("Enter how many element you want in the list: "))
my_list = [int(input()) for i in range(n)]
QuickSort(my_list)
print('After Sorting : {}'.format(my_list))
