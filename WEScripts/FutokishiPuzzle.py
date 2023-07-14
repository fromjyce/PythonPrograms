def solve_futoshiki(puzzle, constraints):
    if is_solved(puzzle):
        return puzzle
    row, col = find_empty_cell(puzzle)
    for num in range(1, len(puzzle) + 1):
        if is_valid_move(puzzle, row, col, num, constraints):
            puzzle[row][col] = num
            if solve_futoshiki(puzzle, constraints):
                return puzzle
            puzzle[row][col] = 0
    return None


def is_solved(puzzle) -> bool:
    for row in puzzle:
        if 0 in row:
            return False
    return True


def find_empty_cell(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j
    return None, None


def is_valid_move(puzzle, row: int, col: int, num: int, constraints) -> bool:
    size = len(puzzle)
    for j in range(size):
        if puzzle[row][j] == num:
            return False
    for i in range(size):
        if puzzle[i][col] == num:
            return False
    for constraint in constraints:
        cell1, cell2, operator = constraint
        r1, c1 = cell1
        r2, c2 = cell2
        value1 = puzzle[r1][c1]
        value2 = puzzle[r2][c2]

        if value1 != 0 and value2 != 0:
            if operator == "<" and value1 <= value2:
                return False
            if operator == ">" and value1 >= value2:
                return False

    return True


def display_puzzle(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=" ")
        print()


def get_input():
    puzzle = [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    constraints = [((1, 1), (1, 2), "<"), ((2, 1), (2, 2), "<"), ((2, 2), (3, 2), "<")]
    return puzzle, constraints


def main():
    puzzle, constraints = get_input()
    solved_puzzle = solve_futoshiki(puzzle, constraints)
    if solved_puzzle:
        display_puzzle(solved_puzzle)
    else:
        print("No solution found.")


main()
