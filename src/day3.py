import sys
import numpy as np


def read_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            digits = [int(digit) for digit in list(line.strip())]
            data.append(digits)
    return np.array(data)


def to_decimal(arr):
    to_decimal_array = 2 ** np.arange(len(arr)-1, -1, -1)
    return (arr*to_decimal_array).sum()


def part1(path):
    data = read_data(path)
    gamma_array = data.mean(axis=0).round().astype('int')
    epsilon_array = gamma_array ^ True
    return to_decimal(gamma_array) * to_decimal(epsilon_array)


if __name__ == "__main__":
    print(f"{part1(sys.argv[1])} result of multiplying position")
