#!/usr/bin/python3
"""check if all boxes can be opened"""


def canUnlockAll(boxes):
    """check boxes to see if it contains keys to unlock
    else return false"""
    if not boxes or not boxes[0]:
        return False
    keys = []

    for value in boxes[0]:
        # value(key) should be > 0 and less than len(boxes)
        if value > 0 and value < len(boxes) and value not in keys:
            keys.append(value)
    # go through each key opening its corresponding
    # box and adding those key to the keys array
    for key in keys:
        # open box of key
        for value in boxes[key]:
            if value > 0 and value < len(boxes) and value not in keys:
                keys.append(value)

    return len(boxes) - 1 == len(keys)
