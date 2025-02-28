# Numeric Matrix Processor

## Description
This project is a command-line Python program that allows users to perform various matrix operations, including addition, scalar multiplication, matrix multiplication, transposition, determinant calculation, and matrix inversion. It provides an interactive interface for users to input matrices and choose operations dynamically.

## Features
- **Add Matrices**: Computes the sum of two matrices.
- **Multiply Matrix by a Constant**: Scales a matrix by a given scalar.
- **Multiply Matrices**: Computes the product of two matrices.
- **Transpose Matrix**: Offers multiple transposition options:
  - Main diagonal
  - Side diagonal
  - Vertical line
  - Horizontal line
- **Calculate Determinant**: Computes the determinant of a square matrix.
- **Inverse Matrix**: Computes the inverse of a square matrix (if it exists).
- **Exit**: Allows the user to exit the program.

## User Interaction
1. The program prompts the user to choose an operation from the following:
   ```
   1. Add matrices
   2. Multiply matrix by a constant
   3. Multiply matrices
   4. Transpose matrix
   5. Calculate a determinant
   6. Inverse matrix
   0. Exit
   ```
2. The user selects an operation by entering the corresponding number.
3. The program requests input for matrix dimensions and elements.
4. The result is displayed or an error message is shown if the operation cannot be performed.
5. The user is prompted to choose another operation or exit.

### Matrix Input Format
- The user first enters the matrix dimensions (rows and columns).
- Then, the user enters the matrix elements row by row, separated by spaces.
