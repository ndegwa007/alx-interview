#!/usr/bin/python3
"""returns perimeter of the grid"""


def island_perimeter(grid):
    """perimeter of the island, 1 represents land"""
    length_row = len(grid)
    length_column = len(grid[0])
    p = 0
    connects = 0
    for x in range(0, length_row):
        for y in range(0, length_column):

            if grid[x][y] == 1:
                p += 4

                if x != 0 and grid[x-1][y] == 1:
                    connects += 1
                if y != 0 and grid[x][y-1] == 1:
                    connects += 1

    return p - (connects * 2)
