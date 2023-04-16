def interpolation_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high and lst[low] <= target <= lst[high]:
        pos = low + ((target - lst[low]) * (high - low)) // (lst[high] - lst[low])
        if lst[pos] == target:
            return pos
        elif lst[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
