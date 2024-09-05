#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    res = []
    if n > 0:
        for i in range(n):
            level = [1]  # Start each level with 1
            # Calculate the values in the current level
            for j in range(1, i):
                level.append(level[j - 1] * (i - j + 1) // j)
            level.append(1)  # End each level with 1
            res.append(level)
    return res

