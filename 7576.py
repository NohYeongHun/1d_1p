import sys


def input():
    return sys.stdin.readline().rstrip()


def check(board):
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return False
    return True


def solve(q, board):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    temp = []
    while q:
        r, c = q.pop()
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]

            if dr < 0 or dr >= n or dc < 0 or dc >= m:
                continue
            if board[dr][dc] == 0:
                board[dr][dc] = 1
                temp.append([dr, dc])
    return temp


if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        board.append(arr)
    q = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append([i, j])

    for cnt in range(1_000_000):
        q = solve(q, board)

        if not q:
            if check(board):
                print(cnt)
                exit(0)
            else:
                print(-1)
                exit(0)
