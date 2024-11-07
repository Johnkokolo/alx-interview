def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of size n.

    Args:
        n (int): The size of Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
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

