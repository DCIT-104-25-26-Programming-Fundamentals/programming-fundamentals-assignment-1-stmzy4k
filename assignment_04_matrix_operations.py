# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def transpose_matrix(matrix):
    result = []
    for col in range (len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for col in range(len(matrix_a[0])):
            new_row.append(matrix_a[row][col] + matrix_b[row][col])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for col in range(len(matrix_b[0])):
            total = 0
            for k in range(len(matrix_a[0])):
                total = total + matrix_a[row][k] * matrix_b[k][col]
            new_row.append(total)
        result.append(new_row)
    return result


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: Enter exactly {cols} numbers.")
            exit()
        matrix.append(row)
    return matrix
    

def print_matrix(matrix):
    for row in matrix:
        print(*row)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols)

print("Original Matrix:")
print_matrix(matrix)

transpose = transpose_matrix(matrix)
print("Transposed Matrix:")
print_matrix(transpose)

print("Enter second matrix:")
matrix_b = read_matrix(rows, cols)
sum_result = add_matrices(matrix, matrix_b)
print("Sum:")
print_matrix(sum_result)

rows_b = int(input("Enter number of rows of second matrix: "))
cols_b = int(input("Enter number of columns of second matrix: "))
if cols != rows_b:
    print("Error: Matrix multiplication not possible.")
    exit()
matrix_b = read_matrix(rows_b, cols_b)
product = multiply_matrices(matrix, matrix_b)
print("Product:")
print_matrix(product)