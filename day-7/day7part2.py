from collections import defaultdict, Counter
from functools import cmp_to_key

input = []
card_strength = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 1,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

def check_five_of_a_kind(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [5] == list(tmp.values())

def check_four_of_a_kind(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [1,4] == sorted(tmp.values())

def check_full_house(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [2,3] == sorted(tmp.values())

def check_three_of_a_kind(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [1,1,3] == sorted(tmp.values())

def check_two_pair(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [1,2,2] == sorted(tmp.values())

def check_one_pair(hand):
    tmp = defaultdict(int)
    for card in hand:
        tmp[card] += 1
    return [1,1,1,2] == sorted(tmp.values())

def check_hand(hand):
    if check_five_of_a_kind(hand):
        return 7
    if check_four_of_a_kind(hand):
        return 6
    if check_full_house(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pair(hand):
        return 3
    if check_one_pair(hand):
        return 2
    return 1

def card_compare(card1, card2):
    if card_strength[card1] > card_strength[card2]:
        return 1
    else:
        return -1

def hand_compare(hand1, hand2):
    new_hand1 = replace_hand(hand1)
    new_hand2 = replace_hand(hand2)

    if check_hand(new_hand1) > check_hand(new_hand2):
        return 1
    elif check_hand(new_hand1) < check_hand(new_hand2):
        return -1
    else:
        for x,y in zip(hand1, hand2):
            if(card_strength[x] > card_strength[y]):
                return 1
            elif(card_strength[x] < card_strength[y]):
                return -1
            else:
                continue

def replace_hand(hand):
    if 'J' not in hand:
        return hand
    if hand == 'JJJJJ':
        return 'AAAAA'
    partial_hand = hand.replace('J','')
    counts = dict(Counter(partial_hand))
    most_freq_card = max(counts, key=counts.get)
    max_count = counts[most_freq_card]
    
    if len(partial_hand) == 1:
        new_hand = hand.replace('J', partial_hand[0])
    else:
        if len(counts) == 2 or max_count > 1:
            new_hand = hand.replace('J', most_freq_card)
        else:
            new_hand = hand.replace('J', sorted(partial_hand, key=cmp_to_key(card_compare))[-1])
    return new_hand

hand_bid_map = {}
hands = []
sum = 0
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            hand = line.split(' ')[0]
            bid = int(line.split(' ')[1])
            hand_bid_map[hand] = bid
            hands.append(hand)
        hands = sorted(hands, key=cmp_to_key(hand_compare))
        for i in range(len(hands)):
            sum += ((i+1) * hand_bid_map[hands[i]])
        print(sum)

        
