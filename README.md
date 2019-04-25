# Lecture 1 

## Peak Finding 1 Dimensional

Given the array of numbers;

`[a, b, c, d, e, f, g, h, i]`

* Position 2 is a `peak` if and only if b >= a and b>=c.
* Position 9 is a `peak` if i>=h 

Find the peak if it exists. 

### 1. Straightforward algorithm

Traverse the array and find the peak.
* Worst case θ(n) linear complexity

Traversing an array with Python 
```
for i in range(len(arr)):
```

### 2. Binary search algorithm
a = [1, 2, ..., n/2-1, n/2, n/2+1, ..., n-1, n]
* Divide and conquer algorithm
* if  a[n/2-1] < a[n/2] > a[n/2 + 1]] n/2 is the peak point.
* if a[n/2] < a[n/2 - 1] take left side 
* if a[n/2] < a[n/2 + 1] take right side
* θ(logn) logarithmic complexity

Logarithmic complexity: With binary search, each step we divide the search space in two halves. In worst case, the item being searched will be found after k steps.

* n * (1/2)^k = 1
* n = 2^k
* k = log2n

In worst case, algorithm will take `log2n` steps. Since 2 is also constant, can be dropped and the final time complexity is `θ(logn)`.