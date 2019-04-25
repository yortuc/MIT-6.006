import math
import sys

# PEEK FINDING 
# One dimensional

# Naive approach θ(n)
def find_peak_naive(arr):
    for i in range(len(arr)):
        x = arr[i]
        left = arr[i-1] if i>0 else -sys.maxsize
        right = arr[i+1] if i<len(arr)-1 else -sys.maxsize

        if x >= left and x >= right:
            return x

# recursive binary search θ(logn)
def find_peak_binary_search(arr):
    h = math.floor(len(arr) / 2)
    x = arr[h]
    left = arr[h-1] if h>0 else -sys.maxsize
    right = arr[h+1] if h<len(arr)-1 else -sys.maxsize
    
    if x >= left and x >= right:
        return x
    elif x>= left: # take right
        par_arr = arr[h:]
    elif x>= right: # take left
        par_arr = arr[:h]

    return find_peak_binary_search(par_arr)
