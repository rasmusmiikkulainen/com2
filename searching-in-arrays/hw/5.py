def read_words_from_url(url):
    import requests

    response = requests.get(url, stream=True)
    words = [line.decode("utf-8").strip() for line in response.iter_lines()]

    return words

wordlist_url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
words = read_words_from_url(wordlist_url)

# 1.
lastwords = words[-10:]
print(lastwords)

# 2.
def seq_search(key, array):
    for i in range(len(array)):
        if key == array[i]:
            return (True, i)
    return (False, -1)

key = "world"
print(seq_search(key, words))

# 3.
def bin_search(key, array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > array[mid]:
            start = mid + 1
        elif key < array[mid]:
            end = mid - 1
        else:
            return (True, mid)
    return (False, -1)
print(bin_search(key, words))

# 4.
# My binary search fails, since python thinks that the wordlist isn't sorted correctly
# Doing the following fixed it:
words.sort()

import time
keys = lastwords + ["definetly_not_a_word"]
print_output = False

for key in keys:
    print("\n" + key)
    for f in [seq_search, bin_search]:
        start = time.process_time_ns()
        output = f(key, words)
        end = time.process_time_ns()
        if print_output: print(output)
        print(f"{f.__name__} took {end-start} ns")