# Week 1

## Merge Sort
- Divide & Conquer
- Base Case: <= 1 element
- Recursive Case: > 1 element
    - Split in half repeatedly until lists of 1 element.
    - Recursively re-merge in order by assessing left and right halves in order.
- Running time: n*log(n)

## Working out running time in recursive methods
- Use recursion tree
    - Furthest level from root node will be at level log2(n) <- zero-indexed, so log2(n)+1
    - Each level has 2^(level) subproblems each with an array of size n/2^(level)
    - Hence, number of operations on level = 2^(level number) * n/2^(level number)
    - Nature of binary tree means that the 2^(level number) cancels and no. of ops is independent of level number.
    - Total operation = sum (operations on level * number of levels)

## Guiding Principles of Algorithm Analysis
1. Use worst-case analysis: your running time bound should hold for every input size.
    - Others include: average-case, best-case, benchmarks.
2. Ignore constant factors and lower order terms.
    - Become negligible at high n values.
    - Constants depend on individual system architecture and other minutiae.
3. Use Asymptotic Analysis: focus on running time for large input sizes.
    - Conclusions may not be accurate for small input sizes.
    - If problem size is small anyway, excess time for algorithm is negligible anyway.
    - e.g. for small n, insertion sort running time < merge sort running time.

- N.B. Fast algorithm ~= worst-case running time that grows slowly with input size.
- Sweet Spot: balance of mathematical tractability and predictive power.
- Holy Grail: linear running time (or as close as possible).

 
