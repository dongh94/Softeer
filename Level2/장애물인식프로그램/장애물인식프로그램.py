import sys; sys.stdin=open("장애물인식프로그램.txt")
from collections import deque;

# 상 하 좌 우
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def BFS(r,c):
    arr[r][c] = 0
    count = 1
    Q = deque([(r,c)])
    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue;
            if arr[nr][nc] == 1:
                arr[nr][nc] = 0
                count += 1
                Q.append((nr,nc))

    answer_list.append(count)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
answer_list = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            BFS(r,c)

answer_N = len(answer_list)
print(answer_N)
print(*sorted(answer_list), sep='\n')
