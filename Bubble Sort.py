def bubble_sort(list):
    """Sorts a list of numbers from smallest to largest."""
    sorted = False
    number_of_passes = 1
    while sorted == False:
        swapped = False
        for i in range(len(list) - number_of_passes): #repeats for the number of swaps needed to complete a pass
            if list[i] > list[i + 1]: #if i > i+1, swap them
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                swapped = True
        if swapped == False: #tests nothing has never been swapped for the pass, 
            sorted = True
        number_of_passes += 1 #keeps track of number of passes to increase efficiency for the for loop
    return list

import math


#Asserts:
assert(bubble_sort([9,5,5,1,2,1,2,2,6])==[1,1,2,2,2,5,5,6,9])
assert(bubble_sort([5,7,12,324.7,245,-123,123.4])==[-123,5,7,12,123.4,245,324.7])