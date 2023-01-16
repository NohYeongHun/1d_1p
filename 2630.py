import sys


def input():
    return sys.stdin.readline()


def check_board(board, r, c, n):
    color = board[r][c]

    for i in range(0, n):
        for j in range(0, n):
            if board[r + i][c + j] != color:
                return False
    return True


if __name__ == "__main__":
    n = int(input())
    board = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        temp = list(map(int, input().split()))
        board.append([0] + temp)

    white, blue = 0, 0

    def dfs(board, n, r, c):
        global white, blue
        if n == 1:
            if board[r][c] == 0:
                white += 1
            else:
                blue += 1
        else:
            if check_board(board, r, c, n):
                color = board[r][c]
                if color == 0:
                    white += 1
                elif color == 1:
                    blue += 1
                return
            else:
                dfs(board, n // 2, r, c)
                dfs(board, n // 2, r + n // 2, c)
                dfs(board, n // 2, r, c + n // 2)
                dfs(board, n // 2, r + n // 2, c + n // 2)
            return
        return
    dfs(board, n, 1, 1)

    print(white)
    print(blue)
