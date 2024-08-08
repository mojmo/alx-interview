# 0x0A. Prime Game

## Description

This module determines the winner of a prime number game played between Maria and Ben. The game involves selecting prime numbers from a set of consecutive integers and removing those primes and their multiples until no more moves can be made. Maria always starts the game. The player who cannot make a move loses.

The function `isWinner` takes the number of rounds and an array of integers representing the upper limit of the set of consecutive integers for each round. It returns the name of the player who wins the most rounds, or `None` if there is a tie.

## Problem Explanation

Maria and Ben play a game with the following rules:

1. They have a set of consecutive integers starting from 1 up to and including `n`.
2. Players take turns choosing a prime number from the set.
3. When a player chooses a prime number, that number and all of its multiples are removed from the set.
4. The player who cannot make a move loses.

They play `x` rounds of the game, where `n` may be different for each round. Maria always goes first and both players play optimally. The task is to determine who wins the most rounds.

## Example

### Input

```python
x = 3
nums = [4, 5, 1]
print(isWinner(3, [4, 5, 1]))
```

### Output

```python
"Ben"
```

### Explanation


1. **Round 1** (n = 4):

Maria picks 2: remaining set {1, 3}.
Ben picks 3: remaining set {1}.
Ben wins as there are no primes left for Maria.

2. **Round 2** (n = 5):

Maria picks 2: remaining set {1, 3, 5}.
Ben picks 3: remaining set {1, 5}.
Maria picks 5: remaining set {1}.
Maria wins as there are no primes left for Ben.

3. **Round 3** (n = 1):

There are no primes to pick from.
Ben wins as Maria cannot make a move.
Ben wins 2 rounds, Maria wins 1 round. Thus, Ben is the overall winner.
