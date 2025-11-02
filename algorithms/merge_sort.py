"""
Merge Sort Algorithm
Time Complexity: O(n log n) in all cases
Space Complexity: O(n)
"""

def merge_sort(arr):
    """
    Sorts an array using merge sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    
    Args:
        left: Sorted list
        right: Sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    # Test the merge sort algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    sorted_array = merge_sort(test_array)
    print(f"Sorted array: {sorted_array}")
