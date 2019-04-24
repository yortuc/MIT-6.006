from peak_finding import find_peak_naive

def test_find_peak_naive():
    arr = [1, 2, 3, 4, 5, 6, 4, 2]
    assert find_peak_naive(arr) == 5 # position