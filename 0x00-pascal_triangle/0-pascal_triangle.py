#!/usr/bin/python3
"""the pascal's triangle code"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row
    """
    triangle = []
    if n <= 0:
        return []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]
            row = [1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
            triangle.append(row)
    return triangle

