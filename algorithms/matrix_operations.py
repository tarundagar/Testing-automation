"""
Matrix Operations Algorithms
Common matrix operations and algorithms
"""

def matrix_multiply(A, B):
    """
    Multiplies two matrices.
    Time Complexity: O(n^3) for n×n matrices
    
    Args:
        A: First matrix (list of lists)
        B: Second matrix (list of lists)
    
    Returns:
        Product matrix A × B
    """
    if not A or not B:
        return []
    
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions incompatible for multiplication")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def matrix_transpose(matrix):
    """
    Transposes a matrix.
    Time Complexity: O(n*m)
    
    Args:
        matrix: Input matrix (list of lists)
    
    Returns:
        Transposed matrix
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    
    return transposed


def matrix_add(A, B):
    """
    Adds two matrices.
    Time Complexity: O(n*m)
    
    Args:
        A: First matrix
        B: Second matrix
    
    Returns:
        Sum matrix A + B
    """
    if not A or not B:
        return []
    
    rows, cols = len(A), len(A[0])
    
    if rows != len(B) or cols != len(B[0]):
        raise ValueError("Matrices must have same dimensions")
    
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result


def matrix_scalar_multiply(matrix, scalar):
    """
    Multiplies a matrix by a scalar.
    
    Args:
        matrix: Input matrix
        scalar: Scalar value
    
    Returns:
        Matrix multiplied by scalar
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    result = [[matrix[i][j] * scalar for j in range(cols)] for i in range(rows)]
    return result


def identity_matrix(n):
    """
    Creates an n×n identity matrix.
    
    Args:
        n: Size of matrix
    
    Returns:
        n×n identity matrix
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matrix_power(matrix, n):
    """
    Raises a square matrix to power n using exponentiation by squaring.
    Time Complexity: O(k^3 * log n) where k is matrix size
    
    Args:
        matrix: Square matrix
        n: Power (non-negative integer)
    
    Returns:
        Matrix raised to power n
    """
    if n == 0:
        return identity_matrix(len(matrix))
    if n == 1:
        return [row[:] for row in matrix]  # Deep copy
    
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))


def print_matrix(matrix):
    """Helper function to print matrix in readable format."""
    for row in matrix:
        print("  ", row)


if __name__ == "__main__":
    # Test matrix operations
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print("Matrix A:")
    print_matrix(A)
    
    print("\nMatrix B:")
    print_matrix(B)
    
    print("\nA × B:")
    result = matrix_multiply(A, B)
    print_matrix(result)
    
    print("\nTranspose of A:")
    print_matrix(matrix_transpose(A))
    
    C = [[1, 2], [3, 4]]
    D = [[5, 6], [7, 8]]
    
    print("\nMatrix C:")
    print_matrix(C)
    print("\nMatrix D:")
    print_matrix(D)
    
    print("\nC + D:")
    print_matrix(matrix_add(C, D))
    
    print("\n2 × C:")
    print_matrix(matrix_scalar_multiply(C, 2))
    
    print("\n3×3 Identity Matrix:")
    print_matrix(identity_matrix(3))
