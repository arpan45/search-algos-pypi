from .binary_search import binary_search


def exponential_search(lst, target):
    n = len(lst)
    if lst[0] == target:
        return 0
    i = 1
    while i < n and lst[i] <= target:
        i = i * 2
    return binary_search(lst, target, i // 2, min(i, n - 1))
