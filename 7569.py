import sys
from collections import deque


def input():
    return sys.stdin.readline()


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    box = [[] for _ in range(H)]
    dx, dy, dz = [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]

    q = deque()
    for i in range(H):
        temp = [list(map(int, input().split())) for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if temp[r][c] == 1:
                    q.appendleft([i, r, c])
        box[i] = temp

    new_q = 1
    cnt = -1
    while new_q:
        new_q = deque()
        
        while q:
            h, r, c = q.popleft()

            for k in range(6):
                dh, dr, dc = h + dz[k], r + dy[k], c + dx[k]

                if dh < 0 or dh >= H or dr < 0 or dr >= N or dc < 0 or dc >= M:
                    continue

                if box[dh][dr][dc] == 0:
                    new_q.appendleft([dh, dr, dc])
                    box[dh][dr][dc] = 1
        cnt += 1
        q = new_q

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    print(-1)
                    exit(0)

    print(cnt)
