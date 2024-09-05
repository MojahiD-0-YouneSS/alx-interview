#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n."""
    if n <= 0:
        return []
    
    res = [[1]]  
    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    
    return res
