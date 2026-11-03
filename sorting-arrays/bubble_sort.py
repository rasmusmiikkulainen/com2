def bubble_sort(array):
    n = len(array)
    ordered = False
    while not ordered:
        ordered = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                ordered = False

arr = [7, 9, 11, 2]
bubble_sort(arr)
print(arr)
