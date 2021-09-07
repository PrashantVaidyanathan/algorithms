from typing import List, Any

def parent(i: int):
    return i//2

def left(i: int):
    return (2*i) + 1

def right(i: int):
    return 2 * (1+ i)


def max_heapify(to_sort: List[Any], heap_size, i):
    l = left(i)
    r = right(i)
    largest = i
    if l <= heap_size and to_sort[l] > to_sort[largest]:
        largest = l
    if r <= heap_size and to_sort[r] > to_sort[largest]:
        largest = r
    if largest != i:
        to_sort[largest], to_sort[i] = to_sort[i], to_sort[largest]
        max_heapify(to_sort, heap_size, largest)

def build_max_heap(to_sort: List[Any]):
    arr_len = (len(to_sort) - 1)//2
    indices = range(0, arr_len + 1)
    for i in reversed(indices):
        max_heapify(to_sort, len(to_sort) - 1 , i)

def sort(to_sort: List[Any]):
    build_max_heap(to_sort)
    indices = range(1, len(to_sort))
    for i in reversed(indices):
        to_sort[0], to_sort[i] = to_sort[i], to_sort[0]
        max_heapify(to_sort, i-1, 0)