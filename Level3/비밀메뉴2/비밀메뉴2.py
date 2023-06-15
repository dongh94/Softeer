import sys
from pprint import pprint
sys.stdin = open("비밀메뉴2.txt")

N, M, K = map(int, input().split())
A = list(input().split())
B = list(input().split())
C = [[0] * M for _ in range(N)]
answer = 0
for r in range(N):
    for c in range(M):
        if A[r] == B[c]:
            if r == 0 or c == 0:
                C[r][c] = 1
            else:
                C[r][c] = C[r-1][c-1] + 1
        answer = max(answer, C[r][c])
print(answer)
