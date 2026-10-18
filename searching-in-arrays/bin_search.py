def bin_search(key, array):
    x = 0
    start = 0
    end = len(array) - 1
    while end >= start:
        x += 1
        mid = (start + end) // 2
        if key > array[mid]:
            start = mid + 1
        elif key < array[mid]:
            end = mid - 1
        else:
            return (True, x, mid)
    return (False, x, -1)

print(bin_search(10**4, [i for i in range(1, 10**4 + 1)]))
