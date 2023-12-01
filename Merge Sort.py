def merge(list_a, list_b):
    """Merges two lists (in ascending order) and returns the merged list (in ascending order)."""
    merged_list = []
    a = 0
    b = 0
    while len(merged_list) < (len(list_a) + len(list_a)): 
    #while total length of other lists < length of merged_list
        if list_a[a] < list_b[b]:
            merged_list.append(list_a[a])
            a += 1
        else:
            merged_list.append(list_a[b])
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




