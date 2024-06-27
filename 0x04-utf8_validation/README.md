# 0x04. UTF-8 Validation

This folder contains a Python function `validUTF8` that determines if a given data set represents a valid UTF-8 encoding. The function takes a list of integers where each integer represents a byte and returns `True` if the data set is a valid UTF-8 encoding, otherwise it returns `False`.

## Explanation

The validUTF8 function works as follows:

- **Initialization and Byte Masking:** The bytes are masked using byte = byte & 0xFF to ensure only the 8 least significant bits are considered.

- **Counting the Number of Bytes:** A while loop is used to count the leading 1s in the byte to determine the number of bytes in the UTF-8 character. This count is stored in num_bytes.

- **Handling Continuation Bytes:** If num_bytes is greater than 0, it checks if the current byte is a valid continuation byte (it should start with 10xxxxxx). If it is not valid, the function returns False.

- **Validation of Initial Bytes:** If the number of leading 1s is 1 or more than 4, the function returns False as these are invalid UTF-8 sequences.

- **Final Check:** At the end of the loop, the function checks if num_bytes is 0, which means all characters are complete and valid. If num_bytes is not 0, it means the data ends with incomplete characters, and the function returns False.

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
