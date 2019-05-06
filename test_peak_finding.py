from peak_finding import find_peak_naive, find_peak_binary_search

def test_find_peak_naive():
    arr = [1, 2, 3, 4, 5, 6, 4, 2]
    assert find_peak_naive(arr) == 6


def test_find_peak_binary_search():
    arr_one_element = [2]
    arr_peak_middle = [1, 2, 3, 4, 5, 6, 4, 2]
    arr_peak_end = [5, 6, 7, 8]
    arr_peak_start = [12, 5, 3]
    arr_peak_random = [37, 2, 46, 12, 12, 25, 42, 26, 33, 8, 16, 13, 41, 16, 29, 4, 1, 41, 31, 29, 5, 41, 13, 25, 46, 13, 39, 38, 34, 1, 30, 25, 33, 34, 36, 3, 28, 42, 3, 44, 18, 35, 32, 15, 33, 22, 8, 21, 23, 32]
    
    assert find_peak_binary_search(arr_one_element) == 2
    assert find_peak_binary_search(arr_peak_middle) == 6
    assert find_peak_binary_search(arr_peak_end) == 8
    assert find_peak_binary_search(arr_peak_start) == 12
    assert find_peak_binary_search(arr_peak_random) == 41
