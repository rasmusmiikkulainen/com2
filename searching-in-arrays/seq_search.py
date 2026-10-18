def seq_search(key, array):
    found = False
    for i in array:
        if key == i:
            found = True
            break
    return found

def seq_search2(key, array):
    index = 0
    found = False
    while not found and index < len(array):
        if array[index] == key:
            found = True
        else:
            index += 1
    return found

def time_search(algo, n, /, sort_data=False):
    import random, time

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

print(time_search(seq_search2, 10**6))
