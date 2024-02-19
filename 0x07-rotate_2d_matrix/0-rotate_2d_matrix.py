#!/usr/bin/python3
"""0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

# def rotate_2d_matrix(matrix):
#     """Function to perform the matrix rotation
#     """
#     n = m = t = 0
#     mat_len = len(matrix)
#     while n + m < mat_len - 1:
#         while n + m < mat_len - 1:
#             o, p = n, m
#             curr_val = matrix[n][m]
#             for i in range(4):
#                 next_val = matrix[p][(mat_len - 1) - o]
#                 matrix[p][(mat_len - 1) - o] = curr_val
#                 curr_val = next_val
#                 temp = o
#                 o = p
#                 p = (mat_len - 1) - temp
#             n += 1
#         t += 1
#         n = m = t
