#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    
    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.
    
    Returns:
    list of lists: Pascal's Triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each row from the second row onwards
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        
        # Calculate the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # End each row with a 1
        row.append(1)
        
        # Append the generated row to the triangle
        triangle.append(row)
        
    return triangle
