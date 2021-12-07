import sys
import numpy as np

def memoize(f):
    memo = {}
    def helper(x,y):
        if (x,y) not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper

@memoize
def count_from_single_fish(initial, days):
    count = 1
    for reproduction_day in range(initial + 1, days + 1, 7):
        count += count_from_single_fish(8, days-reproduction_day)
    return count


def count_fish(path, days):
    with open(path) as file:
        initial_states = np.fromstring(file.readline(), sep=',', dtype=np.uint)

    fn = np.frompyfunc(count_from_single_fish, 2, 1)

    return fn(1,np.arange(days,days-6,-1))[initial_states-1].sum()


if __name__ == "__main__":
    days = int(sys.argv[1])
    path = sys.argv[2]
    print(f"{count_fish(path, days)} fish after {days} days")
