from typing import List, Any


def sort(to_sort: List[Any]):
    if len(to_sort) > 1:
        mid = len(to_sort) // 2
        l = to_sort[:mid]
        r = to_sort[mid:]
        sort(l)
        sort(r)
        l_indx = r_indx = indx = 0
        while (l_indx < len(l) and r_indx < len(r)):
            if l[l_indx] < r[r_indx]:
                to_sort[indx] = l[l_indx]
                l_indx += 1
            else:
                to_sort[indx] = r[r_indx]
                r_indx += 1
            indx += 1 
        while(l_indx < len(l)):
            to_sort[indx] = l[l_indx]
            l_indx += 1
            indx += 1
        while(r_indx < len(r)):
            to_sort[indx] = r[r_indx]
            r_indx += 1
            indx += 1
