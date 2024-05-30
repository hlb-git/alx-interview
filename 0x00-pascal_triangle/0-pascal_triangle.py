#!/usr/bin/python3
""" Function to print a Pascal Triangle """


def pascal_triangle(n):
    """
    Create a function that returns a list of lists
    of integers representing Pascal’s triangle of n levels.
    """
    triangle = []
    if n > 0:
        for row_number in range(1, n + 1):
            row = []
            value = 1
            for position in range(1, row_number + 1):
                row.append(value)
                value = value * (row_number - position) // position
            triangle.append(row)
    return triangle
