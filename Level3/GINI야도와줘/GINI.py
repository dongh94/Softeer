import sys
from collections import deque
sys.stdin = open("GINI.txt")

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# . 이동, * 소나기, X는 강이라 못가, H는 집, W는 세차장.
# 1. 세차장에서 출발한다. Q 상우좌하 돌리면서 바로 다음 for문에 소나기를 확산시킨다.
# 2. visited를 count로 쓴다.
# 3. H도착 시 visited를 answer로 한다. 끝.

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[0] * C for _ in range(R)]


def goHome(r, c, rain):
    Q = deque()

    # 소나기온 뒤
    for y, x in rain:
        Q.append((y, x))
    # 차 이동
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()

        if arr[sr][sc] == 'W' or arr[sr][sc] == '.':
            for d in range(4):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0<= nr < R and 0<= nc < C:
                    if visited[nr][nc] == 0:
                        if arr[nr][nc] == '.':
                            visited[nr][nc] = visited[sr][sc] + 1
                            Q.append((nr, nc))
                        if arr[nr][nc] == 'H':
                            return visited[sr][sc]

        elif arr[sr][sc] == '*':
            for d in range(4):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0<= nr < R and 0<= nc < C:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = '*'
                        Q.append((nr,nc))

    return -1

# 출발
def start(rain):
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'W':
                ans = goHome(r, c, rain)
                if ans == -1:
                    return "FAIL"
                else:
                    return ans

# 소나기 찾고
rain = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == '*':
            rain.append((r, c))
# 출발
answer = start(rain)
print(answer)


