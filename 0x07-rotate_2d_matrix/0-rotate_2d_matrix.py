#!/usr/bin/python3
"""rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """rotation clockwise"""
    N = len(matrix)

    for r in range(N):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in matrix:
        r.reverse()
