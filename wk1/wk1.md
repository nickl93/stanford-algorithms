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

## Asymptotic Analysis
- Vocabulary for the design and analysis of algorithms.
- Coarse enough to supress spurious detail, fine enough to be a useful measure.
- Suppress constant factors and lower-order terms.
    - Lower order terms irrelevant for large inputs.
    - Too system-dependent.
- E.g. equate 6nlog2n + 6n to nlogn.
    - Running time is O(nlogn)
    - "Big O" notation.
    - n = input size.
- E.g. Do arrays A, B have a number in common?
    - O(n^2)

## Big O Notation
- T(n) = function on integers.
- Big O of T(n) = O(T) = [usually] the worst case running time of T.
- i.e. the running time of T is bounded by some constant multiple of f(n), no matter the size of n.
- Formal Definition:
    - iff there exists constants c, n0 > 0, such that T(n) <= c.f(n) for all n >= n0.

### Example 1
- if T(n) = akn^k + ... + a1n + a0
- T(n) = O(n^k)
- Proof:
    - Let n0 = 1 and c = |ak| + |ak-1| + ... + |a1| + |a0|
    - Show All N >= 1, T(n) < c.n^k
    - We have, for every n >= 1,
    - T(n) <= |ak|n^k + ... + |a1|n + |a0|
    - |ak|n^k + ... + |a1|n^k + |a0| n^k (replace all n terms with n^k - will be larger).
    - = c*n^k

### Example 2
- Claim: for every k >= 1, n^k is not O(n^(k-1)).
- Proof: by contradiction.
    - Suppose n^k = O(n^(k-1))
    - Then there exist constants c, n0 > 0 such that n^k < c*n^(k-1) for all n >= n0.
    - Cancel n^(k-1) from both sides.
    - n <= c for all n > n0.
    - This is clearly false.

## Omega Notation
- Definition: T(n) = Omega(f(n)) iff there exists constants c, n0 such that T(n) >= c*f(n) for all n >= n0.
- Same concept as Big O, except we are finding a constant multiple that is always less than T(n).

## Theta Notation
- Definition: T(n) = Theta(f(n)) iff T(n) = O(f(n)) and T(n) = Omega(f(n)).
- There exists constants c1, c2, n0 such that c1*f(n) <= T(n) <= c2.F(n) for all n >= n0.
- "Actual" running time.
- We focus on Big O as upper bounds are more relevant.

## Little O Notation
- Strictly less quickly than n.
- Definition: T(n) = o(f(n)) iff for all constants c>0, there exists a constance n0 such that T(n) <= c*f(n) for all n > n0.

 
