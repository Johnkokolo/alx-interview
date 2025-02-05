#!/usr/bin/python3
    
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # First row, which is always [1]
    
    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Add the sum of the two numbers above
        row.append(1)  # End each row with 1
        triangle.append(row)
    
    return triangle
