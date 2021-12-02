import sys
from functools import reduce
from typing import Iterable

def count_increases(values: Iterable):
    return reduce(lambda a, y: (y, a[1] + 1 if a[0] != None and y > a[0] else a[1]), values, (None, 0))[1]

if __name__ == "__main__":
    path = sys.argv[1]
    file = open(path, "r")
    values = file.read().split(",")
    values = list(map(lambda x: int(x), values))
    print(f"{len(values)} values")
    print(f"{count_increases(values)} are increasing over the previous")