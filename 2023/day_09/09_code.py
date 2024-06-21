DAY_NUM = str(9).zfill(2)

def get_sequence(history):
    sequence = []
    for index in range(len(history)):
        # print(f"getting sequence for history: {history}; index: {index}; sequence so far: {sequence}")
        if index == len(history) - 1:
            break
        sequence.append(history[index + 1] - history[index])
    return sequence

def get_final_extrapolation(all_sequences, direction):
    extrapolations = []
    for index, sequence in enumerate(reversed(all_sequences)):
        if index == 0:
            extrapolation = 0
        else:
            if direction == "forward":
                extrapolation = sequence[-1] + extrapolations[-1]
            else:
                extrapolation = sequence[0] - extrapolations[-1]
        # print(f"processing sequence {index}: {sequence} // extrapolation: {extrapolation}")
        extrapolations.append(extrapolation)
    # print(f"all extrapolations: {extrapolations}")
    # print(f"final extrapolation: {extrapolations[-1]}")
    return extrapolations[-1]

def get_all_sequences(history):
    all_sequences = [history]
    completed = False
    while not completed:
        previous_sequence = all_sequences[-1]
        this_sequence = get_sequence(previous_sequence)
        all_sequences.append(this_sequence)
        completed = all(map(lambda entry: entry == 0, this_sequence))
        # print(f"this_sequence: {this_sequence}; completed? {completed}")
    return all_sequences

def get_extrapolation_sum(histories, direction="forward"):
    final_extrapolations = []
    for history in histories:
        all_sequences = get_all_sequences(history)
        final_extrapolations.append(get_final_extrapolation(all_sequences, direction))
    return sum(final_extrapolations)

def process_input(file):
    lines = file.read().strip().split('\n')
    histories = [list(map(lambda entry: int(entry), line.split(' '))) for line in lines]
    # print(f"histories: {histories}")
    return histories

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        histories = process_input(file)
        result = get_extrapolation_sum(histories)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        histories = process_input(file)
        result = get_extrapolation_sum(histories, "backward")
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        histories = process_input(file)
        actual = get_extrapolation_sum(histories)
        expected = 114
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        histories = process_input(file)
        actual = get_extrapolation_sum(histories, "backward")
        expected = 2
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 1842168671
    test_puzzle_b()
    puzzle_b() # Solution: 903
