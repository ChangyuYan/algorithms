A = [12, 32, 1, 23, 45, 2, 6, 3, 453, 19]

def selection_sort(my_list): 
    
    total = len(my_list)

    # Traverse through all array elements
    for i in range(total):

        # Find the minimum element in remaining unsorted array
        minloc = i
        for j in range(i+1, total):
            if my_list[minloc] > my_list[j]:
                minloc = j 
        # Swap the found minimum element with the first element 
        my_list[i], my_list[minloc] = my_list[minloc], my_list[i] 

    return my_list

def bubble_sort(my_list): 

    # Repeatedly swap the adjacent elements if they are in wrong order

    total = len(my_list)

    
    # Traverse through all array elements 
    for i in range(total):

        # Last i elements are already in place
        for j in range(n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if my_list[
