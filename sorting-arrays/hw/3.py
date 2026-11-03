def insertion_sort(array):
    n = len(array)
    for i in range(n):
        val = array[i]
        j = i - 1
        while j >= 0 and array[j] > val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = val

arr = [9, 7, 2, 11]
insertion_sort(arr)
print(arr)
