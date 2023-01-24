import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def sub(pos, board, visited):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    r, c = pos
    color = board[r][c]
    q = deque()
    q.appendleft([r, c])

    while q:
        r, c = q.popleft()
        for k in range(4):
            dr, dc = r + dx[k], c + dy[k]
            if dr < 0 or dr >= n or dc < 0 or dc >= n:
                continue
            if visited[dr][dc]:
                continue

            if board[dr][dc] == color:
                q.appendleft([dr, dc])
                visited[dr][dc] = True
    return


def solve1(board):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sub([i, j], board, visited)
                cnt += 1

    return cnt


def solve2(board):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        board[i] = board[i].replace('R', 'G')

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sub([i, j], board, visited)
                cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    board = [input() for _ in range(n)]
    print(solve1(board))
    print(solve2(board))
