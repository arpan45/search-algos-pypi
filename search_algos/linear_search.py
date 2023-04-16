def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1