def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start the row with 1
        row = [1]
        # Get the previous row from the triangle
        prev_row = triangle[i - 1]

        # Each element in the row is the sum of the two elements above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # End the row with 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
