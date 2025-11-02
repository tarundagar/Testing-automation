"""
Fibonacci Sequence Algorithms
Different implementations with varying time complexities
"""

def fibonacci_recursive(n):
    """
    Calculates nth Fibonacci number using recursion.
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - due to call stack
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    Calculates nth Fibonacci number using memoization (top-down DP).
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary to store computed values
    
    Returns:
        nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_dp(n):
    """
    Calculates nth Fibonacci number using dynamic programming (bottom-up).
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Position in Fibonacci sequence
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n):
    """
    Calculates nth Fibonacci number with space optimization.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in Fibonacci sequence
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def fibonacci_sequence(n):
    """
    Generates first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
    
    Returns:
        List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


if __name__ == "__main__":
    n = 10
    
    print(f"Fibonacci number at position {n}:")
    print(f"  Recursive: {fibonacci_recursive(n)}")
    print(f"  Memoization: {fibonacci_memoization(n)}")
    print(f"  Dynamic Programming: {fibonacci_dp(n)}")
    print(f"  Optimized: {fibonacci_optimized(n)}")
    
    print(f"\nFirst {n} Fibonacci numbers:")
    print(f"  {fibonacci_sequence(n)}")
