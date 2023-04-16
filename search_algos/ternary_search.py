def ternary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if lst[mid1] == target:
            return mid1
        elif lst[mid2] == target:
            return mid2
        elif lst[mid1] > target:
            right = mid1 - 1
        elif lst[mid2] < target:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1
