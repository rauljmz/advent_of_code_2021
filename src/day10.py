from collections import deque
from sys import argv
import numpy as np
from functools import reduce

open_symbols = "{(<["
close_symbols = "})>]"

points_corrupted = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points_incomplete = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def part1(path):
    score = 0
    stack = deque()
    with open(path) as file:
        for line in file.readlines():
            stack.clear()
            for symbol in line.strip():
                if symbol in open_symbols:
                    stack.append(close_symbols[open_symbols.index(symbol)])
                else:
                    if symbol != stack.pop():
                        score += points_corrupted.get(symbol)
                        continue
    return score


def part2(path):
    scores = []
    stack = deque()
    with open(path) as file:
        for line in file.readlines():
            for symbol in line.strip():
                if symbol in open_symbols:
                    stack.append(close_symbols[open_symbols.index(symbol)])
                else:
                    if symbol != stack.pop():
                        stack.clear()
                        break
            if len(stack) > 0:
                stack.reverse()
                scores.append(reduce(lambda acu, ele: acu *
                                5 + points_incomplete.get(ele), stack, 0))
                stack.clear()
    return int(np.median(np.array(scores)))

if __name__ == "__main__":
    print(f"score is {part2(argv[1])}")
