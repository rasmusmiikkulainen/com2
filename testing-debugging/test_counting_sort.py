import pytest, counting_sort

# pytest way to list used parameters to test function
@pytest.mark.parametrize('list_in, expected', [
    ([5, 6, 1], [1, 5, 6]), # typical
    # [1000, 999,..., 1]
    (list(range(1000, 0, -1)), list(range(1, 1001))),
    ([], []), # empty
    ([0], [0]), # single element
    ([1, 2, 3], [1, 2, 3]), # already sorted
    ([1, 2, 1, 2], [1, 1, 2, 2]), # duplicates
    ([0, -10, 100], [-10, 0, 100])]) # neg, pos and zero values

def test_counting_sort(list_in, expected): # test function
    counting_sort.counting_sort(list_in) # note: sorts in-place
    assert list_in == expected # match against expected
