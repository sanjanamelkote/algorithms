import random

def selection_sort(arr: list):
    """
    Selection Sort is a comparison based algorithm. 
    It sorts by selecting the smallest or largest element,
    and swapping it with the first unsorted element of an array,
    continuing this proccess until the whole array is sorted

    Time Complexity: O(n) -> we are going through the whole array once O(n) and calling min on the unsorted portion of the array O(n) -> O(2n) -> O(n)
    Space: O(n) because of the sorted array splicing
    
    """

    if type(arr) != list:
        raise ValueError("Input type must be a list.") 
    
    if not arr:
        return arr
    
    i = 0

    while i < len(arr):
        sorted = arr[i:]
        curr_min = min(sorted)
        curr_min_index = sorted.index(curr_min) + i
        temp = arr[i]
        arr[i] = curr_min
        arr[curr_min_index] = temp
        i += 1
    
    return arr