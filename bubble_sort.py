def bubble_sort(arr:list):
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
    adjacent elements if they are in the wrong order until the whole list is sorted (ascending).

    Time Complexity: O(n^2)
    Space: O(n)
    """
    if type(arr) != list:
        raise ValueError("Input type must be a list.") 
    
    if not arr:
        return arr

    end = len(arr) - 1

    for n in range(len(arr)):
        start = 0
        next = start + 1
        while start < end:
            if arr[start] > arr[next]:
                arr[start], arr[next] = arr[next], arr[start]
            start += 1
            next += 1
        end -= 1
    
    return arr