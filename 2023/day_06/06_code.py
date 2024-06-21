from functools import reduce

DAY_NUM = str(6).zfill(2)

def get_num_ways_to_win(races):
    num_ways_to_win = []
    for race_index, race in enumerate(races):
        ways_to_win = []
        time, record = race
        for ms_held in range(time + 1):
            speed = ms_held
            remaining_time = time - ms_held
            distance = speed * remaining_time
            if distance > record:
                ways_to_win.append(ms_held)
            # print(f"Holding for {ms_held} ms gives a distance of {distance}")
        num_ways_to_win.append(len(ways_to_win))
        print(f"Race {race_index} has {len(ways_to_win)} ways to win.")
    total_num_ways_to_win = reduce(lambda x,y: x * y, num_ways_to_win)
    return total_num_ways_to_win

def process_input_a(file):
    lines = file.read().strip().split('\n')
    times = [int(time) for time in list(filter(None, lines[0].strip('Time:').strip().split(' ')))]
    records = [int(distance) for distance in list(filter(None, lines[1].strip('Distance:').strip().split(' ')))]
    print(f"Times: {times}, Records: {records}")
    assert len(times) == len(records)
    races = list(zip(times, records))
    return races

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        races = process_input_a(file)
        result = get_num_ways_to_win(races)
    print(f"Result: {result}\n")

def process_input_b(file):
    lines = file.read().strip().split('\n')
    time = int(lines[0].strip('Time:').replace(' ', ''))
    record = int(lines[1].strip('Distance:').replace(' ', ''))
    print(f"Time: {time}, Record: {record}")
    races = [(time, record)]
    return races

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        races = process_input_b(file)
        result = get_num_ways_to_win(races)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        races = process_input_a(file)
        result = get_num_ways_to_win(races)
        expected = 288
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        races = process_input_b(file)
        result = get_num_ways_to_win(races)
        expected = 71503
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 345015
    test_puzzle_b()
    puzzle_b() # Solution: 42588603
