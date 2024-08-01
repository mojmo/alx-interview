# 0x09. Island Perimeter

## Problem Description:

Given a 2D grid where each cell can be either 1 (land) or 0 (water), the task is to calculate the total perimeter of the largest island. An island is a group of connected 1s surrounded by water (0s).


## Solution

This code implements the island_perimeter function to solve this problem. It works by iterating through each cell in the grid and checking if it's land (1). If it is, the function assumes the cell contributes 4 units to the perimeter (one for each side). However, this would overcount the perimeter because connected land doesn't contribute to both sides.

Therefore, the function then checks the adjacent cells (up, down, left, right). If the adjacent cell is also land (1), it means that side of the current cell doesn't contribute to the island's perimeter, so 1 unit is subtracted from the total perimeter. This ensures accurate perimeter calculation for all connected land cells.


## Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```
