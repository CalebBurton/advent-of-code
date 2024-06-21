import math
from functools import reduce

DAY_NUM = str(8).zfill(2)

class Node:
    def __init__(self, name, L, R):
        self.name = name
        self.L = L
        self.R = R

    def __str__(self):
        return f"Node(name={self.name}, L={self.L}, R={self.R})"

    def __repr__(self):
        return f"N({self.name})"

def process_input(file):
    instructions = list(file.readline().strip())
    file.readline() # Get rid of the blank line
    raw_nodes = file.read().strip().split('\n')
    nodes = list(map(lambda raw_node: process_raw_node(raw_node), raw_nodes))
    return (instructions, nodes)

def process_raw_node(raw_node):
    # convert raw text nodes into parsed nodes
    # given ["AA = (BB, CC)\n", ...] return [Node(name="AA", L="BB", R="CC"), ...]
    name, rest = raw_node.strip().split(' = ')
    L, R = rest.strip("()").split(", ")
    return Node(name, L, R)

def find_node_by_name(target_name, all_nodes):
    return next((node for node in all_nodes if node.name == target_name), None)

def find_num_steps(instructions, nodes):
    num_steps = 0
    concluded = False
    current_node = find_node_by_name("AAA", nodes)
    while not concluded:
        # print("Processing instructions")
        for instruction in instructions:
            num_steps += 1
            next_node = find_node_by_name(getattr(current_node, instruction), nodes)
            # print(f"step {num_steps} | current: {current_node}, instruction: {instruction}, next: {next_node}")
            if next_node.name == "ZZZ":
                concluded = True
            current_node = next_node
    print("Processing complete")
    return num_steps

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        instructions, nodes = process_input(file)
        result = find_num_steps(instructions, nodes)
    print(f"Result: {result}\n")

def find_all_nodes_by_name_suffix(target_suffix, all_nodes):
    return [node for node in all_nodes if node.name[-1] == target_suffix]

# # Not efficient enough...
# def find_num_simultaneous_steps(instructions, nodes):
#     num_steps = 0
#     concluded = False
#     current_nodes = find_all_nodes_by_name_suffix("A", nodes)
#     next_nodes = []
#     print(f"Simultaneity: {len(current_nodes)}")
#     while not concluded:
#         # print("Processing instructions")
#         # print(f"step {num_steps} | current: {current_nodes}")
#         for instruction in instructions:
#             num_steps += 1
#             next_nodes = [find_node_by_name(getattr(node, instruction), nodes) for node in current_nodes]
#             if any(node.name[-1] == "Z" for node in next_nodes):
#                 print(f"step {num_steps} | current: {current_nodes}, next: {next_nodes}")
#             if all(node.name[-1] == "Z" for node in next_nodes):
#                 concluded = True
#             current_nodes = next_nodes
#     print("Processing complete")
#     return num_steps

def lcm(x, y):
    mul = x * y
    gcd = math.gcd(x, y)
    result = int(mul / gcd)
    # print(f"lcm({x, y}) = mul({mul}) / gcd({gcd}) = {result}")
    return result

def lcm_list(numbers):
    return reduce(lcm, numbers)

def find_cycles(instructions, nodes):
    current_nodes = find_all_nodes_by_name_suffix("A", nodes)
    total_nodes = len(current_nodes)
    path_lengths = []
    for i, node in enumerate(current_nodes):
        # find how many steps it takes to get back to itself
        concluded = False
        num_steps = 0
        current_node = node
        while not concluded:
            for j, instruction in enumerate(instructions):
                num_steps += 1
                next_node = find_node_by_name(getattr(current_node, instruction), nodes)
                # print(f"step {num_steps} | current: {current_node}, next: {next_node}")
                if next_node.name[-1] == "Z" and j == len(instructions) - 1:
                    concluded = True
                current_node = next_node
        print(f"Processing complete for node {i + 1} of {total_nodes}: {num_steps}")
        path_lengths.append(num_steps)
    print(path_lengths)
    return lcm_list(path_lengths)

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        instructions, nodes = process_input(file)
        result = find_cycles(instructions, nodes)
    print(f"Result: {result}\n")

def test_puzzle_a():
    print("-- Test A1 --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        instructions, nodes = process_input(file)
        actual = find_num_steps(instructions, nodes)
        expected = 2
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

    print("-- Test A2 --")
    with open(f"{DAY_NUM}_test_input_2.txt") as file:
        instructions, nodes = process_input(file)
        actual = find_num_steps(instructions, nodes)
        expected = 6
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_3.txt") as file:
        instructions, nodes = process_input(file)
        # actual = find_num_simultaneous_steps(instructions, nodes)
        actual = find_cycles(instructions, nodes)
        expected = 6
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    test_puzzle_a()
    puzzle_a() # Solution: 19631
    test_puzzle_b()
    puzzle_b() # Solution: 21003205388413