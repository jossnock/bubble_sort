def bubble_sort(list):
    sorted = False
    number_of_passes = 1
    while sorted == False:
        swapped = False
        for i in range(len(list) - number_of_passes):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                swapped = True
        if swapped == False:
            sorted = True
        number_of_passes += 1
    return list

import math

items = [6,5,math.inf,3,213,23,5667,3332222344,23,-math.inf,676,43,34234,54.04,math.inf,34.897,-343,-8342.324]

print(bubble_sort(items))