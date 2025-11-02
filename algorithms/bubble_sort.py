"""
Bubble Sort Algorithm
Time Complexity: O(n^2) in worst case, O(n) in best case
Space Complexity: O(1)
"""

def bubble_sort(arr):
    """
    Sorts an array using bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list in ascending order
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if element is greater than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping happened, array is sorted
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # Test the bubble sort algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    sorted_array = bubble_sort(test_array.copy())
    print(f"Sorted array: {sorted_array}")
