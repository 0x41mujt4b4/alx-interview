#!/usr/bin/env python3
"""Minimum Operations module"""
from math import log2


def minOperations(n):
    """Calculates the minimum number of operations to achieve n 'H' characters."""
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op