
"""
# splitting --> split into single indices
[5 9 3 7 2 8 1 6]
[5 9 3 7] [2 8 1 6]
[5 9] [3 7] [2 8] [1 6]
[5] [9] [3] [7] [2] [8] [1] [6]



# merging 
[5] [9] [3] [7] [2] [8] [1] [6] --
[5 9] [3 7] [2 8] [1 6]
[3 5 7 9] [1 2 6 8]
[1 2 3 5 6 7 8 9]

"""

# TO-DO: complete the helper function below to merge 2 sorted arrays
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr4 = [0, 1, 2, 3, 4, 5]

def merge( arrA, arrB ): # --> sort and merge pieces together
    # print(arrA, arrB)

    # Total length of both arrays
    elements = len( arrA ) + len( arrB )
    print("elements", elements)
    
    # Creates a list of 0's based on the length of elements
    merged_arr = [0] * elements
    print("merged_arr",merged_arr) 


    # TO-DO --> for loop?
        

    
    return merged_arr

merge(arr1, arr4)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ): # --> Divide an array in to sub arrays
    # TO-DO

    #take a single array length and divide it in half:
    n = len(arr) # output --> length of array div. ny half
    # print("merge_sort n:", n, arr) 

    mid = n // 2 # output --> length of array div. ny half
    # print("merge_sort mid:",mid, arr)

    # if length of array is bigger than one, keep dividing
    if n > 1:
        # Get LHS and break it down until array is length of one -> recursion
        left = merge_sort(arr[:mid]) # --> slice to the left
        # print("merge_sort left:", left)

        # Get RHS and break it down until array is length of one -> recursion
        right = merge_sort(arr[mid:]) # --> slice to the right
        # print("merge_sort right:", right)

    #Then use merge() to sort and merge to on full array

    # print("merge_sort final",arr)
    return arr


merge_sort(arr1)

# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
