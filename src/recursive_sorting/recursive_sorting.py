
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

def merge( arrA, arrB ): # --> sort and merge pieces together?
    # print(arrA, arrB)
    elements = len( arrA ) + len( arrB )
    # print("elements", elements)

    merged_arr = [0] * elements
    # print("merged_arr",merged_arr) # --> Equals the same length of the 2 lists added together (concatinated), but filled with zero's. Placeholders?


    # What will my base case be?
    # TO-DO

    
    return merged_arr

# merge(arr1, arr4)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ): # --> Divide an array in to sub arrays
    # TO-DO

    #take a single array length and divide it in half:
    n = int(len(arr)) # output --> length of array div. ny half
    print("merge_sort n:", n) 

    mid = n // 2 # output --> length of array div. ny half

    print("merge_sort  mid:",mid) 

    # then divide multiple times until we have a length of one -> recursion
    # if length of array is bigger than one, keep dividing


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
