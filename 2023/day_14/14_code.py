DAY_NUM = str(14).zfill(2)

def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(f"{symbol}", end='')
        print()
    print()

def process_input(file):
    matrix = []
    for row in file.read().strip().split('\n'):
        matrix.append(list(row))
    return matrix

def rotate_matrix(matrix, direction):
    if direction == 'right':
        rotated_matrix = [list(row)[::-1] for row in zip(*matrix)]
    else:
        rotated_matrix = [list(x) for x in zip(*matrix)][::-1]
    return rotated_matrix

def roll_rocks(str):
    return str.replace('O.', '.O')

def get_rotated_matrix(matrix, direction):
    rotations = []
    if direction == 'north':
        rotations = ['right']
    if direction == 'west':
        rotations = ['right', 'right']
    if direction == 'south':
        rotations = ['left']
    if direction == 'east':
        rotations = []
    rotated_matrix = matrix
    for rotation in rotations:
        rotated_matrix = rotate_matrix(rotated_matrix, rotation)
    return rotations, rotated_matrix

def get_rolled_matrix(matrix):
    rolled_matrix = []
    for row in matrix:
        old = ''.join(row)
        # print(f"Old: {old}")
        while True:
            new = roll_rocks(old)
            # print(f"New: {new}")
            if new == old:
                # print(f"Matches. Breaking loop.")
                break
            old = new
        rolled_matrix.append(list(new))
    return rolled_matrix

def get_final_matrix(matrix, direction):
    # print("Before:")
    # print_grid(matrix)
    # print(f"\nRotating {direction}.")
    rotations, rotated_matrix = get_rotated_matrix(matrix, direction)
    # print(f"\nAfter forward rotations ({rotations}):")
    # print_grid(rotated_matrix)
    rolled_matrix = get_rolled_matrix(rotated_matrix)
    # print("\nAfter rolling the rocks:")
    # print_grid(rolled_matrix)
    final_matrix = rolled_matrix
    for rotation in rotations:
        inverted_rotation = 'left' if rotation == 'right' else 'right'
        final_matrix = rotate_matrix(final_matrix, inverted_rotation)
    # print("\nAfter undoing the rotations:")
    # print_grid(final_matrix)
    return final_matrix

def get_hashable(matrix):
    flattened = []
    for row in matrix:
        flattened.extend(row)
    return tuple(flattened)

def get_matrix_from_hashable(hashable, width):
    expanded = []
    row = []
    for i, item in enumerate(hashable):
        row.append(item)
        if i > 0 and i % width == 0:
            expanded.append(row)
            row = []
    return expanded

def get_northern_load(matrix):
    load = 0
    for i, row in enumerate(matrix):
        for char in row:
            if char == 'O':
                load += (len(matrix) - i)
    return load

def get_total_load(matrix, num_spin_cycles=None):
    if num_spin_cycles:
        start_matrix = matrix
        seen_indexes, seen_values = {}, {}
        has_loop = False
        for i in range(num_spin_cycles):
            hashable = get_hashable(start_matrix)
            if hashable in seen_indexes:
                print(f"Loop found!")
                has_loop = True
                break
            seen_indexes[hashable] = i
            seen_values[i] = get_northern_load(start_matrix)
            rolled_north = get_final_matrix(start_matrix, 'north')
            rolled_west = get_final_matrix(rolled_north, 'west')
            rolled_south = get_final_matrix(rolled_west, 'south')
            rolled_east = get_final_matrix(rolled_south, 'east')
            start_matrix = rolled_east
            # print(f"Completed cycle {str(i).zfill(3)}: {''.join(hashable)}")
        if has_loop:
            # print(f"Completed cycle {str(i).zfill(3)}: {''.join(hashable)}")
            loop_start = seen_indexes[hashable]
            loop_length = i - loop_start
            index_matching_final = loop_start + ((num_spin_cycles - loop_start) % loop_length)
            # print(f"Loop start: {loop_start}")
            # print(f"Loop length: {loop_length}")
            # print(f"Index matching final: {index_matching_final}")
            return seen_values[index_matching_final]
        else:
            rolled_matrix = rolled_east
    else:
        rolled_matrix = get_final_matrix(matrix, 'north')
    return get_northern_load(rolled_matrix)

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix, num_spin_cycles=1_000_000_000)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix)
        expected = 136
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix, num_spin_cycles=1)
        expected = 87
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix, num_spin_cycles=2)
        expected = 69
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix, num_spin_cycles=3)
        expected = 69
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        matrix = process_input(file)
        result = get_total_load(matrix, num_spin_cycles=1_000_000_000)
        expected = 64
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 108759
    test_puzzle_b()
    puzzle_b() # Solution: 89089
