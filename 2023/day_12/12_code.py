import functools

DAY_NUM = str(12).zfill(2)

def process_input(file):
    rows = []
    for line in file.read().strip().split('\n'):
        raw_springs, raw_groups = line.split(' ')
        springs = tuple(spring for spring in raw_springs)
        groups = tuple(int(group) for group in raw_groups.split(','))
        rows.append((springs, groups))
    return rows

def does_group_match_beginning(springs, group):
    if len(springs) < group:
        return False
    matches_beginning = '.' not in springs[:group]
    following_spring_is_valid = (len(springs) == group or springs[group] != '#')
    if matches_beginning and following_spring_is_valid:
        return True
    return False

@functools.lru_cache(maxsize=None)
def get_num_arrangements(springs, groups, depth=0):
    indent = ''.join(['  '] * depth)
    depth += 1
    # print(f"{indent}---")
    # print(f"{indent}springs: {''.join(springs)} // groups: {groups}")
    total = sum(groups)
    minimum = sum(spring == '#' for spring in springs)
    maximum = sum(spring != '.' for spring in springs)
    if minimum > total or maximum < total:
        # print(f"{indent}Invalid configuration (min {minimum}, max {maximum}, total {total}). Returning 0.")
        return 0
    if total == 0:
        # print(f"{indent}Base case. No groups requested. Only one configuration allowed. Returning 1.")
        return 1
    if springs[0] == '.':
        # print(f"{indent}First spring is a '.', no impact on arrangements. Removing and recursing.")
        return get_num_arrangements(springs[1:], groups, depth)
    if springs[0] == '#':
        # print(f"{indent}First spring is a '#'. Checking if the first group matches the beginning.")
        first_group = groups[0]
        is_matching_group = does_group_match_beginning(springs, first_group)
        if is_matching_group:
            if len(springs) == first_group:
                # print(f"{indent}Match found for group {first_group}: {springs[:first_group]}. Returning 1.")
                return 1
            # print(f"{indent}Match found for group {first_group}: {springs[:first_group]}. Removing and recursing.")
            return get_num_arrangements(springs[(first_group + 1):], groups[1:], depth)
        # print(f"{indent}Match not found. Returning 0.")
        return 0
    # print(f"{indent}First spring is a '?'. Recursing over both branches and adding results.")
    # springs[0] must be '?'
    value_if_dot = get_num_arrangements(tuple('.') + springs[1:], groups, depth)
    value_if_hash = get_num_arrangements(tuple('#') + springs[1:], groups, depth)
    # print(f"{indent}!!!! Completed checking branches for '{''.join(springs)}' ({groups}). Value if dot: {value_if_dot}. Value if hash: {value_if_hash}.")
    return value_if_dot + value_if_hash

def get_expansion(row, expansion_factor):
    springs, groups = row
    if expansion_factor == 1:
        return row
    expanded_springs = ((springs + tuple('?')) * expansion_factor)[:-1]
    expanded_groups = groups * expansion_factor
    # print(f"Initial row: {springs} // {groups}")
    # print(f"Expanded row: {expanded_springs} // {expanded_groups}")
    return (expanded_springs, expanded_groups)


def get_sum_of_arrangements(rows, expansion_factor):
    expanded_rows = [get_expansion(row, expansion_factor) for row in rows]
    return sum(get_num_arrangements(springs, groups) for springs, groups in expanded_rows)

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        rows = process_input(file)
        result = get_sum_of_arrangements(rows, expansion_factor=1)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        rows = process_input(file)
        result = get_sum_of_arrangements(rows, expansion_factor=5)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        rows = process_input(file)
        result = get_sum_of_arrangements(rows, expansion_factor=1)
        expected = 21
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        rows = process_input(file)
        result = get_sum_of_arrangements(rows, expansion_factor=5)
        expected = 525152
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 7007
    test_puzzle_b()
    puzzle_b() # Solution: 3476169006222
