# 0x07. Rotate 2D Matrix

This repository contains a Python function to rotate a 2D matrix 90 degrees clockwise in-place. The function is designed to work with square matrices (n x n).

## Algorithm

The algorithm to rotate the matrix 90 degrees clockwise involves two main steps:

1. **Transpose the Matrix**: Convert the rows of the matrix into columns. This is done by swapping the elements across the diagonal.
2. **Reverse Each Row**: After transposing the matrix, reverse each row to achieve the 90-degree clockwise rotation.

### Step-by-Step Explanation

1. **Transpose the Matrix**:
   - Iterate through each element of the matrix.
   - For each element at position `(i, j)`, swap it with the element at position `(j, i)`.
   - This operation effectively converts rows to columns.

2. **Reverse Each Row**:
   - After transposing the matrix, iterate through each row.
   - Reverse the elements of each row to complete the rotation.

## Usage

To use the function, simply call `rotate_2d_matrix(matrix)` with your n x n matrix as the argument. The matrix will be rotated in-place, meaning no new matrix is created, and the original matrix is modified directly.

### Example

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

The output will be:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

### Testing
The provided main_0.py script can be used to test the function. Simply run the script to see the rotated matrix.

```
./main_0.py
```