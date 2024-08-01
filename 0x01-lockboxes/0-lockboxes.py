#!/usr/bin/env python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes=[]):
    """A function that returns True if all boxes in
    the list can be opened
    """
    if not boxes:
        return False

    keys = set([0])  # Start with the key to the first box
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True


if __name__ == '__main__':
    boxes = [
                [1, 3],
                [2],
                [3, 0],
                [1, 2, 3],
            ]
    print(canUnlockAll(boxes))  # Call the correct function

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Call the correct function

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Call the correct function

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Call the correct function
