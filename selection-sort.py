import random

def selection_sort(arr: list):
    """Selection Sort is a comparison based algorithm. 
    It sorts by selecting the smallest or largest element,
    and swapping it with the first unsorted element of an array,
    continuing this proccess until the whole array is sorted"""

    if type(arr) != list:
        return "The input must be a list, please try again!"

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

if __name__ == "__main__":
    test_dict = {"sorted_array": [1, 2, 3, 4, 5, 6, 7], # Expected Output: [1, 2, 3, 4, 5, 6, 7]
                 "reverse_sorted_array": [7, 6, 5, 4, 3, 2, 1], # Expected Output: [1, 2, 3, 4, 5,6, 7]
                 "unsorted_array": [3, 1, 4, 6, 7, 2, 5], # Expected Output: [1, 2, 3, 4, 5, 6, 7]
                 "duplicates_array": [4, 7, 2, 3, 7, 4], # Expected Output: [2, 3, 4, 4, 7, 7]
                 "negative_array": [3, -1, 7, -2, 0], # Expected Output: [-2, -1, 0, 3, 7]
                 "identical_array": [7, 7, 7, 7, 7], # Expected Output: [7, 7, 7, 7, 7]
                 "empty_array": [], # Expected Output: []
                 "single_element_array": [7] # Expected Output: [7]
                 #"large_random_array": random.sample(range(1, 1001), 100)  # 100 random elements between 1 and 1000
    }
    
    for test in test_dict.keys():
        print(test, selection_sort(test_dict[test]))