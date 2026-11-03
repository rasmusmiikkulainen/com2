def selection_sort(array):
    n = len(array)
    for start in range(n):
        smallest = start

        for i in range(start + 1, n):
            if array[i] < array[smallest]:
                smallest = i

        array[start], array[smallest] = array[smallest], array[start]
        print(array)

def bubble_sort(array):
    n = len(array)
    ordered = False
    while not ordered:
        ordered = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                ordered = False
                print(array)

arr = [-4, 11, 7, -12, 6, 1]
arr2 = arr.copy()

print(arr)
selection_sort(arr)
print()

print(arr2)
bubble_sort(arr2)
