from collections import Counter

with open('p054_poker.txt') as file:
    x = file.readlines()
    hands = [(i[:14].split(), i[15:-1].split()) for i in x]

num_dict = {**dict(zip([str(x) for x in range(1,10)], range(1,10))), **{'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}}

def get_streak(numbers):
    streak = 0
    for i in range(4):
        if numbers[i + 1] - numbers[i] == 1:
            streak += 1
        else:
            streak = 0
    return streak

def calculate_hand(hand):
    numbers, suits = sorted([num_dict[i[0]] for i in hand]), [i[1] for i in hand]
    streak = get_streak(numbers)
    counts = sorted(Counter(numbers).values())
    rating = rate_hand(numbers, suits, streak, counts)
    return rating, numbers

def rate_hand(numbers, suits, streak, counts):
    if len(set(suits)) == 1:
        if streak == 4:
            if numbers[0] == 10:
                return 23  # royal flush
            else:
                return 22  # straight flush
    if counts[-1] == 4:
        return 21  # four of a kind
    if counts[-1] == 3 and counts[-2] == 2:
        return 20  # full house
    if len(set(suits)) == 1:
        return 19  # flush
    if streak == 4:
        return 18  # straight
    if counts[-1] == 3:
        return 17  # three of a kind
    if counts[-1] == 2:
        if counts[-2] == 2:
            return 16  # two pairs
        return 15  # one pair
    return numbers[-1]  # returns highest card

def compare_hands(hand_pair):
    score_a, numbers_a = calculate_hand(hand_pair[0])
    score_b, numbers_b = calculate_hand(hand_pair[1])
    if score_a != score_b:
        return score_a > score_b
    if score_a > 14:  # there are combinations to compare
        numbers_a = [i[0] for i in sorted(Counter(numbers_a).items(), key=lambda kv: kv[1])]
        numbers_b = [i[0] for i in sorted(Counter(numbers_b).items(), key=lambda kv: kv[1])]
    for i in range(-1,-6, -1):
        if numbers_a[i] != numbers_b[i]:
            return numbers_a[i] > numbers_b[i]

print(sum([compare_hands(i) for i in hands]))
