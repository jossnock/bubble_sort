def quick_sorter(items):
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
        return quick_sorter(smaller_sublist) + [pivot_value] + quick_sorter(larger_sublist)

#Test:
import math
items = [6,5,math.inf,3,213,23,5667,math.factorial(8),23,-math.inf,343,34234,math.sin(23),324978,54.04,math.inf,34.897,abs(-343),-8342.324,-23.22111211212]
print(quick_sorter(items))