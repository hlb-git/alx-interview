#!/usr/bin/python3
"""minimum operation module"""

def minOperations(n):
    """minimum operations to reach n from 1"""
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
