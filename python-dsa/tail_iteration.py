# Recursion is a special case of iteration known as tail iteration

def iteration_test(low: int, high: int) -> None:
    while low <= high:
        print(low)
        low = low + 1

def recursive_test(low: int, high: int) -> None:
    if low <= high:
        print(low)
        recursive_test(low + 1, high)
