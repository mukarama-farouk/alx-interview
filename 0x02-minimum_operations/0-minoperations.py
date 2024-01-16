#!/usr/bin/python3
"""This module calculates the fewest number of operations needed to
result in exactly n H characters in the file"""

def minOperations(n):
    """ minOperations
    Gets fewest # of operations needed to result in exactly n H characters"""
    # all outputs should be at least 2 char: (min, Copy All => Paste)

    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
