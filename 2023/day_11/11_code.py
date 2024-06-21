DAY_NUM = str(11).zfill(2)

def find_index(target, iterable):
    for index, item in enumerate(iterable):
        if item == target:
            return index
    return None

def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(f"{symbol}", end='')
        print()
    print()

def get_expansions(p1, p2, items_with_galaxies, row_or_col):
    start = min(p1[row_or_col], p2[row_or_col])
    end = max(p1[row_or_col], p2[row_or_col]) + 1
    num_expansions = 0
    for i in range(start, end):
        if i not in items_with_galaxies:
            num_expansions += 1
    return num_expansions

def get_expanded_point(point, num_col_expansions, num_row_expansions, expansion_factor):
    expanded_point = {
        'id': point['id'],
        'row': point['row'] + num_row_expansions * expansion_factor,
        'col': point['col'] + num_col_expansions * expansion_factor
    }
    return expanded_point

def get_sum_of_distances(grid, expansion_factor):
    rows_with_galaxies = []
    cols_with_galaxies = []
    galaxies = []
    galaxy_id = 0
    for row_index, row in enumerate(grid):
        if '#' in row:
            rows_with_galaxies.append(row_index)
            for col_index in range(len(row)):
                if row[col_index] == '#':
                    galaxy_id += 1
                    galaxies.append({"id": galaxy_id, "row": row_index, "col": col_index})
                    if col_index not in cols_with_galaxies:
                        cols_with_galaxies.append(col_index)

    unique_pairs = get_unique_pairs(len(galaxies))
    distances = []
    for pair in unique_pairs:
        p1 = next(galaxy for galaxy in galaxies if galaxy["id"] == pair[0])
        p2 = next(galaxy for galaxy in galaxies if galaxy["id"] == pair[1])
        num_row_expansions = get_expansions(p1, p2, rows_with_galaxies, 'row')
        num_col_expansions = get_expansions(p1, p2, cols_with_galaxies, 'col')
        distance = get_manhattan_distance(p1, p2, num_col_expansions, num_row_expansions, expansion_factor)
        distances.append(distance)
    # print(f"Rows with galaxies: {rows_with_galaxies}")
    # print(f"Cols with galaxies: {cols_with_galaxies}")
    # print(f"Galaxies:")
    # for galaxy in galaxies:
    #     print(f"  {galaxy}")
    # print(f"Unique Pairs | Distances:")
    # for item in zip(unique_pairs, distances):
    #     print(f"  {item[0]} | {item[1]}")
    # print(f"Distances:")
    # for distance in distances:
    #     print(f"  {distance}")
    return sum(distances)

def print_galaxies(input_grid, galaxies):
    grid = list(input_grid)
    for galaxy in galaxies:
        grid[galaxy['row']][galaxy['col']] = galaxy['id']
    print_grid(grid)

def get_unique_pairs(num_galaxies):
    unique_pairs = []
    for i in range(num_galaxies):
        for j in range(i + 1, num_galaxies):
            unique_pairs.append((i + 1, j + 1))
    return unique_pairs

def get_manhattan_distance(p1, p2, num_col_expansions, num_row_expansions, expansion_factor):
    row_distance = abs(p1['row'] - p2['row']) - num_row_expansions + (num_row_expansions * expansion_factor)
    col_distance = abs(p1['col'] - p2['col']) - num_col_expansions + (num_col_expansions * expansion_factor)
    # print(f"p1: {p1}")
    # print(f"p2: {p2}")
    # print(f"num_row_expansions: {num_row_expansions}")
    # print(f"num_col_expansions: {num_col_expansions}")
    # print(f"expansion_factor: {expansion_factor}")
    # print(f"row_distance: {row_distance}")
    # print(f"col_distance: {col_distance}")
    # print(f"distance: {row_distance + col_distance}")
    return row_distance + col_distance

def process_input(file):
    grid = [list(line) for line in file.read().strip().split('\n')]
    return grid

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        grid = process_input(file)
        result = get_sum_of_distances(grid, expansion_factor=2)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        grid = process_input(file)
        result = get_sum_of_distances(grid, expansion_factor=1000000)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        grid = process_input(file)
        result = get_sum_of_distances(grid, expansion_factor=2)
        expected = 374
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        grid = process_input(file)
        result = get_sum_of_distances(grid, expansion_factor=10)
        expected = 1030
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        grid = process_input(file)
        result = get_sum_of_distances(grid, expansion_factor=100)
        expected = 8410
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 9445168
    test_puzzle_b()
    puzzle_b() # Solution: 742305960572
