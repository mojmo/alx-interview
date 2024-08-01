# 0x08. Making Change

## Problem Statement

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

## Solution

The solution uses dynamic programming to efficiently compute the minimum number of coins needed for any amount up to the given total.

1. Initialization:

    - Create a dp array where dp[i] holds the minimum number of coins needed to make the amount i.
    - Initialize the array with a value higher than any possible solution (total + 1), except dp[0] which is set to 0.

2. Filling the DP Table:

    - Iterate through each amount from 1 to total.
    - For each amount, iterate through the list of coins.
    - Update the dp value for the current amount by considering whether including this coin results in a fewer number of coins needed compared to the previously known minimum for that amount.

3. Result Extraction:

    - After filling the DP table, the value at dp[total] will represent the minimum number of coins needed to make the total.
    - If dp[total] is still set to the initial high value (total + 1), it means the total cannot be made up with the given coins, so return -1.

## Example

```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```
