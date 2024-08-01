#!/usr/bin/python3

"""
This module provides a function `island_perimeter` that
calculates the perimeter of an island in a 2D grid.

An island is defined as a group of connected 1s surrounded
by water (0s).

The function assumes a rectangular grid where each cell can
be either 1 (land) or 0 (water).
"""


def island_perimeter(grid):
    """
    Calculates the total perimeter of an island in a 2D grid.

    Args:
        grid: A 2D list representing the grid with 1s for land
        and 0s for water.

    Returns:
        The total perimeter of the island, or 0 if no island is found.
    """

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Assume all sides contribute 4 units to perimeter
                perimeter += 4

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
