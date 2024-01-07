#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    of Pascal’s triangle of n
    """

    # Check if n is less than or equal to 0
    if n <= 0:
        return []
    # Initialize the triangle with the first row [1]
    triangle = [[1]]

    # Loop to generate each subsequent row of Pascal's Triangle
    for i in range(1, n):
        # The first element in each row is always 1
        row = [1]
        # Loop to calculate the middle elements in the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
