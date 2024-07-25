"""
Module for printing Pascal's triangle.

 Contains a function to print Pascal's triangle given the number of rows.
"""

pascal_triangle = __import__("0-pascal_triangle").pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
