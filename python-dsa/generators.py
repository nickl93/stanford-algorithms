import time
from typing import List


def odd_generator(n: int, m: int):
    while n < m:
        yield n
        n += 2

def odd_list(n: int, m: int) -> List[int]:
    odds = []
    while n < m:
        odds.append(n)
        n += 2
    return odds

t1 = time.time()
sum(odd_generator(1, 1000000))
print(f"Time to sum iterator: {time.time() - t1}")

t1 = time.time()
sum(odd_list(1, 1000000))
print(f"Time to sum list: {time.time() - t1}")

# A generator calculates the data only when required

t1 = time.time()
sum((x for x in range(1,1000000)))  # Generator expression syntax
print(f"Time to sum generator: {time.time() - t1}")
