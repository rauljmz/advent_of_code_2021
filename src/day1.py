import sys
from functools import reduce
from typing import Iterable

def count_increases(values: Iterable):
    return reduce(lambda a, y: (y, a[1] + 1 if a[0] is not None and y > a[0] else a[1]), values, (None, 0))[1]

def window3(values: Iterable):
    return list(map(lambda x,y,z: x+y+z, values, values[1:], values[2:]))

if __name__ == "__main__":
    path = sys.argv[1]
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(int(line))
    print(f"{len(data)} values")
    print(f"{count_increases(window3(data))} are increasing over the previous")
