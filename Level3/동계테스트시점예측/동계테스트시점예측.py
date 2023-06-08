import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("동계테스트시점예측.txt")
input = sys.stdin.readline


def check(r, c):
    Q = deque()
    Q.append((r, c))
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                # 1 보이면 바로 += 1 끝.
                if arr[nr][nc] == 1:
                    visited[nr][nc] += 1
                elif arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr,nc))

    for x in range(N):
        for y in range(M):
            if visited[x][y] >= 2:
                arr[x][y] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0

while True:
    if sum(sum(row) for row in arr) == 0:
        break
        
    else:
        check(0, 0)
        answer += 1
print(answer)


