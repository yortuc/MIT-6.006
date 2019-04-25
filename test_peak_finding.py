from peak_finding import find_peak_naive, find_peak_binary_search

def test_find_peak_naive():
    arr = [1, 2, 3, 4, 5, 6, 4, 2]
    assert find_peak_naive(arr) == 6


def test_find_peak_binary_search():
    arr_one_element = [2]
    arr_peak_middle = [1, 2, 3, 4, 5, 6, 4, 2]
    arr_peak_end = [5, 6, 7, 8]
    arr_peak_start = [12, 5, 3]
    
    assert find_peak_binary_search(arr_one_element) == 2
    assert find_peak_binary_search(arr_peak_middle) == 6
    assert find_peak_binary_search(arr_peak_end) == 8
    assert find_peak_binary_search(arr_peak_start) == 12
