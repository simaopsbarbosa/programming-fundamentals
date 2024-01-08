def bubble_sort(alist): # sorts lists
    swapped = False # flag
    for i in range(len(alist) - 1):
        if alist[i] > alist[i+1]:
            # swap items
            alist[i], alist[i+1] = alist[i+1], alist[i]
            swapped = True
            
    if swapped == False: 
        return alist
    return bubble_sort(alist)