from collections import Counter

DAY_NUM = str(7).zfill(2)

USING_JOKERS = True

HAND_RANKS = {
    "HIGH_CARD": 1,
    "ONE_PAIR": 2,
    "TWO_PAIR": 3,
    "THREE_OF_A_KIND": 4,
    "FULL_HOUSE": 5,
    "FOUR_OF_A_KIND": 6,
    "FIVE_OF_A_KIND": 7,
}

CARD_RANKS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11, # Will be overwritten if using Jokers
    "Q": 12,
    "K": 13,
    "A": 14,
}

if USING_JOKERS:
    CARD_RANKS['J'] = 1

def compare_individual_cards(x_cards, y_cards):
    x_card_vals = [CARD_RANKS[card] for card in x_cards]
    y_card_vals = [CARD_RANKS[card] for card in y_cards]
    for x_card_val, y_card_val in zip(x_card_vals, y_card_vals):
        if x_card_val != y_card_val:
            is_x_smaller = x_card_val < y_card_val
            # print(f"    {x_card_val} vs {y_card_val} -> { 'first' if is_x_smaller else 'second' } is smaller.")
            return is_x_smaller
        else:
            # print(f"    {x_card_val} vs {y_card_val} -> tie. Checking next card in hand.")
            pass

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __str__(self):
        return f"H({self.cards}, {self.bid})"

    def __repr__(self):
        return f"H({self.cards})"

    def __lt__(x, y):
        # print(f"Comparing hand ranks:")
        x_rank = x.hand_rank_with_jokers() if USING_JOKERS else x.hand_rank()
        y_rank = y.hand_rank_with_jokers() if USING_JOKERS else y.hand_rank()
        if x_rank == y_rank:
            # print(f"  {x} vs {y} -> tie ({x_rank}). Comparing individual cards")
            return compare_individual_cards(x.cards, y.cards)
        else:
            is_x_smaller = x_rank < y_rank
            # print(f"  {x} vs {y} -> { 'first' if is_x_smaller else 'second' } is smaller")
            return is_x_smaller

    def hand_rank(self):
        card_count = Counter(self.cards)
        if USING_JOKERS:
            # Don't count the jokers toward the normal hand rank, they'll be counted later
            card_count['J'] = 0
        num_pairs = sum(1 for count in card_count.values() if count > 1)
        if num_pairs > 1:
            top_two = card_count.most_common(2)
            if top_two[0][1] == 3 and top_two[1][1] == 2:
                return HAND_RANKS['FULL_HOUSE']
            else:
                return HAND_RANKS['TWO_PAIR']
        max_count = max(card_count.most_common(1))[1]
        if max_count == 5:
            return HAND_RANKS['FIVE_OF_A_KIND']
        elif max_count == 4:
            return HAND_RANKS['FOUR_OF_A_KIND']
        elif max_count == 3:
            return HAND_RANKS['THREE_OF_A_KIND']
        elif max_count == 2:
            return HAND_RANKS['ONE_PAIR']
        else:
            return HAND_RANKS['HIGH_CARD']

    def hand_rank_with_jokers(self):
        rank = self.hand_rank()
        if 'J' not in self.cards:
            # print(f"No jokers in hand {self.cards}. Returning initial hand rank of {rank}.")
            return rank
        num_jokers = self.cards.count('J')
        for _ in range(num_jokers):
            # Initial value       -> Result after adding a Joker
            # ==================================================
            # High card       (1) -> One pair (2)
            # One pair        (2) -> Three of a kind (4)
            # Two pair        (3) -> Full house (5)
            # Three of a kind (4) -> Four of a kind (6)
            # Full house      (5) -> Four of a kind (6)
            # Four of a kind  (6) -> Five of a kind (7)
            # Five of a kind  (7) -> Five of a kind (7)
            # print(f"Using joker from hand {self.cards}. Starting hand rank is {rank}.", end=" ")
            if rank == 1:
                rank = 2
            elif rank == 2:
                rank = 4
            elif rank == 3:
                rank = 5
            elif rank == 4:
                rank = 6
            elif rank == 5:
                rank = 6
            elif rank == 6:
                rank = 7
            else:
                rank = 7
            # print(f"New hand rank is {rank}.")
        return rank

def process_input(file):
    lines = file.read().strip().split('\n')
    hands = [Hand(cards=line.split(' ')[0], bid=int(line.split(' ')[1])) for line in lines]
    return hands

def get_winnings_for_hands(hands):
    sorted_hands = list(sorted(hands)) # uses the __lt__ method by default
    print(f"sorted_hands: {sorted_hands}")
    individual_winnings = [hand.bid * (index + 1) for index, hand in enumerate(sorted_hands)]
    # print(f"individual_winnings: {individual_winnings}, sum: {sum(individual_winnings)}")
    return sum(individual_winnings)

def puzzle_a():
    print("-- Puzzle A --")
    with open(f"{DAY_NUM}_input.txt") as file:
        hands = process_input(file)
        result = get_winnings_for_hands(hands)
    print(f"Result: {result}\n")

def puzzle_b():
    print("-- Puzzle B --")
    with open(f"{DAY_NUM}_input.txt") as file:
        hands = process_input(file)
        result = get_winnings_for_hands(hands)
    print(f"Result: {result}\n")

# =============================================================================

def test_puzzle_a():
    print("-- Test A --")
    with open(f"{DAY_NUM}_test_input_1.txt") as file:
        hands = process_input(file)
        actual = get_winnings_for_hands(hands)
        expected = 6440
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

def test_puzzle_b():
    print("-- Test B --")
    with open(f"{DAY_NUM}_test_input_2.txt") as file:
        hands = process_input(file)
        actual = get_winnings_for_hands(hands)
        expected = 5905
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

    print("-- Test B2 --")
    with open(f"{DAY_NUM}_test_input_3.txt") as file:
        hands = process_input(file)
        actual = get_winnings_for_hands(hands)
        expected = actual
        print(f"Actual: {actual}  //  Expected: {expected}\n")
        assert actual == expected

if __name__ == "__main__":
    print(f"\n\n==== Day {DAY_NUM} ====")
    # test_puzzle_a()
    # puzzle_a() # Solution: 248559379
    test_puzzle_b()
    puzzle_b() # Solution: 249631254
