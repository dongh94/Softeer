import sys
from collections import deque
sys.stdin = open("이미지프로세싱.txt")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def changeColor(r, c, k):
    Q = deque()
    Q.append((r, c))

    K = arr[r][c]
    arr[r][c] = k

    visited = [[0] * W for _ in range(H)]
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                if arr[nr][nc] == K:
                    arr[nr][nc] = k
                    Q.append((nr,nc))
    return arr

H, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
N = int(input())
fixel = [list(map(int, input().split())) for _ in range(N)]
# print(fixel)
# 1. N번 fixel을 돌려가면서 바꿔준다. bfs에 넣고 돌리면 끝?
for i in range(N):
    r, c, k = fixel[i]
    arr = changeColor(r-1, c-1, k)
for i in range(len(arr)):
    print(*arr[i])


