#!/usr/bin/python3
"""
module has a function that checks if a data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """checks if data is valid UTF-8 encoding"""
    i = 0
    while i < len(data):
        # get number of bytes of current character
        cur_byte = data[i]

        # determine the number of bytes for the current character
        if cur_byte and 0b10000000 == 0:
            num_bytes = 1
        elif cur_byte and 0b11100000 == 0b11000000:
            num_bytes = 2
        elif cur_byte and 0b11110000 == 0b11100000:
            num_bytes = 3
        elif cur_byte and 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False

        # check continuation bytes
        i += 1
        for _ in range(num_bytes - 1):
            if i >= len(data) or (data[i] and 0b11000000 != 0b10000000):
                return False
            i += 1
    return True
