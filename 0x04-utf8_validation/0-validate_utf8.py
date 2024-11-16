#!/usr/bin/python3
"""
Main file for testing
"""

def validUTF8(data):
    # This variable will track the number of continuation bytes we expect
    num_bytes = 0

    for byte in data:
        # Check the first 3 bits of the byte to determine the type of byte (1-byte, 2-byte, etc.)
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False  # Invalid first byte
        else:
            # For continuation bytes, the 2 most significant bits must be 10
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0  # If all expected continuation bytes are matched
