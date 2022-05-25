# Bubble sort - poor performance on large data sets, most suited to small lists
#  time complexity = O(n^2), space complexity = O(1), Stable = Yes 
#  Note - stable meaning the order of elelements is preserved 

import math

def BubbleSort(new_list):
    """Function to perform bubble sort on a list"""
    assert type(new_list) == list, 'Must be of type list'
    for i in range(len(new_list)):
        for j in range(len(new_list)-1):
            if new_list[j] > new_list[j+1]:
                new_list[j+1], new_list[j] = new_list[j], new_list[j+1]
    return print(new_list)

    

# Selection Sort - best suited to small lists with numbers which are in random order. Poor performance on onn large data sets 
# Main advantage - no memory usage, easy to implement 
# time complexity = O(n^2), space complexity = O(1), Stable = No

def SelectionSort(new_List):
    '''Function to perform selection sort on a list'''
    #    find minimum element and swap with element, increment start of list by one making list n-1
    for i in range(len(new_List)):
        # create minimum index, set to i (position 0)
        min_index = i
        # create loop start from i+1, as we are comparing the first element to all elements past it in the list, until end of the list
        for j in range(i+1, len(new_List)):
            # compare each element to find minimum value of list 
            if new_List[min_index] > new_List[j]:
                min_index = j
        # once we have iterate through entire list and we have the minimum value in the list, we swamp it to the first postition in the list, this element is now sorted
        new_list[i], new_list[min_index] = new_List[min_index], new_List[i]
    # once nested loop has iterated through entire list, moving up once each time, i,n j+1,n, loop breaks and return list
    return print(new_List)


# Insertion Sort - divide array into two parts, select first element and place it into its position, complete until unsorted area is zero. 
# time complexity = O(n^2), space complexity = O(1), Stable = Yes 

def InsertionSort(new_list):
    '''Function to perform insertion sort on a list'''
    # loop through list starting from 1, as we compare cuurent index 0 with next, 1 
    for i in range(1, len(new_list)):
        # next element
        next_ele = new_list[i]
        # previous element
        prev_ele = i-1
        #  loop to compare current (previous) element with next element and put infront if smaller
        # this seems slightly unintuitive, but if the next element is less than the current element, swap it, otherwise, 
        while prev_ele >=0 and next_ele < new_list[prev_ele]: 
            # swap current element with next element 
            new_list[prev_ele+1] = new_list[prev_ele]
            # decrease prev by 1 
            prev_ele -= 1
        # keep looping through list
        new_list[prev_ele+1] = next_ele
    return new_list

    # (this code does work but it is not the most easy to follow, I will research to try and improve this)

# Bucket Sort - do not use when space complexity is a concern - use if input data is uniformley distrupted ie variation between data is uniformed, 1,3,5,7 uniform, 1,3,56,156 not uniform 

def BucketSort(new_list):
    '''Function to perform bucket sort'''
    # calculate number of buckets 
    numberOfBuckets = round(math.sqrt(len(new_list)))
    maxVal = max(new_list)
    arr = []

    # create buckets (nested lists)
    for i in range(numberOfBuckets):
        arr.append([])

    # sort buckets 
    for j in new_list:
        index_b = math.ceil(j*numberOfBuckets/maxVal)
        arr[index_b-1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = InsertionSort(arr[i])

    # merge buckets 
    k = 0 
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            new_list[k] = arr[i][j]
            k += 1 
    return print(new_list)


    # Merge Sort - this is a divide and conquer algorithm, divide array into halves and keep dividing recursively until they become too small, merge halves by sorting them 
    #  Use when - need stable sort, you want to sort to O(NlogN)
    #  Avoid - when space is an issue 

    # in order for use to create a merge sort function we need a merge function 
def merge(new_list, first_index, middle_index, last_index):
    first_sub_arr = middle_index - first_index +1
    second_sub_arr = last_index - middle_index 
    first = [0] * first_sub_arr
    second = [0] * second_sub_arr

    for i in range(first_sub_arr):
        first[i] = new_list[first_index+i]

    for j in range(second_sub_arr):
        second[j] = new_list[middle_index+1+j]

    i = 0
    j = 0 
    k = first_index
    while i < first_sub_arr and j < second_sub_arr:
        if first[i] <= second[j]:
            new_list[k] = first[i]
            i+=1
        else:
            new_list[k] = second[j]
            j+=1
        k+=1 
    while i < first_sub_arr:
        new_list[k] = first[i]
        i+=1
        k+=1 
    while j < second_sub_arr:
        new_list[k] = second[j]
        j+=1
        k+=1

def mergeSort(new_list, first_index, last_index):
    if first_index < last_index:
        middle_index = (first_index+(last_index -1))//2
        mergeSort(new_list, first_index, middle_index)
        mergeSort(new_list, middle_index +1, last_index)
        merge(new_list, first_index, middle_index, last_index)
    return new_list

# Quick sort - is a divide and conquer algorithm, partition list into two halves, use pivot number in each arrau and put lower numbers to left of pivot and higher number to the right, 
# repeat until array is sortted for both havles unlike merge sort space is not a concern. 

def partition(new_list, first_index, last_index):
    i = first_index - 1
    pivot = new_list[last_index]
    for j in range(first_index, last_index):
        if new_list[j] <= pivot:
            i += 1 
            new_list[i], new_list[j] = new_list[j], new_list[i]

    new_list[i+1], new_list[last_index] = new_list[last_index], new_list[i+1]
    return (i+1)

def quickSort(new_list, first_index, last_index):
    if first_index < last_index:
        pi = partition(new_list, first_index, last_index)
        quickSort(new_list, first_index, pi-1)
        quickSort(new_list, pi+1, last_index)
    return new_list



if __name__ == '__main__':

    new_list = [6,2,7,12,65,223,8999,12,3]

    print(quickSort(new_list, 0, 8))






