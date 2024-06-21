import math

DAY_NUM = str(13).zfill(2)

def process_input(file):
    mirrors = []
    for mirror in file.read().strip().split('\n\n'):
        rows = [list(row) for row in mirror.split('\n')]
        mirrors.append(rows)
    return mirrors

def is_valid_reflection(mirror, start_index, reflection_line, allowed_difference, distance=0):
    # indent = ''.join(['  ' for _ in range(distance)])
    # print(f"{indent}Checking reflection: {start_index}, {reflection_line}, {distance} ({allowed_difference})")
    index_before = math.floor(reflection_line) - distance
    index_after = math.ceil(reflection_line) + distance
    maximum = len(mirror) - 1
    if (index_before < 0) or (index_after > maximum):
        reached_allowed_difference = True if allowed_difference == 0 else False
        # print(f"{indent}Base case. Returning {reached_allowed_difference}.")
        return reached_allowed_difference
    before = mirror[index_before]
    after = mirror[index_after]
    difference = 0
    for before_char, after_char in zip(before, after):
        if before_char != after_char:
            difference += 1
            if difference > allowed_difference:
                # print(f"{indent}  Difference {difference} > {allowed_difference}. Returning False.")
                return False
    # print(f"{indent}  Difference: {difference} <= {allowed_difference}. Recursing.")
    return is_valid_reflection(mirror, start_index, reflection_line, allowed_difference - difference, distance + 1)

def find_horizontal_reflection_line(mirror, allowed_difference):
    reflection_line = 0
    for row_index, row in enumerate(mirror[:-1]):
        reflection_line = row_index + 0.5
        # print(f"Checking row {row_index} ({row}).")
        valid = is_valid_reflection(mirror, row_index, reflection_line, allowed_difference)
        if valid:
            return reflection_line
    return 0

def get_summary(mirrors, allowed_difference):
    summary = 0
    for mirror in mirrors:
        cols_to_left = 0
        rows_above = math.ceil(find_horizontal_reflection_line(mirror, allowed_difference))
        if not rows_above:
            rotated_mirror = list(map(list, zip(*mirror)))
            cols_to_left = math.ceil(find_horizontal_reflection_line(rotated_mirror, allowed_difference))
        summary += cols_to_left + (100 * rows_above)
    return summary

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        mirrors = process_input(file)
        result = get_summary(mirrors, allowed_difference=0)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        mirrors = process_input(file)
        result = get_summary(mirrors, allowed_difference=1)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        mirrors = process_input(file)
        result = get_summary(mirrors, allowed_difference=0)
        expected = 405
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        mirrors = process_input(file)
        result = get_summary(mirrors, allowed_difference=1)
        expected = 400
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_input.txt") as file:
        mirrors = [process_input(file)[0]]
        result = get_summary(mirrors, allowed_difference=1)
        expected = 1600
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_input.txt") as file:
        mirrors = [process_input(file)[1]]
        result = get_summary(mirrors, allowed_difference=1)
        expected = 500
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected
    with open(f"{DAY_NUM}_input.txt") as file:
        mirrors = [process_input(file)[2]]
        result = get_summary(mirrors, allowed_difference=1)
        expected = 9
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 27742
    test_puzzle_b()
    puzzle_b() # Solution: 32728
