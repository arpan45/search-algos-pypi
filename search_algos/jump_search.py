def jump_search(lst, target):
    n = len(lst)
    step = int(n ** 0.5)
    prev = 0
    while lst[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while lst[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if lst[prev] == target:
        return prev
    return -1
