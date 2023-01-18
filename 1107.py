import sys
from itertools import product
from functools import reduce


def input():
    return sys.stdin.readline()


if __name__ == "__main__":
    cur = 100
    n = int(input())
    m = int(input())
    d = dict()
    if m != 0:
        breaks = list(map(int, input().split()))
    else:
        breaks = []
    numbers = [i for i in range(10) if i not in breaks]

    if n == 100:
        print(0)
        exit(0)
    L = len(str(n))
    solves = dict()
    for i in range(1, 7):
        for array in product(numbers, repeat=i):
            temp = reduce(lambda x, y: str(x) + str(y), array, '')
            num = int(temp)
            if num in solves:
                solves[num] = min(solves[num], len(temp))
            else:
                solves[num] = len(temp)
    solves[100] = 0
    diff = 1e9
    for sol in solves:
        temp = abs(n - sol) + solves[sol]
        diff = min(temp, diff)
    print(diff)
