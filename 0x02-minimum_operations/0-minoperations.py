#!/usr/bin/python3
"""Minimum Operations module"""
from math import log2


def minOperations(n):
    """Calculates the minimum number of operations"""
    if n <= 1:
        return 0

    operation_needed = 0
    clipbord = 0
    current_lenght = 1

    while current_lenght < n:
        if n % current_lenght == 0:
            clipbord = current_lenght
            operation_needed += 1

        current_lenght += clipbord
        operation_needed += 1

    return operation_needed
