# 0x02. Minimum Operations

## Description

This project contains a Python function to calculate the minimum number of operations required to achieve exactly `n` 'H' characters in a text file starting from a single 'H'. The allowed operations are "Copy All" and "Paste".

## Problem Statement

Given a text file with a single character 'H', you can perform the following operations:

1. **Copy All**: Copy all the characters in the file.
2. **Paste**: Paste the copied characters.

You need to write a function `minOperations(n)` that returns the fewest number of operations needed to result in exactly `n` 'H' characters in the file. If it's impossible to achieve exactly `n` characters, the function should return 0.

## How It Works

### Initialization:
- The function starts with a single 'H'.
- The `operations` counter is initialized to zero.
- The `factor` starts at 2, the smallest prime number.

### Factorization Process:
- The function uses a while loop to continue processing as long as `n` is greater than 1.
- Inside the loop, for each factor, it checks if `n` is divisible by the factor.
- If `n` is divisible, it divides `n` by the factor and adds the factor to the `operations` count.
- The factor is incremented to check the next potential prime factor.

### Final Check:
- After reducing `n` to 1 through division by its prime factors, the function returns the total number of operations.

## Test Cases

### Example 1
```python
n = 9
print(minOperations(n))  # Should return 6
