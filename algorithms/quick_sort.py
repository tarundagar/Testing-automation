"""
Quick Sort Algorithm
Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n) due to recursion stack
"""

def quick_sort(arr):
    """
    Sorts an array using quick sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low, high):
    """
    In-place quick sort implementation.
    
    Args:
        arr: List to sort
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition and get pivot index
        pi = partition(arr, low, high)
        
        # Sort elements before and after partition
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    """Helper function to partition array for in-place quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Test the quick sort algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    sorted_array = quick_sort(test_array.copy())
    print(f"Sorted array (functional): {sorted_array}")
    
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    quick_sort_inplace(test_array2, 0, len(test_array2) - 1)
    print(f"Sorted array (in-place): {test_array2}")
