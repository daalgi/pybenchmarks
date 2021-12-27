from typing import List
from random import randint

from base import Test


def ifs_inside_loop(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    
    dp = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                # First cell
                dp[r][c] = grid[0][0]
            elif c == 0:
                # First row
                dp[r][c] = grid[r][c] + dp[r-1][c]
            elif r == 0:
                # First column
                dp[r][c] = grid[r][c] + dp[r][c-1]
            else:
                # Interior cells
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
                
    return dp[-1][-1]


def multiple_loops(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    
    dp = [[0] * cols for _ in range(rows)]

    # First cell
    dp[0][0] = grid[0][0]

    # First row
    for c in range(1, cols):
        dp[0][c] = grid[0][c] + dp[0][c-1]

    # First column
    for r in range(1, rows):
        dp[r][0] = grid[r][0] + dp[r-1][0]

    # Interior cells
    for r in range(rows):
        for c in range(cols):
            dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
                
    return dp[-1][-1]
    

if __name__ == "__main__":

    lengths = [int(1e1), int(1e2), int(1e3), int(2e3)]
    repetitions = int(10)
    row_template = [randint(-10, 8) for _ in range(10)]
    for length in lengths:
        grid = [row_template * (length // 10) for _ in range(length)]

        output = f"\nGRID SIZE = {length}x{length}"
        output += f" -- REPETITIONS = {repetitions}"
        print(output)

        Test(ifs_inside_loop, grid, repetitions=repetitions, verbose=False)
        Test(multiple_loops, grid, repetitions=repetitions, verbose=False)
        