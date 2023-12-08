def insertion_sort(items):
    for i in range(1,len(items)):
        current_item = items[i]
        j = i
        while j > 0 and items[j - 1] > current_item:
            items[j] = items[j - 1]
            j -= 1
        items[j] = current_item
    return items


#Asserts:
assert(insertion_sort([9,5,5,1,2,1,2,2,6])==[1,1,2,2,2,5,5,6,9])
assert(insertion_sort([5,7,12,324.7,245,-123,123.4])==[-123,5,7,12,123.4,245,324.7])