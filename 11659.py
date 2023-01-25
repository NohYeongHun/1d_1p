import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = [0] + list(map(int, input().split()))
    cmd = [list(map(int, input().split())) for _ in range(M)]
    dp = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + numbers[i]

    for s, e in cmd:
        print(dp[e] - dp[s - 1])
