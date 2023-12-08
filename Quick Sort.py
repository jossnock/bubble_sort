def quick_sort(items):
    """Sorts a list of values from smallest to largest using recursion."""
    #Base Case:
    if len(items) <= 1:
        return items
    #Otherwise create smaller and larger sublists 
    #and recursively call quick_sort on those sublists and recombine the sorted lists with the pivot
    else:
        #Set pivot as first value and create empty smaller and larger lists
        pivot_value = items[0]
        smaller_sublist = []
        larger_sublist = []
        for i in range(1,len(items)):
            if items[i] < pivot_value:
                smaller_sublist.append(items[i])
            else:
                larger_sublist.append(items[i])
        return quick_sort(smaller_sublist) + [pivot_value] + quick_sort(larger_sublist)


#Asserts:
assert(quick_sort([9,5,5,1,2,1,2,2,6])==[1,1,2,2,2,5,5,6,9])
assert(quick_sort([5,7,12,324.7,245,-123,123.4])==[-123,5,7,12,123.4,245,324.7])