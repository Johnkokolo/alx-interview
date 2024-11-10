#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position on the board.
    Checks the column and both diagonals to ensure no queens threaten this position.

    Args:
        board (list): List where index is row and value is column of the queen.
        row (int): Row index of the board.
        col (int): Column index of the board.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col:
            return False

    # Check the main diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check the secondary diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row, solutions):
    """
    Recursive function to solve the N-Queens problem.

    Args:
        board (list): List where index is row and value is column of the queen.
        row (int): The current row index to place a queen.
        solutions (list): List of solutions where each solution is a list of queen positions.
    """
    n = len(board)
    if row == n:
        # All queens are placed successfully, so save the solution
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1  # Backtrack

def nqueens(n):
    """
    Solve the N-Queens problem and print each solution.

    Args:
        n (int): Size of the board (n x n) and the number of queens.
    """
    board = [-1] * n  # Initialize the board with -1
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Validate input arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
