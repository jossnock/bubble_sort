def quick_sorter(items):
    










"""
FUNCTION quick_sort(items):
// Base case: stop when the partition contains a single item
IF items.length <= 1:
RETURN items
// Otherwise create smaller and larger sublists and recursively call
// quick_sort on those sublists and recombine the sorted lists with the pivot
ELSE:
//set pivot as first value and create empty smaller and larger lists
pivot_value = items[0]
smaller = []
larger = []
FOR i = 1 TO items.length:
if items[i] < pivot_value:
smaller.append(items[i])
else:
larger.append(items[i])
RETURN quick_sort(smaller) + [pivot_value] + quick_sort(larger)
END FUNCTION
"""