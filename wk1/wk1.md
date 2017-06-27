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


 
