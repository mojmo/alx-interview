#!/usr/bin/python3

"""
This module contains a function to calculate the minimum number of operations
needed to get exactly n 'H' characters in a text file starting with a
single 'H'.
The allowed operations are "Copy All" and "Paste".
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in exactly
    n 'H' characters in the file starting with a single 'H'.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required, or 0 if n is impossible
    to achieve.
    """

    # If n is less than or equal to 1,
    # it's impossible to achieve more than one 'H'
    if n <= 1:
        return 0

    operations = 0
    factor = 2     # Start with the smallest prime factor

    # Factorize n by dividing it by its prime factors
    while n > 1:
        # While n is divisible by the current factor,
        # keep dividing and count operations
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1  # Move to the next potential factor

    return operations
