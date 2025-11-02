"""
Prime Number Algorithms
Various methods to work with prime numbers
"""

import math

def is_prime(n):
    """
    Checks if a number is prime.
    Time Complexity: O(sqrt(n))
    
    Args:
        n: Number to check
    
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers up to n using Sieve of Eratosthenes.
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    
    Args:
        n: Upper limit
    
    Returns:
        List of prime numbers up to n
    """
    if n < 2:
        return []
    
    # Create boolean array and initialize all as true
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    # Mark multiples of each prime as composite
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, n + 1, i):
                is_prime_arr[j] = False
    
    # Collect all prime numbers
    primes = [i for i in range(n + 1) if is_prime_arr[i]]
    return primes


def prime_factorization(n):
    """
    Finds prime factorization of a number.
    
    Args:
        n: Number to factorize
    
    Returns:
        List of prime factors
    """
    factors = []
    
    # Handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


def nth_prime(n):
    """
    Finds the nth prime number.
    
    Args:
        n: Position of prime number to find (1-indexed)
    
    Returns:
        The nth prime number
    """
    if n == 1:
        return 2
    
    count = 1
    candidate = 3
    
    while count < n:
        if is_prime(candidate):
            count += 1
        if count < n:
            candidate += 2
    
    return candidate


def primes_in_range(start, end):
    """
    Finds all prime numbers in a given range.
    
    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)
    
    Returns:
        List of prime numbers in range
    """
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    # Test prime number algorithms
    print("Is 17 prime?", is_prime(17))
    print("Is 20 prime?", is_prime(20))
    
    print("\nPrimes up to 50:")
    print(sieve_of_eratosthenes(50))
    
    print("\nPrime factorization of 60:")
    print(prime_factorization(60))
    
    print("\n10th prime number:")
    print(nth_prime(10))
    
    print("\nPrimes between 10 and 30:")
    print(primes_in_range(10, 30))
