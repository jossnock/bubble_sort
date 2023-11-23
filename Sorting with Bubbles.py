def bubble_sort(list,high_to_low = False):
    """Sorts a list of integers from smallest to largest.
    \n Add 'True' parameter after list to sort from largest to smallest."""
    sorted = False
    number_of_passes = 1
    if high_to_low == False:
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
    else: #if you want it sorted high to low, this branch triggers
        while sorted == False:
            swapped = False
            for i in range(len(list) - number_of_passes): #repeats for the number of swaps needed to complete a pass
                if list[i] < list[i + 1]: #if i < i+1, swap them
                    temp = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp
                    swapped = True
            if swapped == False: #tests nothing has never been swapped for the pass, 
                sorted = True
            number_of_passes += 1 #keeps track of number of passes to increase efficiency for the for loop
        return list

import math

items = [6,5,math.inf,3,213,23,5667,math.factorial(8),23,-math.inf,343,34234,math.sin(23),324978,54.04,math.inf,34.897,abs(-343),-8342.324,-23.22111211212]

print(bubble_sort(items))