# TO-DO: Implement a recursive implementation of binary search
# this assumes it is sorted
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        current = ((start + end) // 2)
        if arr[current] == target:
            return current
        elif arr[current] < target:
            return binary_search(arr, target, (current - 1), end )
        else:
            return binary_search(arr, target, start, (current + 1))
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

