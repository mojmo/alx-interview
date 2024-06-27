#!/usr/bin/python3

"""Determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list): A list of integers where each integer represents a byte
    (8 least significant bits considered).

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits of each byte
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:

        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF
        mask_byte = 1 << 7

        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            # by counting leading 1s
            while mask_byte & byte:
                num_bytes += 1
                mask_byte >>= 1

            # If no leading 1s were found, it's a 1-byte character
            if num_bytes == 0:
                continue

            # If the number of bytes is 1 or more than 4, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # If this is a continuation byte, it must start with 10xxxxxx
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        # Decrement the number of bytes remaining in the current character
        num_bytes -= 1

    # If we finish and have no more expected continuation bytes, return True
    return num_bytes == 0
