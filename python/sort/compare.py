from mergesort import sort as mergesort
from heapsort import sort as heapsort
from random import seed
from random import randint, random
import time

def timed_merge_sort(list_to_sort):
    start = time.time()
    mergesort(list_to_sort)
    end = time.time()
    return (end - start)

def timed_heap_sort(list_to_sort):
    start = time.time()
    heapsort(list_to_sort)
    end = time.time()
    return (end - start)

def timed_native_sort(list_to_sort):
    start = time.time()
    sorted_list = sorted(list_to_sort)
    end = time.time()
    return (sorted_list, (end - start))

n = 10000
seed(1)


def create_lists():
    list1 = [x for x in range(0, n)]
    list2 = [randint(0, 10000) for _ in range(n)]
    list3 = [random() for _ in range(n)]
    lists_to_sort = [list1, list2, list3]
    native_sorts = [timed_native_sort(A) for A in lists_to_sort]
    return (lists_to_sort, native_sorts)

lists_to_sort, native_sorts = create_lists()
merge_sort_list = [list(x) for x in lists_to_sort]



print("Merge Sort")
for i, list_to_sort in enumerate(merge_sort_list):
    sorted_list, native_elapsed = native_sorts[i]
    elapsed = timed_merge_sort(list_to_sort)
    assert sorted_list == list_to_sort
    print(f"List {i} sorted in {elapsed} seconds compared to {native_elapsed} seconds for native sort.")

print("--------------------------------------")
print("Heap Sort")
heap_sort_list = [list(x) for x in lists_to_sort]
for i, list_to_sort in enumerate(heap_sort_list):
    sorted_list, native_elapsed = native_sorts[i]
    elapsed = timed_heap_sort(list_to_sort)
    assert sorted_list == list_to_sort
    print(f"List {i} sorted in {elapsed} seconds compared to {native_elapsed} seconds for native sort.")
