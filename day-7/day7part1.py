from collections import defaultdict
from functools import cmp_to_key

input = []
card_strenght = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 11,
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

def hand_compare(hand1, hand2):
    if check_hand(hand1) > check_hand(hand2):
        return 1
    elif check_hand(hand1) < check_hand(hand2):
        return -1
    else:
        for x,y in zip(hand1, hand2):
            if(card_strenght[x] > card_strenght[y]):
                return 1
            elif(card_strenght[x] < card_strenght[y]):
                return -1
            else:
                continue

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

        
