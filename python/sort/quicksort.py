from typing import List, Any

def partition(to_sort: List[Any], p: int, r: int):
    x = to_sort[r]
    i = p - 1
    for j in range(p, r):
        if to_sort[j] <= x:
            i += 1
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
    to_sort[i+1], to_sort[r] = to_sort[r], to_sort[i+1]
    return i+1


def initiate_quicksort(to_sort: List[Any], p: int, r:int):
    if p < r:
        q = partition(to_sort, p, r)
        initiate_quicksort(to_sort, p, q-1)
        initiate_quicksort(to_sort, q+1, r)


def sort(to_sort: List[Any]):
    initiate_quicksort(to_sort, 0, len(to_sort)-1)
