import sys
import numpy as np


def calculate_points(winner, number):
    winning_card = np.copy(winner)
    winning_card[winning_card == -1] = 0
    return np.absolute(winning_card.sum()) * number


class Bingo():
    numbers: np.array
    cards: np.array

    def __init__(self, numbers, cards) -> None:
        self.numbers = numbers
        self.cards = cards

    def _calculate_winner_index(self, axis):
        return np.where(self.cards.sum(axis=axis) ==
                          (self.cards.shape[axis] * -1))[0]

    def winner_index(self):
        for axis in range(1,len(self.cards.shape)):
            index = self._calculate_winner_index(axis)
            if(index.size > 0):
                return index

    def winner(self):
        index = self.winner_index()
        return self.cards[index] if index is not None else None

    def play(self):
        for number in self.numbers:
            self.cards[self.cards == number] = -1
            winner = self.winner()
            if winner is not None:
                return calculate_points(winner, number)

    def play_last_card(self):
        for number in self.numbers:
            self.cards[self.cards == number] = -1
            winner_index = self.winner_index()
            if winner_index is not None:
                if self.cards.shape[0] == 1:
                    return calculate_points(self.cards[winner_index], number)
                else:
                    self.cards = np.delete(self.cards, winner_index, axis=0)


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
        numbers=np.fromstring(numbers_line, dtype=int, sep=','),
        cards=np.block(cards),
    )


def part1(path):
    bingo = create_bingo_game(path)
    return bingo.play()


def part2(path):
    bingo = create_bingo_game(path)
    return bingo.play_last_card()


if __name__ == "__main__":
    print(f"{part2(sys.argv[1])} is the winning bingo score")
