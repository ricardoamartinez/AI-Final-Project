import random

def generate_sudoku(difficulty):
    # Initialize an empty 9x9 grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the diagonal 3x3 boxes with random numbers
    for i in range(0, 9, 3):
        fill_box(grid, i, i)

    # Solve the grid to ensure it has a valid solution
    solve(grid)

    # Remove numbers based on the difficulty level
    remove_numbers(grid, difficulty)

    return grid

def fill_box(grid, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)

    for i in range(3):
        for j in range(3):
            grid[row + i][col + j] = nums[i * 3 + j]

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

def remove_numbers(grid, difficulty):
    count = 0
    while count < difficulty:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if grid[row][col] != 0:
            grid[row][col] = 0
            count += 1