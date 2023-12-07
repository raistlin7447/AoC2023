import functools
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum


class Card(IntEnum):
    CARD_J = 1
    CARD_2 = 2
    CARD_3 = 3
    CARD_4 = 4
    CARD_5 = 5
    CARD_6 = 6
    CARD_7 = 7
    CARD_8 = 8
    CARD_9 = 9
    CARD_T = 10
    CARD_Q = 11
    CARD_K = 12
    CARD_A = 13


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
@functools.total_ordering
class Hand:
    cards: str
    bid: int = 0

    def get_type(self):
        c = Counter(self.cards)

        if "J" in self.cards:
            for card in c.most_common(2):
                if card[0] != "J":
                    c = Counter(self.cards.replace("J", card[0]))
                    break

        most_common = c.most_common()[0][1]
        next_most_common = c.most_common()[1][1] if len(c.most_common()) > 1 else 0

        match most_common, next_most_common:
            case 5, 0:
                return HandType.FIVE_OF_A_KIND
            case 4, 1:
                return HandType.FOUR_OF_A_KIND
            case 3, 2:
                return HandType.FULL_HOUSE
            case 3, 1:
                return HandType.THREE_OF_A_KIND
            case 2, 2:
                return HandType.TWO_PAIR
            case 2, 1:
                return HandType.ONE_PAIR
            case 1, 1:
                return HandType.HIGH_CARD

    def break_tie(self, other):
        for i in range(5):
            self_card = Card["CARD_" + self.cards[i]]
            other_card = Card["CARD_" + other.cards[i]]
            if self_card == other_card:
                continue
            else:
                return -1 if self_card < other_card else 1
        else:
            return 0

    def __ge__(self, other):
        if self.get_type() == other.get_type():
            return self.break_tie(other) >= 0
        return self.get_type() >= other.get_type()

    def __eq__(self, other):
        if self.get_type() == other.get_type():
            return self.break_tie(other) == 0
        return self.get_type() == other.get_type()

    def __repr__(self):
        return f"{self.cards}: {self.get_type().name} {self.bid}"


hands = []
with open('day07_input.txt') as f:
    for line in f:
        hand, bid = line.split()
        hands.append(Hand(hand, int(bid)))


hands.sort()
print(sum([i * hand.bid for i, hand in enumerate(hands, start=1)]))
