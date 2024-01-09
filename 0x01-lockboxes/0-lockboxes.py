#!/usr/bin/python3
"""A module for working with lockboxes in python
"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """

    keys = set([0])

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                stack.append(key)

    return len(keys) == len(boxes)
