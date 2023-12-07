def merge(list_a, list_b):
    """Merges two lists (in ascending order) and returns the merged list (in ascending order)."""
    merged_list = []
    a = 0
    b = 0
    while len(merged_list) < (len(list_a) + len(list_b)): 
    #while total length of other lists < length of merged_list
        if list_a[a] < list_b[b]:
            merged_list.append(list_a[a])
            a += 1
        else:
            merged_list.append(list_b[b])
            b += 1
        
        if a == len(list_a):
        #tests if the remainder of list_a is [], if so it merges and ends the loop
            for i in range(b,len(list_b)):
                merged_list.append(list_b[i])
            break
        if b == len(list_b):
        #tests if the remainder of list_b is [], if so it merges and ends the loop
            for i in range(a,len(list_a)):
                merged_list.append(list_a[i])
            break

    return merged_list

assert(merge([1,2],[1,4,7])==[1,1,2,4,7])


def merge_sort(items):
    # Base case a 1 item list is sorted so return it..
    if len(items) <= 1:
        return items
    # Otherwise split it two, merge sort the two and combine..
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


import math
unsorted_list = [9,5,5,1,2,1,2,2,6]
assert(merge_sort([9,5,5,1,2,1,2,2,6])==[1,1,2,2,2,5,5,6,9])
#IndexError: list index out of range