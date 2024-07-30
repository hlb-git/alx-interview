#!/usr/bin/python3
""" Module to calculate perimeter of island in grid """

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """ Calculate the number of boundaries of a cell """
    boundaries = 0
    try:
        if i == 0:
            boundaries += 1
        elif grid[i-1][j] == 0:  # checks the top cell
            boundaries += 1
    except Exception:
        boundaries += 1  # executes if the iteration is out of bound
    try:
        if grid[i+1][j] == 0:  # checks the bottom cell
            boundaries += 1
    except Exception:
        boundaries += 1
    try:
        if grid[i][j+1] == 0:  # checks the right of the cell
            boundaries += 1
    except Exception:
        boundaries += 1
    try:
        if j == 0:
            boundaries += 1
        elif grid[i][j-1] == 0:  # checks the left of the cell
            boundaries += 1
    except Exception:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """ Calculate the perimeter of an island """
    if grid == []:
        return 0
    length = len(grid)
    width = len(grid[0])
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
