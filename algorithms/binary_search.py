"""
Binary Search Algorithm
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1


def binary_search_recursive(arr, target, left, right):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        left: Left boundary index
        right: Right boundary index
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    # Test the binary search algorithm
    test_array = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    
    print(f"Sorted array: {test_array}")
    print(f"Target: {target}")
    
    index = binary_search(test_array, target)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    
    # Test recursive version
    index_recursive = binary_search_recursive(test_array, target, 0, len(test_array) - 1)
    print(f"Recursive search result: {index_recursive}")
