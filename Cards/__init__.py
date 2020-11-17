import random


class Cards:
    def __init__(self):
        self.suits = ["clubs", "diamonds", "hearts", "spades"]
        self.values = [str(i) for i in range(2, 11)] + ["jack", "queen", "king", "ace"]
        self.colors = {"red": ["diamonds", "hearts"], "black": ["clubs", "spades"]}
        self.static_deck = list()
        for suit in self.suits:
            for value in self.values:
                self.static_deck.append((suit, value))
        self.current_deck = list(self.static_deck)

    def shuffle_deck(self):
        self.current_deck = random.sample(self.static_deck, len(self.static_deck))

    def draw(self, n=1, shuffle=False):
        if len(self.current_deck) < n:
            self.shuffle_deck()
        result = [self.current_deck.pop(0) for i in range(n)]
        if shuffle:
            self.shuffle_deck()
        return result
