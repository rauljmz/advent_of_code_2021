import sys
import numpy as np

def calculate_points(winner, number):
    winning_card = np.copy(winner)
    winning_card[winning_card == -1] = 0
    return np.absolute(winning_card.sum()) * number

class Bingo():
    numbers: np.array
    cards: np.array
    def __init__(self,numbers, cards) -> None:
        self.numbers = numbers
        self.cards = cards
    
    def winner(self):
        winner_by_row = np.where(self.cards.sum(axis=2) == (self.cards.shape[2] * -1))[0]
        if winner_by_row.size > 0:
            return self.cards[winner_by_row]
        winner_by_column = np.where(self.cards.sum(axis=1) == self.cards.shape[1] * -1)[0]
        if winner_by_column.size > 0:
            return self.cards[winner_by_column]
        return None

    def play(self):
        for number in self.numbers:
            self.cards[self.cards == number] = -1
            winner = self.winner()
            if winner is not None:
                return calculate_points(winner, number)

def create_bingo_game(path) -> Bingo:
    cards = []
    with open(path) as file:
        numbers_line = file.readline()
        text_line = file.readline()
        text_line = file.readline()
        card = []
        while text_line != "": 
            if text_line != "\n": 
                card.append([np.fromstring(text_line, sep=' ', dtype='int')])
            else:      
                cards.append(card)
                card = []
            text_line = file.readline()
        if len(card) == 5:
            cards.append(card)

    return Bingo(
            numbers = np.fromstring(numbers_line, dtype=int, sep=','),
            cards = np.block(cards),
    )


def part1(path):
    bingo = create_bingo_game(path)
    return bingo.play()


if __name__ == "__main__":
    print(f"{part1(sys.argv[1])} is the winning bingo score")