"""
0/1 Knapsack Problem
Time Complexity: O(n * W) where n is number of items and W is capacity
Space Complexity: O(n * W)
"""

def knapsack_recursive(weights, values, capacity, n):
    """
    Solves 0/1 knapsack problem using recursion.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        n: Number of items to consider
    
    Returns:
        Maximum value that can be obtained
    """
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    # If weight of nth item is more than capacity, it cannot be included
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)
    
    # Return maximum of two cases:
    # 1. nth item included
    # 2. nth item not included
    include = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
    exclude = knapsack_recursive(weights, values, capacity, n - 1)
    
    return max(include, exclude)


def knapsack_dp(weights, values, capacity):
    """
    Solves 0/1 knapsack problem using dynamic programming.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
    
    Returns:
        Maximum value that can be obtained
    """
    n = len(weights)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item can be included
            if weights[i - 1] <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include current item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def knapsack_with_items(weights, values, capacity):
    """
    Solves 0/1 knapsack and returns selected items.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
    
    Returns:
        Tuple of (max_value, selected_items)
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    selected_items.reverse()
    return dp[n][capacity], selected_items


if __name__ == "__main__":
    # Test knapsack algorithms
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print("Knapsack Problem:")
    print(f"  Weights: {weights}")
    print(f"  Values: {values}")
    print(f"  Capacity: {capacity}")
    
    max_value_recursive = knapsack_recursive(weights, values, capacity, len(weights))
    print(f"\nMaximum value (recursive): {max_value_recursive}")
    
    max_value_dp = knapsack_dp(weights, values, capacity)
    print(f"Maximum value (DP): {max_value_dp}")
    
    max_value, selected = knapsack_with_items(weights, values, capacity)
    print(f"\nSelected items (indices): {selected}")
    print(f"Total weight: {sum(weights[i] for i in selected)}")
    print(f"Total value: {max_value}")
