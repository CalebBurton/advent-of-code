DAY_NUM = str(10).zfill(2)

class Square:
    def __init__(self, row, col, symbol, direction=None):
        self.row = row
        self.col = col
        self.symbol = symbol
        self.direction = direction

    def __str__(self):
        return f'S("{self.symbol}", row={self.row}, col={self.col})'

    def __repr__(self):
        return f'S("{self.symbol}")'

    def __eq__(self, other):
        # Ignores symbol and direction, just looks at the square's coordinates
        return self.row == other.row and self.col == other.col

def find_index(target, iterable):
    for index, item in enumerate(iterable):
        if item == target:
            return index
    return None

def print_route(route):
    print(f"Route:")
    for row in route:
        for square in row:
            print(square.symbol, end='')
        print()

def trace_route(grid, start):
    is_complete = False
    iterations = 0
    route = [[start]]
    while not is_complete:
        neighbors = []
        for square in route[-1]:
            # print(f"Square: {square}")
            neighbors.extend(find_valid_neighbors(grid, square))
        route.append(neighbors)
        is_complete = (
            len(neighbors) > 1 and
            neighbors[0].row == neighbors[1].row and
            neighbors[0].col == neighbors[1].col
        )
        # print(f"Neighbors: {neighbors}")
        # print_route(route)
        # print(f"Is Complete: {is_complete}")
        # print(f"----")
        iterations += 1
        # print(f"Iterations: {iterations}")
    return route

UP_FACING_SYMBOLS    = ["|", "L", "J"]
DOWN_FACING_SYMBOLS  = ["|", "7", "F"]
LEFT_FACING_SYMBOLS  = ["-", "7", "J"]
RIGHT_FACING_SYMBOLS = ["-", "L", "F"]

def is_valid_connection(initial_symbol, new_square):
    if new_square.symbol == ".":
        return False
    if new_square.direction == "up":
        return new_square.symbol in DOWN_FACING_SYMBOLS and (initial_symbol in UP_FACING_SYMBOLS or initial_symbol == "S")
    if new_square.direction == "down":
        return new_square.symbol in UP_FACING_SYMBOLS and (initial_symbol in DOWN_FACING_SYMBOLS or initial_symbol == "S")
    if new_square.direction == "left":
        return new_square.symbol in RIGHT_FACING_SYMBOLS and (initial_symbol in LEFT_FACING_SYMBOLS or initial_symbol == "S")
    if new_square.direction == "right":
        return new_square.symbol in LEFT_FACING_SYMBOLS and (initial_symbol in RIGHT_FACING_SYMBOLS or initial_symbol == "S")
    return False

def find_valid_neighbors(grid, initial):
    neighbors = []
    if initial.col > 0 and initial.direction != "right":
        neighbor_row = initial.row
        neighbor_col = initial.col + -1
        neighbors.append(Square(neighbor_row, neighbor_col, grid[neighbor_row][neighbor_col], "left"))
    if initial.col < len(grid[0]) - 1 and initial.direction != "left":
        neighbor_row = initial.row
        neighbor_col = initial.col + 1
        neighbors.append(Square(neighbor_row, neighbor_col, grid[neighbor_row][neighbor_col], "right"))
    if initial.row > 0 and initial.direction != "down":
        neighbor_row = initial.row - 1
        neighbor_col = initial.col
        neighbors.append(Square(neighbor_row, neighbor_col, grid[neighbor_row][neighbor_col], "up"))
    if initial.row < len(grid) - 1 and initial.direction != "up":
        neighbor_row = initial.row + 1
        neighbor_col = initial.col
        neighbors.append(Square(neighbor_row, neighbor_col, grid[neighbor_row][neighbor_col], "down"))
    valid_neighbors = [neighbor for neighbor in neighbors if is_valid_connection(initial.symbol, neighbor)]
    return valid_neighbors

def find_start(grid):
    start_col, start_row = None, None
    for row_index, line in enumerate(grid):
        start_col = find_index("S", line)
        if start_col is not None:
            start_row = row_index
            break
    start = Square(start_row, start_col, "S")
    neighbors = find_valid_neighbors(grid, start)
    for neighbor in neighbors:
        if neighbor.row < start.row:
            UP_FACING_SYMBOLS.append("S")
        elif neighbor.row > start.row:
            DOWN_FACING_SYMBOLS.append("S")
        elif neighbor.col < start.col:
            LEFT_FACING_SYMBOLS.append("S")
        elif neighbor.col > start.col:
            RIGHT_FACING_SYMBOLS.append("S")
    print(f"Start: {start}")
    return start

def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(f"{symbol}", end='')
        print()
    print()

def process_input(file):
    grid = [list(line) for line in file.read().strip().split('\n')]
    # print_grid(grid)
    return grid

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = len(route) - 1
    print(f"Result: {result}\n")

def is_part_of_route(square, route):
    for step in route:
        # print(f"Step: {step}")
        for test_square in step:
            if test_square == square:
                # print(f"Found {test_square} in route at step {step}")
                return True
    # print(f"Did not find {square} in route")
    return False

def get_num_interior(grid, route):
    num_interior_tiles = 0
    for row_index in range(len(grid)):
        is_inside = False
        for col_index in range(len(grid[0])):
            symbol = grid[row_index][col_index]
            is_border = is_part_of_route(Square(row_index, col_index, symbol), route)
            if is_border:
                if symbol in UP_FACING_SYMBOLS:
                    is_inside = not is_inside
            else:
                num_interior_tiles += is_inside
    return num_interior_tiles

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = get_num_interior(grid, route)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        grid = process_input(file)
        start = find_start(grid, )
        route = trace_route(grid, start)
        result = len(route) - 1
        expected = 4
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

    with open(f"{DAY_NUM}_test_input_2.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = len(route) - 1
        expected = 8
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_3.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = get_num_interior(grid, route)
        expected = 4
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

    with open(f"{DAY_NUM}_test_input_4.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = get_num_interior(grid, route)
        expected = 8
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

    with open(f"{DAY_NUM}_test_input_5.txt") as file:
        grid = process_input(file)
        start = find_start(grid)
        route = trace_route(grid, start)
        result = get_num_interior(grid, route)
        expected = 10
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 6773
    test_puzzle_b()
    puzzle_b() # Solution: 493
