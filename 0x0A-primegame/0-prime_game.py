#!/usr/bin/python3

"""
Module for determining the winner of a prime number game between Maria and Ben.

The game involves selecting prime numbers from a set of consecutive integers
and removing those primes and their multiples until no more moves can be made.
Maria always starts the game. The player who cannot make a move loses.

The main function `isWinner` takes the number of rounds and an array of
integers representing the upper limit of the set of consecutive integers
for each round, and returns the name of the player who wins the most
rounds, or `None` if there is a tie.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime number game over multiple rounds.

    Args:
        x (int): The number of rounds.
        nums (list of int): An array where each element represents the upper
                    limit `n` of the set of consecutive integers for each round

    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben"),
             or `None` if there is no overall winner (a tie).
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Use Sieve of Eratosthenes to precompute prime numbers up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    maria_wins, ben_wins = 0, 0
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
