#!/usr/bin/python3

def validUTF8(data):
    def check_bytes(num_bytes, data):
        for i in range(1, num_bytes):
            if idx + i >= len(data) or (data[idx + i] >> 6) != 0b10:
                return False
        return True

    idx = 0
    while idx < len(data):
        # Get the number of bytes for this character
        num_bytes = 0
        if (data[idx] >> 7) == 0:
            num_bytes = 1
        elif (data[idx] >> 5) == 0b110:
            num_bytes = 2
        elif (data[idx] >> 4) == 0b1110:
            num_bytes = 3
        elif (data[idx] >> 3) == 0b11110:
            num_bytes = 4
        else:
            return False

        # Check if the next 'num_bytes - 1' bytes are of form '10xxxxxx'
        if not check_bytes(num_bytes, data):
            return False

        idx += num_bytes

    return True
