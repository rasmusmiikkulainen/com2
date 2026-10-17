# 2.
def bin_search(key, array):
    x = 0
    start = 0
    end = len(array) - 1
    while start <= end:
        x += 1
        mid = (start + end) // 2
        print(array[mid])
        if key > array[mid]:
            start = mid + 1
        elif key < array[mid]:
            end = mid
        else:
            return (True, x, mid)
    return (False, x, -1)

array = [-2, 9, 11, 12, 13, 14, 15, 22, 142]
print(bin_search(15, array))
