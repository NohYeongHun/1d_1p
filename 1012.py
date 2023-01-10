# 1012
from collections import deque
def solution(m, n, k):
    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        c, r = map(int, input().split())
        board[r][c] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                sub_ploblem(board, i, j)
                cnt += 1
    print(cnt)    
    return

def sub_ploblem(board, r, c):
    n = len(board)
    m = len(board[0])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append([r, c])
    
    board[r][c] = 0
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]

            if dr < 0 or dr >= n or dc < 0 or dc >=m:
                continue
            
            if board[dr][dc] == 1:
                board[dr][dc] = 0
                q.append([dr, dc])

    return


if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        m, n, k = map(int, input().split())
        solution(m, n, k)
