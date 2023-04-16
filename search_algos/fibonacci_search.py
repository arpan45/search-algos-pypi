def fibonacci_search(lst, target):
    fib_m2, fib_m1 = 0, 1
    fib = fib_m2 + fib_m1
    while fib < len(lst):
        fib_m2, fib_m1 = fib_m1, fib
        fib = fib_m2 + fib_m1
    offset = -1
    while fib > 1:
        i = min(offset + fib_m2, len(lst) - 1)
        if lst[i] < target:
            fib, fib_m1 = fib_m1, fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        elif lst[i] > target:
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        else:
            return i
    if fib_m1 and lst[offset + 1] == target:
        return offset + 1
    return -1
