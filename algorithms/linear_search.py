"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Searches for a target value in an array using linear search.
    
    Args:
        arr: List of elements
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Finds all occurrences of a target value in an array.
    
    Args:
        arr: List of elements
        target: Element to search for
    
    Returns:
        List of indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


if __name__ == "__main__":
    # Test the linear search algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 25]
    target = 25
    
    print(f"Array: {test_array}")
    print(f"Target: {target}")
    
    index = linear_search(test_array, target)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    
    # Find all occurrences
    all_indices = linear_search_all(test_array, target)
    print(f"All occurrences at indices: {all_indices}")
