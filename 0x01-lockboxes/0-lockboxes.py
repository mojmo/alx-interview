#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of boxes, each containing a list of keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened_boxes = set()
    keys = [0]

    while keys:
        key = keys.pop()
        if key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
