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


def most_common_digit(np_array: np.array):
    return np.floor(np_array.mean(axis=0) + 0.5).astype('int')


def part1(path):
    data = read_data(path)
    gamma_array = data.mean(axis=0).round().astype('int')
    epsilon_array = gamma_array ^ True
    return to_decimal(gamma_array) * to_decimal(epsilon_array)


def calculate_oxygen(data, column_no=0):
    column = data[:, column_no]
    most_common_digit_in_column = most_common_digit(column)
    mask = column == most_common_digit_in_column
    oxygen = data[mask]
    return calculate_oxygen(oxygen, column_no + 1) if len(oxygen) > 1 else to_decimal(oxygen[0])


def calculate_co2(data, column_no=0):
    column = data[:, column_no]
    most_common_digit_in_column = most_common_digit(column)
    mask = column != most_common_digit_in_column
    co2 = data[mask]
    return calculate_co2(co2, column_no + 1) if len(co2) > 1 else to_decimal(co2[0])


def part2(path):
    data = read_data(path)
    oxygen = calculate_oxygen(data)
    co2 = calculate_co2(data)
    return oxygen * co2


if __name__ == "__main__":
    print(f"{part2(sys.argv[1])} result of multiplying position")
