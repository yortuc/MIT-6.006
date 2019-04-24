# PEEK FINDING 
# One dimensional

# Naive approach θ(n)
def find_peak_naive(arr):
    for i in range(0, len(arr)):
        x = arr[i]
        left = arr[i-1]
        right = arr[i+1]

        if x >= left and x >= right:
            return i


