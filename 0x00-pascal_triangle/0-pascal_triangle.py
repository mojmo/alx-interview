#!/usr/bin/python3

"""
This script generates Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate (inclusive).
        Must be greater than 0.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """

    if n <= 0:
        return []

    # Initialize the triangle with the first row (always [1])
    result = [[1]]

    for i in range(1, n):
        # Create a new row starting with 1
        row = [1]

        # Calculate elements in the middle of the row
        for j in range(1, i):
            previous_row = result[i - 1]
            element = previous_row[j - 1] + previous_row[j]
            row.append(element)

        # Add the last element (always 1) to the row
        row.append(1)

        # Append the completed row to the triangle
        result.append(row)

    return result
