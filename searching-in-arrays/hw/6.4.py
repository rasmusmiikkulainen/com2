def interpolation_search(key, array):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        vlo = array[lo]
        vhi = array[hi]

        if not vlo <= key <= vhi:
            return (False, -1)
        if vlo == vhi:
            return (True, lo) if key == vlo else (False, -1)
        
        i = int(lo + (key - vlo) / (vhi - vlo) * (hi - lo))

        if key < array[i]:
            hi = i - 1
        elif key > array[i]:
            lo = i + 1
        else:
            return (True, i)

    return (False, -1)

array = [i for i in range(10**4)]
key = 9999
print(interpolation_search(key, array))