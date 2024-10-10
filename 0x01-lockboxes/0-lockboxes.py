#!/usr/bin/python3
"""Module to solve interview problem"""


def canUnlockAll(boxes):
    """Function that solve lockboxes problem"""
    n = len(boxes)
    opened_boxes = set([0])
    keys = [0]
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                keys.append(key)
    return len(opened_boxes) == n
