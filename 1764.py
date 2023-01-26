import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n, m = map(int, input().split())
    x = set([input() for _ in range(n)])
    y = set([input() for _ in range(m)])
    res = sorted(list(x & y))
    print(len(res))
    for r in res:
        print(r)
