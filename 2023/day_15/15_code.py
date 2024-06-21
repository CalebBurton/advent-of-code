from functools import reduce
import re

DAY_NUM = str(15).zfill(2)

def process_input(file):
    return [sequence for sequence in file.read().strip().split(',')]

def get_hash(acc, char):
    return (17 * (acc + ord(char))) % 256

def get_final_hash_val(sequences):
    # acc = 0
    # for sequence in sequences:
    #     print(f"Sequence: '{sequence}'")
    #     for char in sequence:
    #         print(f"Char: '{char}'")
    #         new_val = reduce_hashes(acc, char)
    #         print(f"New val: {new_val}")
    #         acc += new_val
    # return acc
    return sum(reduce(get_hash, list(sequence), 0) for sequence in sequences)

def remove_label(label, boxes):
    new_boxes = []
    for box in boxes:
        if box[0] != label:
            new_boxes.append(box)
    return new_boxes

def upsert_label(new_box, boxes):
    new_label = new_box[0]
    is_existing_label = any(box[0] == new_label for box in boxes)
    # print(f"Is '{new_label}' an existing label? {is_existing_label}")
    if is_existing_label:
        return [new_box if old_box[0] == new_label else old_box for old_box in boxes]
    return boxes + [new_box]

def get_lens_order(sequences):
    boxes_by_index = [[] for _ in range(256)]
    boxes_by_label = {}
    count = 0
    for sequence in sequences:
        count += 1
        # print(f'Before "{sequence}":')
        label, focal_length = re.split(r'[=-]', sequence)
        hash_val = get_final_hash_val([label])
        # print(f"Label, focal length: ({label}, {focal_length})")
        # print(f"Target box ({hash_val}): {boxes_by_index[hash_val]})")
        if focal_length != '':
            boxes_by_index[hash_val] = upsert_label((label, int(focal_length)), boxes_by_index[hash_val])
            boxes_by_label[label] = hash_val
        else:
            try:
                index = boxes_by_label[label]
                boxes_by_index[index] = remove_label(label, boxes_by_index[index])
                del boxes_by_label[label]
            except Exception as e:
                # print(f"Exception raised: {e}")
                pass
        # print(f'\nAfter "{sequence}":')
        # print(f"Target box ({hash_val}): {boxes_by_index[hash_val]})")
        # print()
        # for i, box in enumerate(boxes_by_index):
        #     if len(box):
        #         print(f"Box {i}: {box}")
    return boxes_by_index

def get_focusing_power(box_num, lenses):
    power = 0
    for i, lens in enumerate(lenses):
        slot = i + 1
        focal_length = lens[1]
        power += box_num * slot * focal_length
    return power

def get_total_focusing_power(boxes):
    total_power = 0
    for i, box in enumerate(boxes):
        box_num = i + 1
        total_power += get_focusing_power(box_num, box)
    return total_power

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        sequences = process_input(file)
        result = get_final_hash_val(sequences)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        sequences = process_input(file)
        boxes = get_lens_order(sequences)
        result = get_total_focusing_power(boxes)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        sequences = process_input(file)
        result = get_final_hash_val(sequences)
        expected = 1320
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        sequences = process_input(file)
        boxes = get_lens_order(sequences)
        result = get_total_focusing_power(boxes)
        expected = 145
        print(f"Actual: {result}  //  Expected: {expected}\n")
        assert result == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 507666
    test_puzzle_b()
    puzzle_b() # Solution: 233537
