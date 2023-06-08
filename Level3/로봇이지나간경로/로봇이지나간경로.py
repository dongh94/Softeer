import sys
from pprint import pprint
sys.stdin = open("로봇이지나간경로.txt")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dm = ["^", "<", "v", ">"]
dr = [-1, 0, 1, 0] # 상좌하우
dc = [0, -1, 0, 1]

def findD(r, c):
    count = 0
    direct = -1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '#':
            count += 1
            direct = d
    return direct if count == 1 else -1

def findStart(arr):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                direct = findD(r, c)
                if direct != -1:
                    return r, c, direct

def navi(r, c, d):
    newD = preD = d
    arr[r][c] = '.'
    while True:
        while newD == preD:
            print('A', end="")
            for _ in range(2):
                r = r + dr[newD]
                c = c + dc[newD]
                arr[r][c] = '.'

            preD = newD
            newD = findD(r, c)

        # 상좌하우 0, 1, 2, 3 pre
        # 좌하우상 1, 2, 3, 0 new = 1, 1, 1, -3 => ((-3 % 4) + 4) % 4
        # 우상좌하 3, 0, 1, 2 new = 3, -1, -1, -1 => ((-1 % 4) + 4) % 4
        if newD == -1:
            return
        elif (newD - preD) % 4 == 1:
            print('L', end="")
        elif (newD - preD) % 4 == 3:
            print('R', end="")
        preD = newD


r, c, d = findStart(arr)
print(r+1, c+1)
print(dm[d])
navi(r, c, d)










