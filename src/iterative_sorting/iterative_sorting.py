# TO-DO: Complete the selection_sort() function below 
a = [3, 5, 8, 4, 2, 9, 6, 0, 1, 7]
 
# Understanding:
    # Need to sort the array from smallest to biggest numbers

#Plan:
# First part done: looping through the array from 0 to the length - 1 (or to the end of the array)
# Loop again or can we use the same loop:
    # Now we need to find the smallest number in arr and swap it with the number that is currently at index[0]...provided that it is not the smallest number.
    #Then find the next smallest and swap it to index[1]...swap and repeat

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        print(smallest_index) # outputs index
        for j in range(cur_index, len(arr) - 1):
            pass


        # TO-DO: swap




    return arr

selection_sort(a)


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr