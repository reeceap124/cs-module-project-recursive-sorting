# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    for x in range(elements):
        if i < len(arrA) and j < len(arrB):
            if arrA[i] <= arrB[j]:
                merged_arr[x] = arrA[i]
                i += 1
            else:
                merged_arr[x] = arrB[j]
                j += 1
        elif i >= len(arrA):
            merged_arr[x] = arrB[j]
            j += 1
        else:
            merged_arr[x] = arrA[i]
            i += 1
    


    return merged_arr



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid_index = len(arr) // 2
        left = merge_sort(arr[:mid_index])
        right = merge_sort(arr[mid_index:])
        return merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

