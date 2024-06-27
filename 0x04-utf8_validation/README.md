# 0x04. UTF-8 Validation

This folder contains a Python function `validUTF8` that determines if a given data set represents a valid UTF-8 encoding. The function takes a list of integers where each integer represents a byte and returns `True` if the data set is a valid UTF-8 encoding, otherwise it returns `False`.

## Explanation

The validUTF8 function works as follows:

- It starts by initializing num_bytes to 0, which tracks the number of bytes in the current UTF-8 character.
- It uses bitwise masks to determine the number of bytes in a character and to validate continuation bytes.
- For each byte in the input list, the function checks if it starts a new UTF-8 character or is a valid continuation byte.
- If at any point a byte does not conform to UTF-8 encoding rules, the function returns False.
- If the entire list is processed without errors, the function returns True.

## Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Expected: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Expected: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Expected: False
```
