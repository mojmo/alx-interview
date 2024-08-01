#!/usr/bin/python3

"""Determine the fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of integers representing the coin denominations.
    total (int): The total amount to make using the coins.

    Returns:
    int: The minimum number of coins needed to make the total. If the total
         cannot be met by any number of coins, returns -1.
         If total is 0 or less, returns 0.
    """

    if total <= 0:
        return 0

    # Initialize the dp array with total + 1,
    # which is an impossible high value.
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0.

    # Fill the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still total + 1,
    # it means we cannot make up the total with given coins.
    return dp[total] if dp[total] != total + 1 else -1
