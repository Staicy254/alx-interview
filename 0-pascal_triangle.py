#!/usr/bin/python3
"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: where each inner list represents a row of Pascal's triangle.
    """

    if n <= 0:
        return []

    # Initialize an empty resulting array
    pascal = [[] for _ in range(n)]

    for li in range(n):
        for col in range(li + 1):
            if col == 0 or col == li:
                # The first and last column of each row is always 1
                pascal[li].append(1)
            else:
                # Sum of the two numbers above the current position
                above_left = pascal[li - 1][col - 1]
                above_right = pascal[li - 1][col]
                pascal[li].append(above_left + above_right)

    return pascal
