#!/usr/bin/python3

"""
Module for determining the winner of a prime number game between Maria and Ben.

The game involves selecting prime numbers from a set of consecutive integers
and removing those primes and their multiples until no more moves can be made.
Maria always starts the game. The player who cannot make a move loses.

The main function `isWinner` takes the number of rounds and an array of
integers representing the upper limit of the set of consecutive integers
for each round, and returns the name of the player who wins the most rounds,
or `None` if there is a tie.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime number game over multiple rounds.

    Args:
        x (int): The number of rounds.
        nums (list of int): An array where each element represents the upper
                        limit `n` of the set of consecutive integers for
                        each round.

    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben"),
             or `None` if there is no overall winner (a tie).
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Use Sieve of Eratosthenes to find all prime numbers up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1

    # Function to determine the winner of a single game
    def find_winner(n):
        """
        Determine the winner of a single round of the game.

        Args:
            n (int): The upper limit of the set of consecutive integers
            for the round.

        Returns:
            str: The name of the player who wins the round ("Maria" or "Ben").
        """
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        moves = 0  # Maria starts, so move count determines whose turn it is

        while primes:
            # Maria or Ben pick the smallest prime
            smallest_prime = primes.pop(0)
            # Remove the smallest_prime and its multiples from the list
            primes = [num for num in primes if num % smallest_prime != 0]
            moves += 1

        # If the move count is odd, Maria made the last move; if even, Ben did
        return "Maria" if moves % 2 != 0 else "Ben"

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = find_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
