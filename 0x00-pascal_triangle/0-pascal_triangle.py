#!/usr/bin/python3

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
def pascal_triangle(n):

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with first row

    for i in range(1, n):
        row = [1]  # Start with 1
        for j in range(1, i):
            # Calculate middle elements as sum of two elements directly above
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle
