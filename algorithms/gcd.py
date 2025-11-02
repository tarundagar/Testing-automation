"""
Greatest Common Divisor (GCD) and Least Common Multiple (LCM) Algorithms
"""

def gcd_euclidean(a, b):
    """
    Calculates GCD using Euclidean algorithm.
    Time Complexity: O(log(min(a, b)))
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a, b):
    """
    Calculates GCD using recursive Euclidean algorithm.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Greatest common divisor of a and b
    """
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def gcd_multiple(numbers):
    """
    Calculates GCD of multiple numbers.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Greatest common divisor of all numbers
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd_euclidean(result, num)
    
    return result


def lcm(a, b):
    """
    Calculates Least Common Multiple using GCD.
    LCM(a, b) = (a * b) / GCD(a, b)
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Least common multiple of a and b
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclidean(a, b)


def lcm_multiple(numbers):
    """
    Calculates LCM of multiple numbers.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Least common multiple of all numbers
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result


def extended_gcd(a, b):
    """
    Extended Euclidean algorithm.
    Finds GCD and coefficients x, y such that: a*x + b*y = gcd(a, b)
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Tuple (gcd, x, y)
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


def coprime(a, b):
    """
    Checks if two numbers are coprime (GCD = 1).
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        True if coprime, False otherwise
    """
    return gcd_euclidean(a, b) == 1


if __name__ == "__main__":
    # Test GCD and LCM algorithms
    a, b = 48, 18
    
    print(f"GCD of {a} and {b}:")
    print(f"  Euclidean: {gcd_euclidean(a, b)}")
    print(f"  Recursive: {gcd_recursive(a, b)}")
    
    print(f"\nLCM of {a} and {b}: {lcm(a, b)}")
    
    numbers = [12, 18, 24]
    print(f"\nGCD of {numbers}: {gcd_multiple(numbers)}")
    print(f"LCM of {numbers}: {lcm_multiple(numbers)}")
    
    print(f"\nExtended GCD of {a} and {b}:")
    gcd_val, x, y = extended_gcd(a, b)
    print(f"  GCD: {gcd_val}")
    print(f"  Coefficients: x={x}, y={y}")
    print(f"  Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")
    
    print(f"\nAre {a} and {b} coprime? {coprime(a, b)}")
    print(f"Are 15 and 28 coprime? {coprime(15, 28)}")
