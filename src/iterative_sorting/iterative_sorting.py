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
        # print("beggining arr", arr) # --> used this to see what was happening with the list as code was added
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # print(smallest_index, arr,) # outputs array 9 times....going through each number but not doing anything ---> need another loop
        for j in range(cur_index, len(arr) - 1):
            # If the current value is smaller than the smallest_index update it
            if arr[j + 1] < arr[smallest_index]:
                # print(arr[j + 1], arr )
                smallest_index = j + 1
                # print("si in for loop",smallest_index, arr)

        # TO-DO: swap

        # Copy item at each index into a temp variable
        temp = arr[cur_index]
        # print("temp",temp, arr) # --> first output is 3, which will be swapped with 0, the next 5 with 1....
        
        # set cur_index value to smallest_index value
        arr[cur_index] = arr[smallest_index]
        # print("cur_index",arr[cur_index], arr) # outputs 0 as the smallest then next stops at 1, 2, 3..

        # # then copy temp into the right position
        arr[smallest_index] = temp
        # print("smallest_index",arr[smallest_index], arr) # --> see the change happen through each iteration


    # print("print the array",arr) --> final results
    return arr

print(selection_sort(a))


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr